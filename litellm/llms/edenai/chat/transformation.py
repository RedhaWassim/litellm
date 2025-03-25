from typing import List, Literal, Optional, Tuple, Union, cast, Dict, Any, TYPE_CHECKING
import litellm
from litellm.secret_managers.main import get_secret_str
from litellm.types.llms.openai import AllMessageValues, ChatCompletionImageObject
from litellm.types.utils import ModelInfoBase, ProviderSpecificModelInfo
from litellm.llms.base_llm.chat.transformation import BaseConfig, BaseLLMException
from litellm.types.utils import ModelResponse, Usage

import httpx
import json
import time
from ..utils import validate_environment as edenai_validate_environment
import uuid

if TYPE_CHECKING:
    from litellm.litellm_core_utils.litellm_logging import Logging as _LiteLLMLoggingObj

    LiteLLMLoggingObj = _LiteLLMLoggingObj
else:
    LiteLLMLoggingObj = Any


class EdenAIError(BaseLLMException):
    def __init__(
        self, status_code: int, message: str, headers: Optional[httpx.Headers] = None
    ):
        self.status_code = status_code
        self.message = message
        self.request = httpx.Request(
            method="POST", url="https://api.edenai.run/v2/llm/chat"
        )
        self.response = httpx.Response(status_code=status_code, request=self.request)
        super().__init__(status_code=status_code, message=message, headers=headers)


class EdenAIChatConfig(BaseConfig):
    """
    Reference: https://docs.edenai.co/reference/llm_llm_chat_create
    Configuration for EdenAI's Multimodal Chat API
    """

    # Standard parameters
    temperature: Optional[float] = None
    max_completion_tokens: Optional[int] = None
    top_p: Optional[float] = None
    frequency_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    n: Optional[int] = None
    stop: Optional[List[str]] = None
    logprobs: Optional[bool] = None
    top_logprobs: Optional[int] = None
    seed: Optional[int] = None
    tools: Optional[List[dict]] = None
    tool_choice: Optional[str] = None
    user: Optional[str] = None

    # EdenAI specific parameters
    reasoning_effort: Optional[Literal["low", "medium", "high"]] = None
    service_tier: Optional[Literal["auto", "default"]] = "default"
    modalities: Optional[List[str]] = None
    prediction: Optional[dict] = None
    metadata: Optional[List[dict]] = None

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

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

    @classmethod
    def get_config(cls):
        return super().get_config()

    def get_supported_openai_params(self, model: str) -> List[str]:
        return [
            "temperature",
            "max_completion_tokens",
            "top_p",
            "frequency_penalty",
            "presence_penalty",
            "n",
            "stop",
            "logprobs",
            "top_logprobs",
            "seed",
            "tools",
            "tool_choice",
            "user",
            "response_format",
        ]

    def map_openai_params(
        self,
        non_default_params: dict,
        optional_params: dict,
        model: str,
        drop_params: bool,
    ) -> dict:
        param_mapping = {
            "max_tokens": "max_completion_tokens",
        }

        for param, value in non_default_params.items():
            if param in param_mapping:
                optional_params[param_mapping[param]] = value
            elif param in self.get_supported_openai_params(model):
                optional_params[param] = value

        return optional_params

    def transform_request(
        self,
        model: str,
        messages: List[AllMessageValues],
        optional_params: dict,
        litellm_params: dict,
        headers: dict,
    ) -> dict:
        # Build the request payload
        payload = {
            "model": model,
            "messages": messages,
            "providers": [model],
            **optional_params,
        }

        return payload

    def transform_response(
        self,
        model: str,
        raw_response: httpx.Response,
        model_response: ModelResponse,
        logging_obj: Any,
        request_data: dict,
        messages: List[AllMessageValues],
        optional_params: dict,
        litellm_params: dict,
        encoding: Any,
        api_key: Optional[str] = None,
        json_mode: Optional[bool] = None,
    ) -> ModelResponse:
        response_json = raw_response.json()
        model_response = ModelResponse(**response_json)
        return model_response

    def get_error_class(
        self, error_message: str, status_code: int, headers: Union[dict, httpx.Headers]
    ) -> BaseLLMException:
        return EdenAIError(status_code=status_code, message=error_message)
