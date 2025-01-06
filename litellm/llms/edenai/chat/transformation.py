import json
import time
from typing import TYPE_CHECKING, Any, AsyncIterator, Iterator, List, Optional, Union

import httpx

import litellm
from litellm.litellm_core_utils.prompt_templates.factory import cohere_messages_pt_v2
from litellm.llms.base_llm.chat.transformation import BaseConfig, BaseLLMException
from litellm.types.llms.openai import AllMessageValues
from litellm.types.utils import ModelResponse, Usage

from ..common_utils import ModelResponseIterator as CohereModelResponseIterator
from ..common_utils import validate_environment as cohere_validate_environment

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
    temperature: Optional[float] = None
    max_tokens: Optional[int] = None
    api_key: Optional[str] = None

    def __init__(
        self,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        api_key: Optional[str] = None,
    ) -> None:
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key



    def get_supported_openai_params(self, model: str) -> List[str]:
        return [
            "stream",
            "temperature",
            "max_tokens",
            "top_p",
            "frequency_penalty",
            "presence_penalty",
            "stop",
            "n",
            "tools",
            "tool_choice",
            "seed",
            "extra_headers",
        ]
    def validate_environment(
        self,
        headers: dict,
        model: str,
        messages: List[AllMessageValues],
        optional_params: dict,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
    ) -> dict:
        return cohere_validate_environment(
            headers=headers,
            model=model,
            messages=messages,
            optional_params=optional_params,
            api_key=api_key,
        )
    def map_openai_params(
        self,
        non_default_params: dict,
        optional_params: dict,
        model: str,
        drop_params: bool,
    ) -> dict:
        for param, value in non_default_params.items():
            if param == "stream":
                optional_params["stream"] = value
            if param == "temperature":
                optional_params["temperature"] = value
            if param == "max_tokens":
                optional_params["max_tokens"] = value
            if param == "n":
                optional_params["num_generations"] = value
            if param == "top_p":
                optional_params["p"] = value
            if param == "frequency_penalty":
                optional_params["frequency_penalty"] = value
            if param == "presence_penalty":
                optional_params["presence_penalty"] = value
            if param == "stop":
                optional_params["stop_sequences"] = value
            if param == "tools":
                optional_params["tools"] = value
            if param == "seed":
                optional_params["seed"] = value
        return optional_params

    def transform_request(
        self,
        model: str,
        messages: List[AllMessageValues],
        optional_params: dict,
        litellm_params: dict,
        headers: dict,
    ) -> dict:
        # Prepare headers with the API key
        headers["Authorization"] = f"Bearer {self.api_key}"
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        # Transform the messages for EdenAI
        formatted_messages = [
            {"role": msg["role"], "content": [{"type": "text", "content": {"text": msg}}]}
            for msg in messages
        ]

        payload = {
            "providers": [model],
            "messages": formatted_messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens or 1000,
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_base_64": True,
            "show_original_response": False,
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

            # Handle tool calls if any (not common with EdenAI)
            tool_calls = provider_response.get("tool_calls", [])
            if tool_calls:
                model_response.choices[0].message.tool_calls = tool_calls

            # Handle token usage if available
            usage_data = provider_response.get("usage", {})
            prompt_tokens = usage_data.get("input_tokens", 0)
            completion_tokens = usage_data.get("output_tokens", 0)

            model_response.usage = Usage(
                prompt_tokens=prompt_tokens,
                completion_tokens=completion_tokens,
                total_tokens=prompt_tokens + completion_tokens,
            )
        except Exception as e:
            raise EdenAIError(status_code=raw_response.status_code, message=str(e))

        return model_response


    def get_error_class(
        self, error_message: str, status_code: int, headers: Union[dict, httpx.Headers]
    ) -> BaseLLMException:
        return EdenAIError(status_code=status_code, message=error_message, headers=headers)
