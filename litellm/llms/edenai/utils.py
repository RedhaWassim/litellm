from typing import List, Optional
from litellm.types.llms.openai import AllMessageValues


def validate_environment(
    headers: dict,
    model: str,
    messages: List[AllMessageValues],
    optional_params: dict,
    api_key: Optional[str] = None,
) -> dict:
    """
    Return headers to use for edenai chat completion request

    EdenAI API Ref: https://docs.edenai.co/reference/multimodal_multimodal_chat_create

    Expected headers:
    {
        "Request-Source": "unspecified:litellm",
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "bearer $CO_API_KEY"
    }
    """
    headers.update({"accept": "application/json", "content-type": "application/json"})

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers
