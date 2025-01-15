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
### Models that support Multimodal 
| Model Name       | Function Call                        |
|------------------|--------------------------------------|
|anthropic/claude-3-haiku-20240307 |	`completion(model="edenai/anthropic/claude-3-haiku-20240307", messages)`| 
|anthropic/claude-3-haiku-20240307-v1:0 |	`completion(model="edenai/anthropic/claude-3-haiku-20240307-v1:0", messages)`| 
|anthropic/claude-3-sonnet-20240229-v1:0	| `completion(model="edenai/anthropic/claude-3-sonnet-20240229-v1:0", messages)`| 
|anthropic/claude-3-5-sonnet-20240620-v1:0 |	`completion(model="edenai/anthropic/claude-3-5-sonnet-20240620-v1:0", messages)`| 
|anthropic/claude-3-opus-20240229 |	`completion(model="edenai/anthropic/claude-3-opus-20240229", messages)`| 
|anthropic/claude-3-sonnet-20240229 | `completion(model="edenai/anthropic/claude-3-sonnet-20240229", messages)`| 
|anthropic/claude-3-5-sonnet-20240620 |	`completion(model="edenai/anthropic/claude-3-5-sonnet-20240620", messages)`| 
|google/gemini-1.5-pro-exp-0801 |	`completion(model="edenai/google/gemini-1.5-pro-exp-0801", messages)`| 
|google/gemini-1.5-pro-exp-0827 |	`completion(model="edenai/google/gemini-1.5-pro-exp-0827", messages)`| 
|google/gemini-1.5-flash-exp-0801 |	`completion(model="edenai/google/gemini-1.5-flash-exp-0801", messages)`| 
|google/gemini-1.5-flash-exp-0827 |	`completion(model="edenai/google/gemini-1.5-flash-exp-0827", messages)`| 
|google/gemini-1.5-flash |	`completion(model="edenai/google/gemini-1.5-flash", messages)`| 
|google/gemini-1.5-pro |	`completion(model="edenai/google/gemini-1.5-pro", messages)`| 
|google/gemini-1.5-flash-latest |	`completion(model="edenai/google/gemini-1.5-flash-latest", messages)`| 
|google/gemini-pro |	`completion(model="edenai/google/gemini-pro", messages)`| 
|google/gemini-1.5-pro-latest |	`completion(model="edenai/google/gemini-1.5-pro-latest", messages)`| 
|google/gemini-pro-vision |	`completion(model="edenai/google/gemini-pro-vision", messages)`| 
|openai/gpt-4-vision-preview | `completion(model="edenai/openai/gpt-4-vision-preview", messages)`| 
|openai/gpt-4 |	`completion(model="edenai/openai/gpt-4", messages)`| 
|openai/gpt-4o |	`completion(model="edenai/openai/gpt-4o", messages)`| 
|openai/gpt-4-turbo |	`completion(model="edenai/openai/gpt-4-turbo", messages)`| 
|openai/gpt-4o-mini |	`completion(model="edenai/openai/gpt-4o-mini", messages)`| 
|openai/gpt-4o-2024-05-13 |	`completion(model="edenai/openai/gpt-4o-2024-05-13", messages)`| 
|openai/gpt-4o-mini-2024-07-18 |	`completion(model="edenai/openai/gpt-4o-mini-2024-07-18", messages)`| 

### Models that support ToolCalls 

| Model Name       | Function Call                        |
|------------------|--------------------------------------|
|openai/gpt-3.5-turbo-1106 | `completion(model="edenai/openai/gpt-3.5-turbo-1106", messages)`|
|openai/gpt-3.5-turbo-16k | `completion(model="edenai/openai/gpt-3.5-turbo-16k", messages)`|
|openai/gpt-4-turbo-2024-04-09 |	`completion(model="edenai/openai/gpt-4-turbo-2024-04-09", messages)`|
|openai/gpt-4o |	`completion(model="edenai/openai/gpt-4o", messages)`|
|openai/gpt-4-1106-preview |	`completion(model="edenai/openai/gpt-4-1106-preview", messages)`|
|openai/gpt-4-vision-preview |	`completion(model="edenai/openai/gpt-4-vision-preview", messages)`|
|openai/gpt-3.5-turbo-0125 |	`completion(model="edenai/openai/gpt-3.5-turbo-0125", messages)`|
|openai/gpt-4-32k- |	`completion(model="edenai/openai/gpt-4-32k-0314", messages)`|
|openai/gpt-4o-mini	 | `completion(model="edenai/openai/gpt-4o-mini", messages)`|
|openai/gpt-4-0314	 | `completion(model="edenai/openai/gpt-4-0314", messages)`|
|openai/gpt-4	| `completion(model="edenai/openai/gpt-4", messages)`|
|openai/gpt-3.5-turbo| `completion(model="edenai/openai/gpt-3.5-turbo", messages)`|
|openai/o1-|	`completion(model="edenai/openai/o1-preview", messages)`|
|openai/o1-preview-2024-09-12	|`completion(model="edenai/openai/o1-preview-2024-09-12", messages)`|
|openai/o1-mini|	`completion(model="edenai/openai/o1-mini", messages)`|
|openai/o1-mini-2024-09-12|	`completion(model="edenai/openai/o1-mini-2024-09-12", messages)`|
|openai/gpt-4o-2024-05-|	`completion(model="edenai/openai/gpt-4o-2024-05-13", messages)`|
|google/chat-bison|	`completion(model="edenai/google/chat-bison", messages)`|
|google/gemini-1.5-flash	|`completion(model="edenai/google/gemini-1.5-flash", messages)`|
|google/gemini-1.5-pro	|`completion(model="edenai/google/gemini-1.5-pro", messages)`|
|cohere/command-light	|`completion(model="edenai/cohere/command-light", messages)`|
|cohere/command-nightly	|`completion(model="edenai/cohere/command-nightly", messages)`|
|cohere/command|	`completion(model="edenai/cohere/command", messages)`|
|cohere/command-light-|	`completion(model="edenai/cohere/command-light-nightly", messages)`|
|cohere/command-r|	`completion(model="edenai/cohere/command-r", messages)`|
|cohere/command-r-plus|	`completion(model="edenai/cohere/command-r-plus", messages)`|
|meta/llama3-1-405b-instruct-v1:0	|`completion(model="edenai/meta/llama3-1-405b-instruct-v1:0", messages)`|
|meta/llama3-1-70b-instruct-v1:0	|`completion(model="edenai/meta/llama3-1-70b-instruct-v1:0", messages)`|
|meta/llama3-1-8b-instruct-v1:|	`completion(model="edenai/meta/llama3-1-8b-instruct-v1:0", messages)`|
|meta/llama3-70b-instruct-v1:0	|`completion(model="edenai/meta/llama3-70b-instruct-v1:0", messages)`|
|meta/llama3-8b-instruct-v1:0	|`completion(model="edenai/meta/llama3-8b-instruct-v1:0", messages)`|
|mistral/small|	`completion(model="edenai/mistral/small", messages)`|
|mistral/medium	|`completion(model="edenai/mistral/medium", messages)`|
|mistral/tiny|	`completion(model="edenai/mistral/tiny", messages)`|
|mistral/large-|	`completion(model="edenai/mistral/large-latest", messages)`|
|mistral/ministral-3b-latest|	`completion(model="edenai/mistral/ministral-3b-latest", messages)`|
|mistral/ministral-8b-latest|	`completion(model="edenai/mistral/ministral-8b-latest", messages)`|
|mistral/mistral-large-2407	|`completion(model="edenai/mistral/mistral-large-2407", messages)`|
|mistral/mistral-small-2409	|`completion(model="edenai/mistral/mistral-small-2409", messages)`|
|perplexityai/llama-3.1-sonar-huge-128k-online|	`completion(model="edenai/perplexityai/llama-3.1-sonar-huge-128k-online", messages)`|
|perplexityai/llama-3.1-sonar-small-128k-chat|	`completion(model="edenai/perplexityai/llama-3.1-sonar-small-128k-chat", messages)`|
|perplexityai/llama-3.1-sonar-small-128k-online	|`completion(model="edenai/perplexityai/llama-3.1-sonar-small-128k-online", messages)`|
|perplexityai/llama-3.1-8b-instruct	|`completion(model="edenai/perplexityai/llama-3.1-8b-instruct", messages)`|
|perplexityai/llama-3.1-70b-instruct|	`completion(model="edenai/perplexityai/llama-3.1-70b-instruct", messages)`|
|perplexityai/llama-3.1-sonar-large-128k-chat|	`completion(model="edenai/perplexityai/llama-3.1-sonar-large-128k-chat", messages)`|
|perplexityai/llama-3.1-sonar-large-128k-online|`completion(model="edenai/perplexityai/llama-3.1-sonar-large-128k-online", messages)`|
|anthropic/claude-3-sonnet-20240229-v1:0	|`completion(model="edenai/anthropic/claude-3-sonnet-20240229-v1:0", messages)`|
|anthropic/claude-instant-v1|	`completion(model="edenai/anthropic/claude-instant-v1", messages)`|
|anthropic/claude-v2|`completion(model="edenai/anthropic/claude-v2", messages)`|
|anthropic/claude-3-haiku-20240307-v1:|	`completion(model="edenai/anthropic/claude-3-haiku-20240307-v1:0", messages)`|
|anthropic/claude-3-5-sonnet-20240620-v1:0	|`completion(model="edenai/anthropic/claude-3-5-sonnet-20240620-v1:0", messages)`|