from typing import TYPE_CHECKING, Any, List, Optional, Union, Dict
import json
import httpx
import json

import litellm
from litellm.llms.base_llm.chat.transformation import BaseConfig, BaseLLMException
from litellm.types.llms.openai import AllMessageValues
from litellm.types.utils import ModelResponse, Usage
from ..utils import validate_environment as edenai_validate_environment
if TYPE_CHECKING:
    from litellm.litellm_core_utils.litellm_logging import Logging as _LiteLLMLoggingObj

    LiteLLMLoggingObj = _LiteLLMLoggingObj
else:
    LiteLLMLoggingObj = Any


class EdenAIError(BaseLLMException):
    def __init__(self, status_code: int, message: str, headers: Optional[httpx.Headers] = None):
        self.status_code = status_code
        self.message = message
        self.request = httpx.Request(method="POST", url="https://api.edenai.run/v2/multimodal/chat")
        self.response = httpx.Response(status_code=status_code, request=self.request)
        super().__init__(status_code=status_code, message=message, headers=headers)


class EdenAIChatConfig(BaseConfig):
    temperature: Optional[float] = 0
    max_tokens: Optional[int] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    chat_global_actions: Optional[bool] = None
    stop_sequences: Optional[List[str]] = None
    api_key: Optional[str] = None
    tools: Optional[list] = None
    tool_results: Optional[list] = None

    def __init__(
        self,
        temperature: Optional[float] = 0,
        max_tokens: Optional[int] = None,
        api_key: Optional[str] = None,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        chat_global_actions: Optional[bool] = None,
        stop_sequences: Optional[List[str]] = None,
    ) -> None:
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key
        self.top_p = top_p
        self.top_k = top_k
        self.chat_global_actions = chat_global_actions
        self.stop_sequences = stop_sequences



    def get_supported_openai_params(self, model: str) -> List[str]:
        return [
            "temperature",
            "max_tokens",
            "top_p",
            "top_k",
            "stop",
            "tools",
            "tool_choice"
        ]
    def map_openai_params(
        self,
        non_default_params: dict,
        optional_params: dict,
        model: str,
        drop_params: bool,
    ) -> dict:
        for param, value in non_default_params.items():
            if param == "temperature":
                optional_params["temperature"] = value
            if param == "max_tokens":
                optional_params["max_tokens"] = value
            if param == "n":
                optional_params["num_generations"] = value
            if param == "top_p":
                optional_params["p"] = value
            if param == "stop":
                optional_params["stop_sequences"] = value
            if param == "tools":
                optional_params["available_tools"] = value

        return optional_params
    
    def validate_environment(
        self,
        headers: dict,
        model: str,
        messages: List[AllMessageValues],
        optional_params: dict,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
    ) -> dict:
        return edenai_validate_environment(
            headers=headers,
            model=model,
            messages=messages,
            optional_params=optional_params,
            api_key=api_key,
        )
    
    def _is_multimodal_request(self, messages: List[AllMessageValues]) -> bool:
        """
        Check if the request is a multimodal request by inspecting the content of the messages.

        Args:
            messages (List[AllMessagesValues]): The list of messages to check.

        Returns:
            bool: True if the request is multimodal, False otherwise.
        """
        for msg in messages:
            content = msg.get("content", "")
            if isinstance(content, str):
                try:
                    parsed_content = json.loads(content)
                    if isinstance(parsed_content, list):
                        for item in parsed_content:
                            if isinstance(item, dict) and "type" in item and item["type"] in ["text", "media_url","media_base64"]:
                                return True

                except json.JSONDecodeError:
                    continue
        return False

    def _process_multimodal_messages(self, messages: List[AllMessageValues]) -> List[Dict[str, Any]]:
        """
        Process messages for a multimodal request by parsing the content.

        Args:
            messages (List[AllMessagesValues]]): The list of messages.

        Returns:
            List[Dict[str, Any]]: The processed list of messages.
        """
        formatted_messages = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]

            if isinstance(content, str):
                try:
                    parsed_content = json.loads(content)
                    formatted_messages.append({"role": role, "content": parsed_content})
                except json.JSONDecodeError:
                    raise ValueError("Malformed JSON in multimodal message content")
            else:
                raise ValueError("Unsupported content format for multimodal request")

        return formatted_messages

    def format_tools(self, tools: list) -> list:
        """
        Format the available tools for the API request.

        Args:
            tools (list): The list of available tools.

        Returns:
            dict: The formatted tools.
        """
        formatted_tools = []
        for tool in tools:
            function_data = tool['function']
            formatted_tool = {
                "name": function_data['name'],
                "description": function_data['description'],
                "parameters": {
                    "type": function_data['parameters']['type'],
                    "properties": function_data['parameters']['properties'],
                    "required": function_data['parameters']['required']
                }
            }
            formatted_tools.append(formatted_tool)
        return formatted_tools

    def transform_request(
        self,
        model: str,
        messages: List[AllMessageValues],
        optional_params: dict,
        litellm_params: dict,
        headers: dict,
    ) -> dict:
        if self._is_multimodal_request(messages):
            formatted_messages = self._process_multimodal_messages(messages)
        else:
            formatted_messages = [
                {"role": msg["role"], "content": [{"type": "text", "content": {"text": msg["content"]}}]}
                for msg in messages
            ]

        available_tools_param = optional_params.get("available_tools")

        if available_tools_param is not None:
            text = formatted_messages[0]["content"][0]["content"].get("text", "") if formatted_messages else ""
            available_tools = self.format_tools(available_tools_param)
            payload = {
                **optional_params,
                "available_tools": available_tools,
                "providers": [model],
                "text": text,
                "response_as_dict": True,
                "attributes_as_list": False,
                "show_base_64": True,
                "show_original_response": True,
            }
        else:
            payload = {
                **optional_params,
                "providers": [model],
                "messages": formatted_messages,
                "response_as_dict": True,
                "attributes_as_list": False,
                "show_base_64": True,
                "show_original_response": True,
            }

        return payload
    def transform_response(
        self,
        model: str,
        raw_response: httpx.Response,
        model_response: ModelResponse,
        logging_obj: LiteLLMLoggingObj,
        request_data: dict,
        messages: List[AllMessageValues],
        optional_params: dict,
        litellm_params: dict,
        encoding: Any,
        api_key: Optional[str] = None,
        json_mode: Optional[bool] = None,
    ) -> ModelResponse:
        try:
            raw_response_json = raw_response.json()
            provider_response = raw_response_json.get(model, {})

            model_response.choices[0].message.content = provider_response.get("generated_text", "")

            original_response = provider_response.get("original_response", {})
            usage_data = original_response.get("usage", {})

            prompt_tokens = usage_data.get("prompt_tokens", 0)
            completion_tokens = usage_data.get("completion_tokens", 0)
            total_tokens = usage_data.get("total_tokens", 0)

            completion_tokens_details = usage_data.get("completion_tokens_details")
            prompt_tokens_details = usage_data.get("prompt_tokens_details")

            model_response.usage = Usage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=total_tokens,
                completion_tokens_details=completion_tokens_details,
                prompt_tokens_details=prompt_tokens_details,
            )
            
            # handle tools 
            tool_calls = []
            message_list = provider_response.get("message", [])

            if len(message_list) > 1 and message_list[1].get("tool_calls"):
                tool_calls = message_list[1]["tool_calls"]

            if tool_calls:
                formatted_tool_calls = []
                for tool in tool_calls:
                    tool_call = {
                        "id": tool.get("id", ""),
                        "type": "function",
                        "function": {
                            "name": tool.get("name", ""),
                            "arguments": tool.get("arguments", "{}"),
                        },
                    }
                    formatted_tool_calls.append(tool_call)

                _message = litellm.Message(
                    tool_calls=formatted_tool_calls,
                    content=None,
                )
                model_response.choices[0].message = _message 

        except Exception as e:
            raise EdenAIError(status_code=raw_response.status_code, message=str(e))

        return model_response



    def get_error_class(
        self, error_message: str, status_code: int, headers: Union[dict, httpx.Headers]
    ) -> BaseLLMException:
        return EdenAIError(status_code=status_code, message=error_message, headers=headers)
