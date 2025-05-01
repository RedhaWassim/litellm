# EdenAI
https://edenai.co

:::tip

**We support ALL EdenAI models, just set `model=edenai/<any-model-on-edenai>` as a prefix when sending litellm requests**

:::


## API Key
```python
# env variable
os.environ['EDENAI_API_KEY']
```

## Sample Usage
```python
from litellm import completion
import os

os.environ['EDENAI_API_KEY'] = ""
response = completion(
    model="edenai/openai/gpt-4o", 
    messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
)
```

## Sample Usage - Multimodal
```python
from litellm import completion
import os

os.environ['EDENAI_API_KEY'] = ""
response = completion(
    model="edenai/google/gemini-1.5-flash",
    messages=[
    {
        "role": "user",
        "content": """[
            {
                "type": "text",
                "content": {
                    "text": "is there a lizard in the image?"
                }
            },
            {
                "type": "media_url",
                "content": {
                    "media_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS53fbiM_1J_a_gPfGctjxQUWRxhj3-l8ueSw&s",
                    "media_type": "image/jpeg"
                }
            }
        ]"""
    }
],
)

```

## Chat Models
| Model Name       | Function Call                        |
|------------------|--------------------------------------|
|amazon/eu.amazon.nova-lite-v1:0|`completion(model="edenai/amazon/eu.amazon.nova-lite-v1:0", messages)`|
|amazon/amazon.nova-lite-v1:0|`completion(model="edenai/amazon/amazon.nova-lite-v1:0", messages)`|
|amazon/amazon.nova-micro-v1:0|`completion(model="edenai/amazon/amazon.nova-micro-v1:0", messages)`|
|amazon/amazon.nova-pro-v1:0|`completion(model="edenai/amazon/amazon.nova-pro-v1:0", messages)`|
|anthropic/claude-3-5-sonnet-latest|`completion(model="edenai/anthropic/claude-3-5-sonnet-latest", messages)`|
|anthropic/claude-3-5-haiku-latest|`completion(model="edenai/anthropic/claude-3-5-haiku-latest", messages)`|
|anthropic/claude-3-opus-latest|`completion(model="edenai/anthropic/claude-3-opus-latest", messages)`|
|anthropic/claude-3-7-sonnet-latest|`completion(model="edenai/anthropic/claude-3-7-sonnet-latest", messages)`|
|cohere/command-r7b-12-2024|`completion(model="edenai/cohere/command-r7b-12-2024", messages)`|
|cohere/command-r-plus-08-2024|`completion(model="edenai/cohere/command-r-plus-08-2024", messages)`|
|cohere/command-r-plus|`completion(model="edenai/cohere/command-r-plus", messages)`|
|cohere/command-r-08-2024|`completion(model="edenai/cohere/command-r-08-2024", messages)`|
|cohere/command-r-03-2024|`completion(model="edenai/cohere/command-r-03-2024", messages)`|
|cohere/command-r|`completion(model="edenai/cohere/command-r", messages)`|
|cohere/command|`completion(model="edenai/cohere/command", messages)`|
|cohere/command-light|`completion(model="edenai/cohere/command-light", messages)`|
|deepseek/deepseek-chat|`completion(model="edenai/deepseek/deepseek-chat", messages)`|
|deepseek/deepseek-reasoner|`completion(model="edenai/deepseek/deepseek-reasoner", messages)`|
|meta/meta.llama3-1-405b-instruct-v1:0|`completion(model="edenai/meta/meta.llama3-1-405b-instruct-v1:0", messages)`|
|meta/meta.llama3-1-70b-instruct-v1:0|`completion(model="edenai/meta/meta.llama3-1-70b-instruct-v1:0", messages)`|
|meta/meta.llama3-1-8b-instruct-v1:0|`completion(model="edenai/meta/meta.llama3-1-8b-instruct-v1:0", messages)`|
|mistral/pixtral-large-latest|`completion(model="edenai/mistral/pixtral-large-latest", messages)`|
|mistral/mistral-small-latest|`completion(model="edenai/mistral/mistral-small-latest", messages)`|
|mistral/codestral-latest|`completion(model="edenai/mistral/codestral-latest", messages)`|
|mistral/mistral-large-latest|`completion(model="edenai/mistral/mistral-large-latest", messages)`|
|openai/gpt-4.1-2025-04-14|`completion(model="edenai/openai/gpt-4.1-2025-04-14", messages)`|
|openai/gpt-4.1-mini-2025-04-14|`completion(model="edenai/openai/gpt-4.1-mini-2025-04-14", messages)`|
|openai/gpt-4.1-nano-2025-04-14|`completion(model="edenai/openai/gpt-4.1-nano-2025-04-14", messages)`|
|openai/o3-2025-04-16|`completion(model="edenai/openai/o3-2025-04-16", messages)`|
|openai/o4-mini-2025-04-16|`completion(model="edenai/openai/o4-mini-2025-04-16", messages)`|
|openai/gpt-4|`completion(model="edenai/openai/gpt-4", messages)`|
|openai/gpt-4o|`completion(model="edenai/openai/gpt-4o", messages)`|
|openai/gpt-4o-mini|`completion(model="edenai/openai/gpt-4o-mini", messages)`|
|openai/o1-preview|`completion(model="edenai/openai/o1-preview", messages)`|
|openai/o1-mini|`completion(model="edenai/openai/o1-mini", messages)`|
|openai/gpt-4o-2024-05-13|`completion(model="edenai/openai/gpt-4o-2024-05-13", messages)`|
|openai/gpt-4-turbo|`completion(model="edenai/openai/gpt-4-turbo", messages)`|
|openai/o1-2024-12-17|`completion(model="edenai/openai/o1-2024-12-17", messages)`|
|openai/o1|`completion(model="edenai/openai/o1", messages)`|
|openai/o3-mini|`completion(model="edenai/openai/o3-mini", messages)`|
|openai/gpt-4.5-preview-2025-02-27|`completion(model="edenai/openai/gpt-4.5-preview-2025-02-27", messages)`|
|openai/o1-mini-2024-09-12|`completion(model="edenai/openai/o1-mini-2024-09-12", messages)`|
|openai/o3-mini-2025-01-31|`completion(model="edenai/openai/o3-mini-2025-01-31", messages)`|
|openai/gpt-4o-2024-08-06|`completion(model="edenai/openai/gpt-4o-2024-08-06", messages)`|
|openai/gpt-4o-mini-2024-07-18|`completion(model="edenai/openai/gpt-4o-mini-2024-07-18", messages)`|
|openai/gpt-3.5-turbo|`completion(model="edenai/openai/gpt-3.5-turbo", messages)`|
|together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo|`completion(model="edenai/together_ai/Qwen/Qwen2.5-72B-Instruct-Turbo", messages)`|
|together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo|`completion(model="edenai/together_ai/meta-llama/Llama-3.3-70B-Instruct-Turbo", messages)`|
|together_ai/microsoft/WizardLM-2-8x22B|`completion(model="edenai/together_ai/microsoft/WizardLM-2-8x22B", messages)`|
|xai/grok-2-latest|`completion(model="edenai/xai/grok-2-latest", messages)`|
|xai/grok-2|`completion(model="edenai/xai/grok-2", messages)`|
|xai/grok-2-vision-1212|`completion(model="edenai/xai/grok-2-vision-1212", messages)`|
|google/gemini-2.5-pro-preview-03-25|`completion(model="edenai/google/gemini-2.5-pro-preview-03-25", messages)`|
|google/gemini-2.5-flash-preview-04-17|`completion(model="edenai/google/gemini-2.5-flash-preview-04-17", messages)`|
|google/gemini-2.0-flash-lite|`completion(model="edenai/google/gemini-2.0-flash-lite", messages)`|
|google/gemini-1.5-flash|`completion(model="edenai/google/gemini-1.5-flash", messages)`|
|google/gemini-1.5-pro|`completion(model="edenai/google/gemini-1.5-pro", messages)`|
|google/gemini-1.5-flash-latest|`completion(model="edenai/google/gemini-1.5-flash-latest", messages)`|
|google/gemini-1.5-pro-latest|`completion(model="edenai/google/gemini-1.5-pro-latest", messages)`|
|google/gemini-1.5-flash-8b|`completion(model="edenai/google/gemini-1.5-flash-8b", messages)`|
|google/gemini-1.5-flash-8b-latest|`completion(model="edenai/google/gemini-1.5-flash-8b-latest", messages)`|
|google/gemini-2.0-flash|`completion(model="edenai/google/gemini-2.0-flash", messages)`|
|google/gemini-2.5-pro-exp-03-25|`completion(model="edenai/google/gemini-2.5-pro-exp-03-25", messages)`|
|google/gemini-2.0-flash-lite-preview-02-05|`completion(model="edenai/google/gemini-2.0-flash-lite-preview-02-05", messages)`|
|groq/llama-3.1-8b-instant|`completion(model="edenai/groq/llama-3.1-8b-instant", messages)`|
|groq/llama3-70b-8192|`completion(model="edenai/groq/llama3-70b-8192", messages)`|
|groq/llama3-8b-8192|`completion(model="edenai/groq/llama3-8b-8192", messages)`|
|groq/gemma2-9b-it|`completion(model="edenai/groq/gemma2-9b-it", messages)`|
|groq/llama-3.3-70b-versatile|`completion(model="edenai/groq/llama-3.3-70b-versatile", messages)`|
|microsoft/gpt-4o|`completion(model="edenai/microsoft/gpt-4o", messages)`|
|microsoft/o3-mini|`completion(model="edenai/microsoft/o3-mini", messages)`|
|microsoft/o1-mini|`completion(model="edenai/microsoft/o1-mini", messages)`|
|microsoft/gpt-4o-mini|`completion(model="edenai/microsoft/gpt-4o-mini", messages)`|
|microsoft/gpt-4|`completion(model="edenai/microsoft/gpt-4", messages)`|
|microsoft/gpt-35-turbo-16k|`completion(model="edenai/microsoft/gpt-35-turbo-16k", messages)`|
|microsoft/gpt-35-turbo|`completion(model="edenai/microsoft/gpt-35-turbo", messages)`|
