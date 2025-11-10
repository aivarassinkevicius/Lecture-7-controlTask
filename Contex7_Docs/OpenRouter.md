### Installing OpenRouter Client for Development - pip - Bash

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This command installs the OpenRouter Python client along with additional development dependencies. These extra tools are useful for contributors or those needing advanced features like testing utilities or specific linters.

```bash
pip install openrouter-client-unofficial[dev]
```

--------------------------------

### Installing OpenRouter Client - pip - Bash

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This command installs the core OpenRouter Python client library using pip, the standard Python package installer. It's the first step to integrate the client into your Python project, making its functionalities available for use.

```bash
pip install openrouter-client-unofficial
```

--------------------------------

### Installing OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This command installs the `openrouter-client-unofficial` package using pip, which is the official Python client for OpenRouter. It's a prerequisite for running any of the provided examples.

```bash
pip install openrouter-client-unofficial
```

--------------------------------

### Running a Specific OpenRouter Python Example

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This command executes a single Python example file, `basic_chat.py`, demonstrating how to run any of the provided examples. Replace `basic_chat.py` with the desired example file name.

```bash
python basic_chat.py
```

--------------------------------

### Creating a Chat Completion - OpenRouter Client - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This example demonstrates how to make a basic chat completion request using the OpenRouter client. It initializes the client, specifies a model and a list of messages, then prints the content of the AI's response, showcasing a fundamental interaction with the API.

```python
from openrouter_client import OpenRouterClient

# Initialize the client
client = OpenRouterClient(api_key="your-api-key")

# Create a chat completion
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

# Print the response
print(response.choices[0].message.content)
```

--------------------------------

### Initializing OpenRouter Client with API Key - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This snippet demonstrates how to initialize the OpenRouter client by directly passing your API key. The OpenRouterClient class requires an api_key parameter to authenticate requests against the OpenRouter API, enabling access to its services.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key-here")
```

--------------------------------

### Listing and Retrieving Model Information - OpenRouter Client - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This snippet illustrates how to interact with the OpenRouter client's model API to retrieve information. It first lists all available models, printing their IDs and names, then demonstrates fetching detailed information for a specific model, including its context length and pricing.

```python
# Get all available models
models = client.models.list()
for model in models.data:
    print(f"{model.id}: {model.name}")

# Get specific model information
model_info = client.models.get("anthropic/claude-3-opus")
print(f"Context length: {model_info.context_length}")
print(f"Price per token: {model_info.pricing}")
```

--------------------------------

### Customizing OpenRouter Python Examples

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This Python snippet illustrates how to enable additional demonstration functions within the example files. By uncommenting lines like `demonstrate_advanced_feature()` or `demonstrate_error_cases()` within the `if __name__ == "__main__":` block, users can explore more features beyond the default `main()` execution.

```python
if __name__ == "__main__":
    main()
    # Uncomment to run additional examples
    # demonstrate_advanced_feature()
    # demonstrate_error_cases()
```

--------------------------------

### Running Multiple OpenRouter Python Examples

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This bash script iterates through a list of specified Python example files (`basic_chat.py`, `streaming_chat.py`, `function_calling.py`) and executes each one sequentially. It prints the name of the file being run before execution and a separator after each run.

```bash
for file in basic_chat.py streaming_chat.py function_calling.py; do
    echo "Running $file..."
    python "$file"
    echo "---"
done
```

--------------------------------

### Developing a Production-Ready Service with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This snippet advises combining all examples, specifically leveraging `error_handling.py` for robustness, `advanced_usage.py` for scalability, and `credits_and_usage.py` for monitoring, to build a production-grade service. This comprehensive approach ensures the service is reliable, performs well under load, and allows for effective resource tracking.

```python
# Combine all examples focusing on:
# - error_handling.py for robustness
# - advanced_usage.py for scalability
# - credits_and_usage.py for monitoring
```

--------------------------------

### Using OpenRouter Client as Context Manager - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This example demonstrates using the OpenRouter client as a context manager (with statement) for automatic resource management. This pattern ensures that client resources, such as network connections, are properly closed and cleaned up automatically upon exiting the with block, preventing resource leaks.

```python
with OpenRouterClient(api_key="your-api-key") as client:
    response = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
# Client resources are automatically cleaned up here
```

--------------------------------

### Creating a Tool-Enabled Assistant with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This snippet suggests combining `function_calling.py`, `error_handling.py`, and `advanced_usage.py` to develop an intelligent assistant capable of invoking external functions and APIs while handling errors gracefully. This setup allows the assistant to interact with external systems and perform complex tasks.

```python
# Combine function_calling.py + error_handling.py + advanced_usage.py
# For an assistant that can call external functions and APIs
```

--------------------------------

### Installing OpenRouter Python Client for Development - Bash

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/index.md

This command installs the unofficial OpenRouter Python client along with its development dependencies. This is useful for contributors or users who need to run tests or work on the library's source code.

```bash
pip install openrouter-client-unofficial[dev]
```

--------------------------------

### Initializing OpenRouter Client from Environment Variable - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This Python code initializes the OpenRouter client without explicitly providing an API key. The client automatically detects and uses the OPENROUTER_API_KEY environment variable if it's set, simplifying authentication and improving security by avoiding hardcoded credentials.

```python
client = OpenRouterClient()  # Will automatically use OPENROUTER_API_KEY
```

--------------------------------

### Basic Chat Completion with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet demonstrates how to perform a simple chat completion using the OpenRouter Python client. It initializes the client with an API key and sends a system and user message to a specified model to get a direct response.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)
```

--------------------------------

### Running OpenRouter Python Example with Debug Logging

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This command runs a specific Python example, `function_calling.py`, with debug logging enabled by setting the `OPENROUTER_LOG_LEVEL` environment variable to `DEBUG`. This is useful for detailed troubleshooting and understanding client behavior.

```bash
OPENROUTER_LOG_LEVEL=DEBUG python function_calling.py
```

--------------------------------

### Streaming Chat Completion with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet shows how to get real-time streaming responses from the OpenRouter API. It sets `stream=True` in the `chat.create` call and iterates over the response chunks to print content as it arrives, providing a dynamic user experience.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

stream = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Tell me a long story about space exploration"}],
    stream=True
)

print("Assistant: ", end="")
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # New line at the end
```

--------------------------------

### Setting OpenRouter API Key via Environment Variable

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This command sets the `OPENROUTER_API_KEY` environment variable, which is the recommended method for providing your OpenRouter API key to the client. Replace "your-api-key-here" with your actual API key.

```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

--------------------------------

### Setting OpenRouter API Key as Environment Variable - Bash

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This Bash command sets the OPENROUTER_API_KEY environment variable. This method is recommended for securely managing API keys, preventing them from being hardcoded directly into your source code and making them accessible to the OpenRouter client automatically.

```bash
export OPENROUTER_API_KEY="your-api-key-here"
```

--------------------------------

### Retrieving Model Information and Pricing with OpenRouter Client in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet shows how to list available models and retrieve detailed information for a specific model using the `client.models.list()` and `client.models.get()` methods. It demonstrates accessing properties like context length, pricing, and description for a chosen model.

```Python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

# List all models
models = client.models.list()
print("Available models:")
for model in models.data[:5]:  # Show first 5 models
    print(f"- {model.id}: {model.name}")

# Get specific model info
model_info = client.models.get("anthropic/claude-3-opus")
print(f"\nClaude 3 Opus details:")
print(f"Context length: {model_info.context_length}")
print(f"Pricing: {model_info.pricing}")
print(f"Description: {model_info.description}")
```

--------------------------------

### Generating Text Completions with OpenRouter Client in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet demonstrates how to use the `client.completions.create` method to generate text completions from a given prompt. It specifies the model, prompt, maximum tokens, and temperature to control the output, then prints the generated text.

```Python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

response = client.completions.create(
    model="openai/gpt-3.5-turbo-instruct",
    prompt="The benefits of renewable energy include",
    max_tokens=150,
    temperature=0.7
)

print(response.choices[0].text)
```

--------------------------------

### Streaming Chat Completion Responses - OpenRouter Client - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This code demonstrates how to enable and process streaming responses from the OpenRouter chat API. By setting stream=True, the client yields chunks of the response as they become available, allowing for real-time display of generated content, which is useful for long-running generations.

```python
stream = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

--------------------------------

### Installing OpenRouter Python Client - Bash

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/index.md

This command installs the unofficial OpenRouter Python client library using pip. It is the standard way to add the library to your Python environment, making its functionalities available for use in your projects.

```bash
pip install openrouter-client-unofficial
```

--------------------------------

### Installing the OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This snippet provides the command to install the unofficial OpenRouter Python client using pip, the standard package installer for Python.

```bash
pip install openrouter-client-unofficial
```

--------------------------------

### Handling OpenRouter API Exceptions - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/getting-started.md

This snippet illustrates robust error handling for OpenRouter API calls using specific exception types. It demonstrates catching AuthenticationError, RateLimitError, ValidationError, and a general OpenRouterError to provide tailored feedback for common API issues, ensuring graceful application behavior.

```python
from openrouter_client import OpenRouterClient
from openrouter_client.exceptions import (
    OpenRouterError,
    AuthenticationError,
    RateLimitError,
    ValidationError
)

client = OpenRouterClient(api_key="your-api-key")

try:
    response = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": "Hello!"}]
    )
except AuthenticationError:
    print("Invalid API key")
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}")
except ValidationError as e:
    print(f"Invalid request: {e}")
except OpenRouterError as e:
    print(f"API error: {e}")
```

--------------------------------

### Implementing Cost-Optimized Processing with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This snippet describes how to integrate `prompt_caching.py`, `credits_and_usage.py`, and `model_management.py` to achieve cost-effective batch processing, including prompt caching for efficiency and monitoring for usage and credits. This combination is ideal for applications where cost control and resource management are critical.

```python
# Combine prompt_caching.py + credits_and_usage.py + model_management.py
# For cost-effective batch processing with monitoring
```

--------------------------------

### Monitoring Credit Usage with OpenRouter Client in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet demonstrates how to check the current credit balance and total usage for your OpenRouter account using the `client.credits.get()` method. It provides a way to monitor API consumption and manage costs.

```Python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

# Check credit balance
credits = client.credits.get()
print(f"Current balance: ${credits.data.credits}")
print(f"Total usage: ${credits.data.usage}")
```

--------------------------------

### Multi-turn Conversation with Manual Function Definition in OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet begins to set up a multi-turn conversation with function calling, demonstrating how to manually define tool schemas using `build_tool_definition` and `build_parameter_schema` for more complex scenarios. It includes a mock `search_database` function to illustrate tool implementation.

```python
from openrouter_client import OpenRouterClient
from openrouter_client.tools import (
    build_tool_definition,
    build_parameter_schema
)
from openrouter_client.models 대비 ()
    StringParameter,
    NumberParameter,
    FunctionCall,
    ChatCompletionTool
)
import json

def search_database(query: str, category: str = "all") -> dict:
    """Mock database search function."""
    return {
        "query": query,
        "category": category,
        "results": [
            {"title": f"Result 1 for {query}", "score": 0.95},
            {"title": f"Result 2 for {query}", "score": 0.87}
        ]
    }
```

--------------------------------

### Implementing Tool Calling with OpenRouter Chat API in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet demonstrates how to define a tool, integrate it with the OpenRouter chat API, and handle tool calls within a conversation flow. It shows how to pass tool definitions to the `client.chat.create` method and process the `tool_calls` returned by the assistant, including parsing arguments and adding tool responses back to the message history.

```Python
def search_database_func(query: str, category: str = "all") -> dict:
    """Search for information in the database.
    
    Args:
        query: Search query
        category: Search category (all, books, or articles)
    """
    pass

search_tool = build_tool_definition(search_database_func)

client = OpenRouterClient(api_key="your-api-key")

def conversation():
    messages = [
        {"role": "system", "content": "You are a helpful search assistant."}
    ]
    
    # First user message
    user_input = "Find information about machine learning"
    print(f"User: {user_input}")
    messages.append({"role": "user", "content": user_input})
    
    # Get assistant response
    response = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=messages,
        tools=[search_tool]
    )
    
    assistant_message = response.choices[0].message
    messages.append(assistant_message.dict())
    
    # Handle tool calls
    if assistant_message.tool_calls:
        print("Assistant is searching...")
        
        for tool_call in assistant_message.tool_calls:
            # Execute the tool (parse arguments manually)
            import json
            args = json.loads(tool_call.function.arguments)
            result = search_database(**args)
            
            # Add tool response to conversation
            tool_response = {
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id
            }
            messages.append(tool_response)
            
            print(f"Search results: {json.dumps(result, indent=2)}")
        
        # Get final response with tool results
        final_response = client.chat.create(
            model="anthropic/claude-3-opus",
            messages=messages
        )
        print(f"Assistant: {final_response.choices[0].message.content}")
    else:
        print(f"Assistant: {assistant_message.content}")

conversation()
```

--------------------------------

### Initializing OpenRouter Client and Performing Chat Completion in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This example demonstrates how to initialize the OpenRouter client with an API key and perform a basic chat completion request. It shows how to define system and user messages and print the model's response.

```python
from openrouter_client import OpenRouterClient

# Initialize the client
client = OpenRouterClient(
    api_key="your-api-key",  # Or set OPENROUTER_API_KEY environment variable
)

# Chat completion example
response = client.chat.create(
    model="anthropic/claude-3-opus",  # Or any other model on OpenRouter
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about OpenRouter."}
    ]
)

print(response.choices[0].message.content)
```

--------------------------------

### Function Calling with @tool Decorator in OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This example illustrates using the `@tool` decorator to define a callable function (`get_weather`) that the model can invoke. It demonstrates how to pass tool definitions to the `chat.create` method and process the `tool_calls` from the model's response to execute the appropriate function.

```python
from openrouter_client import OpenRouterClient, tool
import requests

@tool
def get_weather(location: str, unit: str = "celsius") -> dict:
    """Get current weather for a location.
    
    Args:
        location: The city and state/country
        unit: Temperature unit (celsius or fahrenheit)
    """
    # Mock implementation - replace with real weather API
    return {
        "location": location,
        "temperature": 22,
        "unit": unit,
        "condition": "Sunny",
        "humidity": 65
    }

client = OpenRouterClient(api_key="your-api-key")

response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "What's the weather like in Paris?"}],
    tools=[get_weather.to_dict()],
    tool_choice="auto"
)

# Process tool calls
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        if tool_call.function.name == "get_weather":
            result = get_weather.execute(tool_call.function.arguments)
            print(f"Weather result: {result}")
else:
    print(response.choices[0].message.content)
```

--------------------------------

### Building a Robust Chat Application with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples/README.md

This snippet outlines the combination of `basic_chat.py`, `streaming_chat.py`, and `error_handling.py` to create a comprehensive chat application that supports real-time responses and robust error management. It focuses on providing a smooth user experience with reliable handling of potential issues.

```python
# Combine basic_chat.py + streaming_chat.py + error_handling.py
# For a robust chat application with real-time responses
```

--------------------------------

### Calculating Rate Limits and Monitoring API Usage - OpenRouter Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet demonstrates how to retrieve current rate limits (requests and tokens per minute) using client.calculate_rate_limits(). It then shows how to make a chat request and subsequently check the updated credit balance to determine the cost of the API call. This helps in managing API consumption and understanding billing.

```Python
# Calculate rate limits based on credits
rate_limits = client.calculate_rate_limits()
print(f"Requests per minute: {rate_limits['requests_per_minute']}")
print(f"Tokens per minute: {rate_limits['tokens_per_minute']}")

# Make a request and monitor usage
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Hello!"}]
)

# Check updated balance
updated_credits = client.credits.get()
cost = credits.data.credits - updated_credits.data.credits
print(f"Request cost: ${cost:.6f}")
```

--------------------------------

### Calculating OpenRouter Rate Limits in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This example demonstrates how to programmatically calculate recommended rate limits based on available credits using the client's `calculate_rate_limits` method. This helps in dynamically adjusting API call frequency.

```python
# Calculate rate limits based on available credits
rate_limits = client.calculate_rate_limits()
print(f"Recommended: {rate_limits['requests']} requests per {rate_limits['period']} seconds")
```

--------------------------------

### Defining Tool Functions with @tool Decorator in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This example demonstrates how to define a tool function for OpenRouter's function calling feature using the `@tool` decorator. It includes type hints for parameters and a docstring for description, which are used by the model to understand and invoke the tool.

```python
from openrouter_client import OpenRouterClient, tool
from openrouter_client.models import ChatCompletionTool, FunctionDefinition, StringParameter, FunctionParameters

client = OpenRouterClient(api_key="your-api-key")

# Method 1: Using the @tool decorator (recommended)
@tool
def get_weather(location: str) -> str:
    """Get the weather for a location.
    
    Args:
        location: The city and state
        
    Returns:
        Weather information for the location
    """
    # Your weather API logic here
    return f"The weather in {location} is sunny."
```

--------------------------------

### Creating Text Completions with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This example shows how to generate a text completion using client.completions.create(). It takes a model identifier and a prompt string as input. Optional parameters like max_tokens and temperature can be used to control the output. The method returns a CompletionResponse object.

```python
response = client.completions.create(
    model="openai/gpt-3.5-turbo-instruct",
    prompt="The capital of France is",
    max_tokens=50,
    temperature=0.7
)
```

--------------------------------

### Streaming Responses with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This Python function 'stream_with_processing' demonstrates how to handle streaming responses from the OpenRouter chat API. It processes chunks of the response in real-time, prints content as it arrives, and provides a live word count update to sys.stderr, showcasing efficient handling of large or continuous outputs.

```python
from openrouter_client import OpenRouterClient
import sys

client = OpenRouterClient(api_key="your-api-key")

def stream_with_processing():
    """Stream response and process chunks as they arrive."""
    stream = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": "Write a detailed explanation of quantum computing"}],
        stream=True,
        max_tokens=1000
    )
    
    full_response = ""
    chunk_count = 0
    
    print("Assistant: ", end="")
    for chunk in stream:
        chunk_count += 1
        delta = chunk.choices[0].delta
        
        if delta.content:
            content = delta.content
            full_response += content
            print(content, end="", flush=True)
            
            # Process chunks in real-time (e.g., word counting)
            if chunk_count % 10 == 0:
                word_count = len(full_response.split())
                sys.stderr.write(f"\r[Words: {word_count}]")
                sys.stderr.flush()
    
    print()  # New line
    print(f"\nStream completed. Total words: {len(full_response.split())}")
    return full_response

# Run streaming example
result = stream_with_processing()
```

--------------------------------

### Automatic Resource Cleanup with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet demonstrates how to use the OpenRouterClient with a 'with' statement for automatic resource cleanup. It shows making multiple synchronous API calls for chat completion, listing models, and retrieving credit information, ensuring the client resources are properly closed upon exiting the 'with' block.

```python
with OpenRouterClient(api_key="your-api-key") as client:
    # Make multiple requests
    response1 = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    
    response2 = client.models.list()
    
    credits = client.credits.get()
    
    print(f"Response: {response1.choices[0].message.content}")
    print(f"Available models: {len(response2.data)}")
    print(f"Credits: ${credits.data.credits}")
```

--------------------------------

### Implementing Prompt Caching with OpenRouter Chat API in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This snippet illustrates how to utilize prompt caching to reduce costs for repetitive system prompts. It demonstrates setting `cache_control: {'type': 'ephemeral'}` on a system message to cache it, allowing subsequent requests with the same system prompt to potentially reuse the cached content, leading to cost savings.

```Python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

# Create a long system prompt to cache
long_system_prompt = """You are an expert software engineer with 20 years of experience.
You specialize in Python, JavaScript, and system architecture.
You always provide detailed explanations and consider edge cases.
You write clean, maintainable code with proper error handling.
""" * 10  # Make it long enough to cache

# First request - caches the system prompt
response1 = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {
            "role": "system",
            "content": long_system_prompt,
            "cache_control": {"type": "ephemeral"}  # Cache this message
        },
        {"role": "user", "content": "Write a Python function to validate emails"}
    ]
)

print("First response:")
print(response1.choices[0].message.content)

# Second request - reuses cached system prompt (cheaper)
response2 = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {
            "role": "system",
            "content": long_system_prompt,  # Same cached content
            "cache_control": {"type": "ephemeral"}
        },
        {"role": "user", "content": "Write a JavaScript function to parse URLs"}
    ]
)

print("\nSecond response (using cached prompt):")
print(response2.choices[0].message.content)
```

--------------------------------

### Getting Credit Balance and Usage with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to fetch the current credit balance and usage information using client.credits.get(). It accesses the credits and usage attributes from the data field of the CreditsResponse object to display the financial details associated with the account.

```python
credits = client.credits.get()
print(f"Balance: ${credits.data.credits}")
print(f"Usage: ${credits.data.usage}")
```

--------------------------------

### Implementing Prompt Caching for OpenAI Models in OpenRouter

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This example illustrates how the OpenRouter client automatically handles prompt caching for OpenAI models when prompts exceed 1024 tokens. It shows a chat completion request with a long document for summarization, where caching is implicitly managed.

```Python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

# OpenAI models: automatic caching for prompts > 1024 tokens
response = client.chat.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Here is a long document: {long_text}\n\nSummarize this document."}
    ]
)
```

--------------------------------

### Getting Specific Model Information with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This code shows how to fetch detailed information about a specific model using client.models.get(), by providing its model_id. It then accesses attributes like context_length and pricing from the returned ModelInfo object to display relevant details about the model.

```python
model = client.models.get("anthropic/claude-3-opus")
print(f"Context length: {model.context_length}")
print(f"Pricing: {model.pricing}")
```

--------------------------------

### Getting Generation Details with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This code illustrates how to retrieve details for a specific generation using client.generations.get() by providing its generation_id. It then accesses and prints the status and created_at attributes from the returned GenerationResponse object, providing insight into the generation's state and timestamp.

```python
generation = client.generations.get("gen_123456789")
print(f"Status: {generation.status}")
print(f"Created: {generation.created_at}")
```

--------------------------------

### Manually Managing Rate Limits and Credits with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet illustrates how to manually check current API rate limits and credit balance using the OpenRouter client. It also provides an example of how to implement a simple wait mechanism if the request rate limit is low, allowing for manual control over API usage.

```python
# Check current rate limits
rate_limits = client.calculate_rate_limits()
print(f"Requests per minute: {rate_limits['requests_per_minute']}")
print(f"Tokens per minute: {rate_limits['tokens_per_minute']}")

# Check credit balance
credits = client.credits.get()
print(f"Current balance: ${credits.data.credits}")

# Wait for rate limit reset if needed
import time
if rate_limits['requests_per_minute'] < 10:
    print("Low rate limit, waiting...")
    time.sleep(60)  # Wait for reset
```

--------------------------------

### Configuring Built-in Rate Limiting with OpenRouter Client (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This example shows how to configure the OpenRouter client's built-in intelligent rate limiting via SmartSurge. It demonstrates setting `max_retries` for automatic retries on rate limits and `rate_limit_buffer` to add a safety margin, ensuring smooth operation during high request volumes.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(
    api_key="your-api-key",
    max_retries=5,                    # Retry on rate limits
    rate_limit_buffer=0.2             # 20% safety buffer
)

# Rate limiting is automatic
for i in range(100):
    response = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": f"Message {i}"}]
    )
    print(f"Completed request {i}")
```

--------------------------------

### Managing Conversation Context Length - OpenRouter Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This function, `manage_conversation_length`, demonstrates how to dynamically trim a list of messages to fit within a model's context window. It estimates token usage based on character count and prioritizes keeping system messages and the most recent user/assistant messages, ensuring that API requests do not exceed the model's input limits.

```Python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

def manage_conversation_length(messages, model, max_context_usage=0.8):
    """Keep conversation within context limits."""
    context_length = client.get_context_length(model)
    max_tokens = int(context_length * max_context_usage)
    
    # Rough token estimation (4 chars per token)
    total_chars = sum(len(msg["content"]) for msg in messages)
    estimated_tokens = total_chars // 4
    
    if estimated_tokens > max_tokens:
        # Keep system message and recent messages
        system_msgs = [msg for msg in messages if msg["role"] == "system"]
        other_msgs = [msg for msg in messages if msg["role"] != "system"]
        
        # Keep last N messages that fit
        char_budget = max_tokens * 4 - sum(len(msg["content"]) for msg in system_msgs)
        
        kept_messages = []
        current_chars = 0
        
        for msg in reversed(other_msgs):
            msg_chars = len(msg["content"])
            if current_chars + msg_chars <= char_budget:
                kept_messages.insert(0, msg)
                current_chars += msg_chars
            else:
                break
        
        return system_msgs + kept_messages
    
    return messages

# Example usage
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is AI?"},
    {"role": "assistant", "content": "AI stands for Artificial Intelligence..."},
    # ... many more messages ...
    {"role": "user", "content": "Tell me more about machine learning."}
]

# Manage conversation length
managed_messages = manage_conversation_length(conversation, "anthropic/claude-3-opus")

response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=managed_messages
)

print(response.choices[0].message.content)
```

--------------------------------

### Implementing Robust Error Handling with Retries - OpenRouter Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/examples.md

This `robust_chat_request` function demonstrates comprehensive error handling for OpenRouter API calls. It catches specific exceptions like `AuthenticationError`, `RateLimitError` (with retry-after logic), `ValidationError`, `NotFoundError`, and `ServerError` (with exponential backoff retries), providing a resilient way to interact with the API.

```Python
from openrouter_client import OpenRouterClient
from openrouter_client.exceptions import (
    OpenRouterError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
    NotFoundError,
    ServerError
)
import time

client = OpenRouterClient(api_key="your-api-key")

def robust_chat_request(messages, model, max_retries=3):
    """Make a chat request with robust error handling."""
    for attempt in range(max_retries):
        try:
            response = client.chat.create(
                model=model,
                messages=messages
            )
            return response
        
        except AuthenticationError:
            print("Authentication failed. Check your API key.")
            break
        
        except RateLimitError as e:
            print(f"Rate limited. Waiting {e.retry_after} seconds...")
            time.sleep(e.retry_after)
            continue
        
        except ValidationError as e:
            print(f"Invalid request parameters: {e}")
            break
        
        except NotFoundError:
            print(f"Model {model} not found. Try a different model.")
            break
        
        except ServerError as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Server error. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            else:
                print(f"Server error after {max_retries} attempts: {e}")
                break
        
        except OpenRouterError as e:
            print(f"Unexpected API error: {e}")
            break
    
    return None

# Use the robust function
response = robust_chat_request(
    messages=[{"role": "user", "content": "Hello!"}],
    model="anthropic/claude-3-opus"
)

if response:
    print(response.choices[0].message.content)
else:
    print("Failed to get response after retries.")
```

--------------------------------

### Getting Specific Model Context Length - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet illustrates how to obtain the context length for a specified model using `client.get_context_length()`. It takes a `model_id` string as a parameter, such as 'anthropic/claude-3-opus', and returns an integer representing the model's context length in tokens. This is useful for managing input size for specific models.

```python
context_length = client.get_context_length("anthropic/claude-3-opus")
print(f"Context length: {context_length}")
```

--------------------------------

### Initializing OpenRouter Client and Creating Chat Completion - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/index.md

This snippet demonstrates how to initialize the OpenRouterClient with an API key and create a basic chat completion. It shows how to send a user message to a specified model and print the model's response content. This requires the `openrouter_client` library.

```python
from openrouter_client import OpenRouterClient

# Initialize the client
client = OpenRouterClient(api_key="your-api-key")

# Create a chat completion
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message.content)
```

--------------------------------

### Configuring OpenRouter Client with Basic Parameters (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet demonstrates how to initialize the OpenRouter Python client with essential configuration parameters such as API key, base URL, HTTP referer, app title, request timeout, and maximum retry attempts. It provides a straightforward way to set up the client for general use.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(
    api_key="your-api-key",                    # Required
    base_url="https://openrouter.ai/api/v1",   # Default base URL
    http_referer="https://your-site.com",      # Optional referer header
    x_title="Your App Name",                   # Optional app name header
    timeout=30.0,                              # Request timeout in seconds
    max_retries=3                              # Maximum retry attempts
)
```

--------------------------------

### Initializing OpenRouterClient in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to initialize the OpenRouterClient class, which is the primary interface for interacting with the OpenRouter API. It shows how to pass essential parameters like api_key and optional configurations such as base_url, http_referer, x_title, timeout, and max_retries to configure the client's behavior.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(
    api_key="your-api-key",
    base_url="https://openrouter.ai/api/v1",  # Optional
    http_referer="https://your-site.com",     # Optional
    x_title="Your App Name",                  # Optional
    timeout=30.0,                             # Optional
    max_retries=3                             # Optional
)
```

--------------------------------

### Initializing OpenRouter Client with Environment Variables (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet shows how to initialize the OpenRouter Python client when configuration parameters are provided via environment variables. The client automatically detects and uses these variables, simplifying initialization and allowing for dynamic configuration without explicit code changes.

```python
from openrouter_client import OpenRouterClient

# Client will automatically use environment variables
client = OpenRouterClient()  # Uses OPENROUTER_API_KEY automatically
```

--------------------------------

### Using OpenRouter Client as a Context Manager for Automatic Cleanup - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

Demonstrates how to use the OpenRouter client within a `with` statement, ensuring automatic resource cleanup even when exceptions occur, promoting robust and efficient resource management.

```python
# Automatic resource cleanup
with OpenRouterClient(api_key="your-api-key") as client:
    response = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
# Client resources are automatically cleaned up here

# Handle exceptions within context
try:
    with OpenRouterClient(api_key="invalid-key") as client:
        response = client.chat.create(
            model="anthropic/claude-3-opus",
            messages=[{"role": "user", "content": "Hello!"}]
        )
except Exception as e:
    print(f"Error: {e}")
# Resources still cleaned up even with exceptions
```

--------------------------------

### Implementing Cost-Optimized Model Selection with OpenRouter Client (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This class, CostOptimizedClient, demonstrates how to dynamically select an OpenRouter model based on a specified maximum cost per 1k tokens. It estimates token count, fetches model pricing, and then selects the most capable model within the budget for chat operations. It requires the openrouter_client library.

```python
from openrouter_client import OpenRouterClient

class CostOptimizedClient:
    """Client that selects models based on cost and context needs."""
    
    def __init__(self, api_key: str):
        self.client = OpenRouterClient(api_key=api_key)
        self.model_tiers = {
            "cheap": ["openai/gpt-3.5-turbo", "anthropic/claude-3-haiku"],
            "medium": ["openai/gpt-4", "anthropic/claude-3-sonnet"],
            "premium": ["openai/gpt-4-turbo", "anthropic/claude-3-opus"]
        }
    
    def estimate_tokens(self, messages):
        """Rough token estimation."""
        total_chars = sum(len(msg["content"]) for msg in messages)
        return total_chars // 4  # Rough estimate
    
    def select_model(self, messages, max_cost_per_1k_tokens=0.01):
        """Select most capable model within cost budget."""
        token_count = self.estimate_tokens(messages)
        
        # Get model pricing
        models = self.client.models.list()
        suitable_models = []
        
        for model in models.data:
            if model.pricing and model.pricing.prompt:
                cost_per_1k = float(model.pricing.prompt)
                if cost_per_1k <= max_cost_per_1k_tokens:
                    suitable_models.append((model.id, cost_per_1k))
        
        # Sort by cost (descending) to get best model within budget
        suitable_models.sort(key=lambda x: x[1], reverse=True)
        
        return suitable_models[0][0] if suitable_models else "openai/gpt-3.5-turbo"
    
    def smart_chat(self, messages, max_cost_per_1k_tokens=0.01, **kwargs):
        """Chat with cost-optimized model selection."""
        model = self.select_model(messages, max_cost_per_1k_tokens)
        print(f"Selected model: {model}")
        
        return self.client.chat.create(
            model=model,
            messages=messages,
            **kwargs
        )

cost_client = CostOptimizedClient(api_key="your-api-key")
response = cost_client.smart_chat(
    messages=[{"role": "user", "content": "Simple question"}],
    max_cost_per_1k_tokens=0.005  # Prefer cheaper models
)
```

--------------------------------

### Loading OpenRouter Client Configuration from YAML (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

These Python functions demonstrate how to load OpenRouter client configuration from a YAML file and then use it to instantiate an OpenRouterClient. The load_config function reads the YAML, and create_client_from_config maps the loaded settings to client parameters. It requires the pyyaml and openrouter_client libraries.

```python
import yaml
from openrouter_client import OpenRouterClient

def load_config(config_file: str):
    """Load configuration from YAML file."""
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    return config['openrouter']

def create_client_from_config(config_file: str):
    """Create client from YAML configuration."""
    config = load_config(config_file)
    
    return OpenRouterClient(
        api_key=config['api_key'],
        base_url=config.get('base_url'),
        timeout=config.get('timeout'),
        max_retries=config.get('max_retries'),
        http_referer=config.get('headers', {}).get('http_referer'),
        x_title=config.get('headers', {}).get('x_title')
    )

# Usage
client = create_client_from_config("openrouter_config.yaml")
```

--------------------------------

### Setting OpenRouter Client Configuration via Environment Variables (Bash)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet demonstrates how to configure the OpenRouter Python client using environment variables. It provides a way to set common parameters like API key, base URL, HTTP referer, app title, timeout, and retry settings externally, promoting secure credential management and flexible deployment without hardcoding values.

```bash
# API key (alternative to passing in code)
export OPENROUTER_API_KEY="your-api-key"

# Base URL override
export OPENROUTER_BASE_URL="https://custom-endpoint.com/api/v1"

# Default headers
export OPENROUTER_HTTP_REFERER="https://your-site.com"
export OPENROUTER_X_TITLE="Your App Name"

# Timeout and retry settings
export OPENROUTER_TIMEOUT="60.0"
export OPENROUTER_MAX_RETRIES="5"

# Logging level
export OPENROUTER_LOG_LEVEL="INFO"
```

--------------------------------

### Manually Defining Tools for OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet illustrates how to manually define a tool for the OpenRouter Python client using helper functions like `build_tool_definition`. It shows how to create a Python function (`search_database`) with type hints and then convert it into a `ChatCompletionTool` object, which can then be passed to the `client.chat.create` method for function calling.

```python
from openrouter_client.tools import (
    build_tool_definition,
    build_parameter_schema
)
from openrouter_client.models import (
    StringParameter,
    NumberParameter,
    ArrayParameter,
    ChatCompletionTool
)
from typing import List

# Define the function with proper type hints
def search_database(query: str, limit: int = 10, categories: List[str] = None) -> dict:
    """Search for items in a database.
    
    Args:
        query: Search query
        limit: Maximum results (1-100)
        categories: Search categories
    """
    pass

# Create tool from function
search_tool = build_tool_definition(search_database)

response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Search for books about AI"}],
    tools=[search_tool],
    tool_choice="auto"
)
```

--------------------------------

### Defining and Using Custom Tools with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This snippet demonstrates how to manually define a tool using `ChatCompletionTool` and `FunctionDefinition` classes, specifying its name, description, and parameters. It then shows how to make a chat completion request that utilizes this tool and processes the tool call response.

```Python
weather_tool = ChatCompletionTool(
    type="function",
    function=FunctionDefinition(
        name="get_weather",
        description="Get the weather for a location",
        parameters=FunctionParameters(
            type="object",
            properties={
                "location": StringParameter(
                    type="string",
                    description="The city and state"
                )
            },
            required=["location"]
        )
    )
)

# Make a request with tool
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {"role": "user", "content": "What's the weather like in San Francisco?"}
    ],
    tools=[get_weather],  # Using the decorated function
)

# Process tool calls
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    print(f"Tool called: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")
```

--------------------------------

### Configuring OpenRouter Client Basic Logging (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet demonstrates how to set up basic logging for the OpenRouter Python client using configure_logging. It allows setting a global logging level (e.g., INFO, DEBUG) for all client components or for specific components, enabling easy monitoring of client operations.

```python
from openrouter_client import configure_logging
import logging

# Configure all OpenRouter client logging
configure_logging(level=logging.INFO)

# Or configure specific components
configure_logging(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

--------------------------------

### Initializing OpenRouter Client from JSON in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This Python function `create_client_from_json` reads OpenRouter client configuration from a specified JSON file. It parses the 'openrouter' section of the JSON and uses the extracted parameters to instantiate an `OpenRouterClient` object, handling missing optional parameters gracefully.

```python
import json
from openrouter_client import OpenRouterClient

def create_client_from_json(config_file: str):
    """Create client from JSON configuration."""
    with open(config_file, 'r') as f:
        config = json.load(f)['openrouter']
    
    return OpenRouterClient(
        api_key=config['api_key'],
        base_url=config.get('base_url'),
        timeout=config.get('timeout'),
        max_retries=config.get('max_retries'),
        http_referer=config.get('headers', {}).get('http_referer'),
        x_title=config.get('headers', {}).get('x_title')
    )

client = create_client_from_json("openrouter_config.json")
```

--------------------------------

### Initializing OpenRouter Client with Encrypted API Key - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

Illustrates how to initialize the OpenRouter client using `AuthManager` to securely handle the API key, with an option to encrypt the key in memory for enhanced security.

```python
from openrouter_client import AuthManager

# Create auth manager with encryption
auth = AuthManager(
    api_key="your-api-key",
    encrypt_key=True  # Encrypt the key in memory
)

client = OpenRouterClient(auth_manager=auth)
```

--------------------------------

### Implementing Automatic Model Fallbacks with OpenRouter Client (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This code demonstrates how to create a `FallbackClient` that automatically attempts to use a series of preferred models. It catches `NotFoundError` and `ServerError` exceptions, allowing the client to gracefully fall back to the next model in the list if a primary model fails or is unavailable.

```python
from openrouter_client import OpenRouterClient
from openrouter_client.exceptions import NotFoundError, ServerError

class FallbackClient:
    """Client with automatic model fallbacks."""
    
    def __init__(self, api_key: str):
        self.client = OpenRouterClient(api_key=api_key)
        self.preferred_models = [
            "anthropic/claude-3-opus",
            "anthropic/claude-3-sonnet", 
            "openai/gpt-4-turbo",
            "openai/gpt-3.5-turbo"
        ]
    
    def chat_with_fallback(self, messages, **kwargs):
        """Try models in order of preference."""
        for model in self.preferred_models:
            try:
                return self.client.chat.create(
                    model=model,
                    messages=messages,
                    **kwargs
                )
            except (NotFoundError, ServerError) as e:
                print(f"Model {model} failed: {e}")
                continue
        
        raise Exception("All fallback models failed")

fallback_client = FallbackClient(api_key="your-api-key")
response = fallback_client.chat_with_fallback(
    messages=[{"role": "user", "content": "Hello!"}]
)
```

--------------------------------

### Retrieving API Key Information - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to retrieve information about the current API key using the `client.keys.get()` method. It accesses the `label` and `usage` attributes from the returned `KeysResponse` object to display key details. This method requires an authenticated client instance.

```python
keys_info = client.keys.get()
print(f"Label: {keys_info.data.label}")
print(f"Usage: {keys_info.data.usage}")
```

--------------------------------

### Configuring OpenRouter Client Advanced Logging (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet illustrates advanced logging configuration for the OpenRouter Python client by directly interacting with Python's logging module. It shows how to create custom loggers, handlers, and formatters, and how to set component-specific logging levels for granular control over log output.

```python
import logging
from openrouter_client import OpenRouterClient

# Create custom logger configuration
logger = logging.getLogger("openrouter_client")
logger.setLevel(logging.DEBUG)

# Create custom handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create custom formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

logger.addHandler(handler)

# Configure component-specific logging levels
logging.getLogger("openrouter_client.http").setLevel(logging.DEBUG)      # HTTP requests
logging.getLogger("openrouter_client.auth").setLevel(logging.INFO)       # Authentication
logging.getLogger("openrouter_client.endpoints").setLevel(logging.WARN)  # Endpoint calls
logging.getLogger("openrouter_client.streaming").setLevel(logging.ERROR) # Streaming

client = OpenRouterClient(api_key="your-api-key")
```

--------------------------------

### Configuring OpenRouter Client in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This snippet illustrates the various configuration options available when initializing the OpenRouter client, including API keys, base URL, organization ID, logging level, timeout, retries, and backoff factor. It allows for fine-grained control over client behavior.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(
    api_key="your-api-key",  # API key for authentication
    provisioning_api_key="your-prov-key",  # Optional: for API key management
    base_url="https://openrouter.ai/api/v1",  # Base URL for API
    organization_id="your-org-id",  # Optional organization ID
    reference_id="your-ref-id",  # Optional reference ID
    log_level="INFO",  # Logging level
    timeout=60.0,  # Request timeout in seconds
    retries=3,  # Number of retries for failed requests
    backoff_factor=0.5,  # Exponential backoff factor
    rate_limit=None  # Optional custom rate limit (auto-configured by default)
)
```

--------------------------------

### Creating Chat Completion with Cached System Prompt - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

Demonstrates how to make a chat completion request using the OpenRouter Python client, specifying a system prompt with `cache_control` set to `ephemeral` to potentially reduce costs on subsequent requests with the same prompt.

```python
response2 = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {
            "role": "system", 
            "content": "You are an expert programmer...",  # Same cached prompt
            "cache_control": {"type": "ephemeral"}
        },
        {"role": "user", "content": "Write a JavaScript function"}
    ]
)
```

--------------------------------

### Configuring OpenRouter Client with JSON

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This JSON snippet defines the configuration parameters for the OpenRouter client, including API key, base URL, timeout, retry settings, and custom headers for referrer and application title. It also includes rate limiting settings.

```json
{
  "openrouter": {
    "api_key": "your-api-key",
    "base_url": "https://openrouter.ai/api/v1",
    "timeout": 30.0,
    "max_retries": 3,
    "headers": {
      "http_referer": "https://your-site.com",
      "x_title": "Your App Name"
    },
    "rate_limiting": {
      "enabled": true,
      "buffer": 0.1
    }
  }
}
```

--------------------------------

### Implementing Prompt Caching with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet demonstrates how to utilize prompt caching for compatible models in the OpenRouter client to potentially reduce costs. By setting `cache_control` to `{"type": "ephemeral"}` within a message, specific prompts can be cached, optimizing repeated API calls with similar system prompts.

```python
# Cache a system prompt
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {
            "role": "system", 
            "content": "You are an expert programmer...",  # Long system prompt
            "cache_control": {"type": "ephemeral"}  # Cache this message
        },
        {"role": "user", "content": "Write a Python function"}
    ]
)
```

--------------------------------

### Programmatic API Key Management with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This snippet illustrates how to manage OpenRouter API keys programmatically, including retrieving current key information (usage, rate limits), listing all available keys, and creating new keys with specified names, labels, and credit limits. It requires a provisioning API key for these operations.

```Python
client = OpenRouterClient(
    api_key="your-api-key",
    provisioning_api_key="your-provisioning-key"
)

# Get current key information
key_info = client.keys.get_current()
print(f"Current usage: {key_info['data']['usage']} credits")
print(f"Rate limit: {key_info['data']['rate_limit']['requests']} requests per {key_info['data']['rate_limit']['interval']}")

# List all keys
keys = client.keys.list()

# Create a new key
new_key = client.keys.create(
    name="My New Key",
    label="Production API Key",
    limit=1000.0  # Credit limit
)
```

--------------------------------

### Creating Chat Completions (Streaming) with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to create a streaming chat completion using client.chat.create() by setting stream=True. The method returns an iterator, allowing the application to process content chunks as they are generated. It shows how to iterate over the stream and print the content delta from each chunk.

```python
stream = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

--------------------------------

### Calculating API Rate Limits - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to calculate the current API rate limits based on the user's credit balance using `client.calculate_rate_limits()`. It returns a dictionary containing 'requests_per_minute' and 'tokens_per_minute', which can be used to manage API call frequency and token consumption. This helps in preventing `RateLimitError` exceptions.

```python
rate_limits = client.calculate_rate_limits()
print(f"Requests per minute: {rate_limits['requests_per_minute']}")
print(f"Tokens per minute: {rate_limits['tokens_per_minute']}")
```

--------------------------------

### Defining Model Information Model - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet defines the `ModelInfo` data model, which describes the structure for information about individual models available through the OpenRouter API. It includes attributes such as `id`, `name`, `description`, `context_length`, `pricing` details, and an optional `top_provider`. This model is used when retrieving details about available AI models.

```python
class ModelInfo:
    id: str
    name: str
    description: str
    context_length: int
    pricing: ModelPricing
    top_provider: Optional[str]
```

--------------------------------

### Implementing Prompt Caching for Anthropic Models in OpenRouter

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This snippet demonstrates explicit prompt caching for Anthropic models using `cache_control` markers within the message content. It shows how to mark specific parts of a long document for ephemeral caching during a summarization request.

```Python
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Here is a long document:"},
                # Mark this part for caching
                {"type": "text", "text": long_text, "cache_control": {"type": "ephemeral"}},
                {"type": "text", "text": "Summarize this document."}
            ]
        }
    ]
)
```

--------------------------------

### Listing Available Models with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to retrieve a list of all available models using client.models.list(). It then iterates through the data attribute of the ModelsResponse object to print the ID and name of each model. This is useful for discovering supported models.

```python
models = client.models.list()
for model in models.data:
    print(f"{model.id}: {model.name}")
```

--------------------------------

### Defining Completion Response Model - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet defines the `CompletionResponse` data model, outlining the structure of responses from text completion API calls. It includes fields like `id`, `object`, `created` timestamp, the `model` identifier, a list of `choices`, and optional `usage` information. This class is essential for parsing and utilizing the results of text completion requests.

```python
class CompletionResponse:
    id: str
    object: str
    created: int
    model: str
    choices: List[CompletionChoice]
    usage: Optional[Usage]
```

--------------------------------

### Streaming Chat Completion Responses in OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet demonstrates how to stream responses from the OpenRouter chat completion API for real-time output. It shows how to set `stream=True` in the `client.chat.create` call and then iterate over the `stream` object, printing each content chunk as it arrives, ensuring immediate display using `flush=True`.

```python
stream = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Write a long story"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

--------------------------------

### Configuring Detailed Logging for OpenRouter Client - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

Explains how to configure logging for the OpenRouter client, enabling debug level logging for the entire client or specific modules like HTTP requests and chat endpoints to aid in debugging and monitoring.

```python
from openrouter_client import configure_logging
import logging

# Enable debug logging
configure_logging(level=logging.DEBUG)

# Or configure specific loggers
logging.getLogger("openrouter_client.http").setLevel(logging.DEBUG)
logging.getLogger("openrouter_client.endpoints.chat").setLevel(logging.INFO)

client = OpenRouterClient(api_key="your-api-key")

# All HTTP requests and responses will be logged
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

--------------------------------

### Defining and Using Tools with @tool Decorator in OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet demonstrates how to define and use a tool for function calling in the OpenRouter Python client using the `@tool` decorator. It shows how to convert a Python function (`get_weather`) into an OpenRouter-compatible tool, make a chat completion request with the tool, and then execute the tool based on the model's `tool_calls` response.

```python
from openrouter_client import OpenRouterClient, tool

@tool
def get_weather(location: str, unit: str = "celsius") -> str:
    """Get the current weather for a location.
    
    Args:
        location: The city and state/country
        unit: Temperature unit (celsius or fahrenheit)
    """
    # Your weather API logic here
    return f"The weather in {location} is 22°{unit[0].upper()}"

client = OpenRouterClient(api_key="your-api-key")

response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=[get_weather.to_dict()],
    tool_choice="auto"
)

# Handle tool calls
if response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
        if tool_call.function.name == "get_weather":
            # Execute the function
            result = get_weather.execute(tool_call.function.arguments)
            print(result)
```

--------------------------------

### Handling and Executing Tool Calls in OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet provides a utility function `handle_tool_calls` to process and execute tool calls received from an OpenRouter chat completion response. It demonstrates how to parse tool arguments, execute the corresponding tool function (represented by `execute_tool`), and then append the tool's response back into the conversation messages to continue the chat with the model.

```python
import json

def handle_tool_calls(response):
    """Process tool calls from a chat response."""
    if not response.choices[0].message.tool_calls:
        return response.choices[0].message.content
    
    messages = [{"role": "user", "content": "Original user message"}]
    messages.append(response.choices[0].message.dict())
    
    for tool_call in response.choices[0].message.tool_calls:
        # Parse arguments safely
        try:
            args = json.loads(tool_call.function.arguments)
        except json.JSONDecodeError as e:
            print(f"Invalid tool arguments: {e}")
            continue
            
        # Execute tool (implement your logic here)
        result = execute_tool(tool_call.function.name, args)
        
        # Add tool response to conversation
        tool_response = {
            "role": "tool",
            "content": json.dumps(result) if isinstance(result, dict) else str(result),
            "tool_call_id": tool_call.id
        }
        messages.append(tool_response)
    
    # Continue conversation with tool results
    return client.chat.create(
        model="anthropic/claude-3-opus",
        messages=messages
    )
```

--------------------------------

### Defining OpenRouter Client Configuration in YAML

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This YAML file (openrouter_config.yaml) defines various configuration parameters for the OpenRouter client, including API key, base URL, timeout, retry settings, custom headers, rate limiting, logging, and preferred/fallback models. It serves as an externalized configuration source.

```yaml
# openrouter_config.yaml
openrouter:
  api_key: "your-api-key"
  base_url: "https://openrouter.ai/api/v1"
  timeout: 30.0
  max_retries: 3
  
  headers:
    http_referer: "https://your-site.com"
    x_title: "Your App Name"
  
  rate_limiting:
    enabled: true
    buffer: 0.1
  
  logging:
    level: "INFO"
    format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  
  models:
    preferred: ["anthropic/claude-3-opus", "openai/gpt-4-turbo"]
    fallback: ["openai/gpt-3.5-turbo"]
```

--------------------------------

### Handling OpenRouter API Exceptions - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates a robust error handling pattern for OpenRouter API calls using a `try-except` block. It catches specific exceptions like `AuthenticationError` for invalid API keys, `RateLimitError` for exceeding limits (providing `retry_after` information), and `ValidationError` for malformed requests. This pattern ensures graceful degradation and informative feedback during API interactions.

```python
from openrouter_client.exceptions import *

try:
    response = client.chat.create(...)
except AuthenticationError:
    print("Check your API key")
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}")
except ValidationError as e:
    print(f"Invalid request: {e}")
```

--------------------------------

### Implementing Custom Secrets Management for OpenRouter Client - Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

Shows how to create a custom `SecretsManager` class to integrate OpenRouter client with external secret storage solutions, allowing for flexible and secure API key retrieval and storage.

```python
from openrouter_client.auth import SecretsManager

class CustomSecretsManager(SecretsManager):
    """Custom secrets manager using your preferred storage."""
    
    def get_secret(self, key: str) -> str:
        # Implement your secret retrieval logic
        # e.g., from AWS Secrets Manager, HashiCorp Vault, etc.
        pass
    
    def set_secret(self, key: str, value: str) -> None:
        # Implement your secret storage logic
        pass

# Use with client
secrets_manager = CustomSecretsManager()
auth = AuthManager(secrets_manager=secrets_manager)
client = OpenRouterClient(auth_manager=auth)
```

--------------------------------

### Configuring OpenRouter Client File Logging (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet demonstrates how to configure the OpenRouter Python client to log messages directly to a file. By specifying a filename in configure_logging, all client logs will be written to the specified file, which is useful for persistent logging and debugging.

```python
import logging
from openrouter_client import configure_logging

# Log to file
configure_logging(
    level=logging.INFO,
    filename="openrouter_client.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
```

--------------------------------

### Managing OpenRouter Client Pool with Context Manager (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

The ClientPool class provides a thread-safe mechanism to manage a pool of OpenRouterClient instances. It uses a context manager (@contextmanager) to ensure clients are acquired and released properly, facilitating concurrent usage and resource efficiency. It requires openrouter_client and threading.

```python
from openrouter_client import OpenRouterClient
from contextlib import contextmanager
import threading

class ClientPool:
    """Pool of OpenRouter clients for concurrent usage."""
    
    def __init__(self, api_key: str, pool_size: int = 5):
        self.pool = []
        self.lock = threading.Lock()
        
        for _ in range(pool_size):
            client = OpenRouterClient(api_key=api_key)
            self.pool.append(client)
    
    @contextmanager
    def get_client(self):
        """Get a client from the pool."""
        with self.lock:
            if not self.pool:
                raise Exception("No clients available in pool")
            client = self.pool.pop()
        
        try:
            yield client
        finally:
            with self.lock:
                self.pool.append(client)
    
    def close_all(self):
        """Close all clients in the pool."""
        with self.lock:
            for client in self.pool:
                client.close()
            self.pool.clear()

# Usage
pool = ClientPool(api_key="your-api-key", pool_size=3)

try:
    with pool.get_client() as client:
        response = client.chat.create(
            model="anthropic/claude-3-opus",
            messages=[{"role": "user", "content": "Hello!"}]
        )
        print(response.choices[0].message.content)
finally:
    pool.close_all()
```

--------------------------------

### Configuring OpenRouter Client with Custom Managers (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet illustrates advanced client configuration using custom AuthManager and HTTPManager instances. It allows for fine-grained control over authentication (e.g., API key encryption) and HTTP request behavior, including detailed timeout, retry, and rate limiting settings, providing more robust and tailored client operation.

```python
from openrouter_client import OpenRouterClient, AuthManager, HTTPManager

# Custom authentication manager
auth_manager = AuthManager(
    api_key="your-api-key",
    encrypt_key=True  # Encrypt API key in memory
)

# Custom HTTP manager with advanced settings
http_manager = HTTPManager(
    base_url="https://openrouter.ai/api/v1",
    timeout=60.0,
    max_retries=5,
    retry_delay=1.0,                           # Base retry delay
    retry_backoff=2.0,                         # Backoff multiplier
    rate_limit_enabled=True,                   # Enable automatic rate limiting
    rate_limit_buffer=0.1                      # Rate limit safety buffer (10%)
)

client = OpenRouterClient(
    auth_manager=auth_manager,
    http_manager=http_manager
)
```

--------------------------------

### Handling Streaming with Function Calls in OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet demonstrates how to process streaming responses from the OpenRouter API, specifically handling accumulated content and parsing tool calls as they arrive. It shows how to reconstruct tool call arguments from delta chunks and then execute the completed tool calls.

```python
def handle_streaming_with_tools():
    stream = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": "What's the weather?"}],
        tools=[get_weather.to_dict()],
        stream=True
    )
    
    accumulated_content = ""
    tool_calls = []
    
    for chunk in stream:
        delta = chunk.choices[0].delta
        
        if delta.content:
            accumulated_content += delta.content
            print(delta.content, end="", flush=True)
        
        if delta.tool_calls:
            # Accumulate tool calls
            for i, tool_call in enumerate(delta.tool_calls):
                if i >= len(tool_calls):
                    tool_calls.append({
                        "id": tool_call.id,
                        "function": {"name": "", "arguments": ""}
                    })
                
                if tool_call.function.name:
                    tool_calls[i]["function"]["name"] = tool_call.function.name
                if tool_call.function.arguments:
                    tool_calls[i]["function"]["arguments"] += tool_call.function.arguments
    
    # Process completed tool calls
    for tool_call in tool_calls:
        if tool_call["function"]["name"] == "get_weather":
            result = get_weather.execute(tool_call["function"]["arguments"])
            print(f"\nWeather result: {result}")
```

--------------------------------

### Configuring Automatic Rate Limiting with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet demonstrates how to initialize the OpenRouter client with automatic rate limiting and retry capabilities. By setting `max_retries` and `timeout`, the client will automatically handle API rate limits, ensuring robust communication without manual intervention.

```python
client = OpenRouterClient(
    api_key="your-api-key",
    max_retries=5,  # Automatic retries on rate limits
    timeout=60.0    # Extended timeout for retries
)

# The client automatically handles rate limits
for i in range(100):
    response = client.chat.create(
        model="anthropic/claude-3-opus",
        messages=[{"role": "user", "content": f"Request {i}"}]
    )
    print(f"Completed request {i}")
```

--------------------------------

### Implementing Custom Rate Limiting for OpenRouter Client (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet illustrates how to implement custom rate limiting by extending the `HTTPManager` class. The `CustomRateLimitHTTPManager` enforces a minimum interval between requests, ensuring that API calls adhere to specific rate limits beyond the client's built-in mechanisms.

```python
from openrouter_client import HTTPManager, OpenRouterClient
import time

class CustomRateLimitHTTPManager(HTTPManager):
    """Custom HTTP manager with additional rate limiting."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_request_time = 0
        self.min_request_interval = 1.0  # 1 second between requests
    
    def make_request(self, *args, **kwargs):
        """Make request with custom rate limiting."""
        # Enforce minimum interval between requests
        now = time.time()
        elapsed = now - self.last_request_time
        if elapsed < self.min_request_interval:
            time.sleep(self.min_request_interval - elapsed)
        
        self.last_request_time = time.time()
        return super().make_request(*args, **kwargs)

http_manager = CustomRateLimitHTTPManager()
client = OpenRouterClient(
    api_key="your-api-key",
    http_manager=http_manager
)
```

--------------------------------

### Listing Model Endpoints with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet demonstrates how to retrieve information about model endpoints using client.models.list_endpoints(). The method returns a ModelEndpointsResponse object containing a dictionary of endpoint data, which can be printed to inspect the available endpoints and their configurations.

```python
endpoints = client.models.list_endpoints()
print(endpoints.data)  # Dictionary of model endpoint information
```

--------------------------------

### Defining Chat Completion Response Model - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet defines the `ChatCompletionResponse` data model, which represents the structure of responses from chat completion API calls. It includes fields such as `id`, `object`, `created` timestamp, the `model` used, a list of `choices`, and optional `usage` statistics. This class is crucial for type-hinting and understanding the shape of successful chat API responses.

```python
class ChatCompletionResponse:
    id: str
    object: str
    created: int
    model: str
    choices: List[ChatCompletionChoice]
    usage: Optional[Usage]
```

--------------------------------

### Creating Chat Completions (Synchronous) with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This code snippet illustrates how to create a synchronous chat completion using the client.chat.create() method. It requires a model identifier and a list of messages with roles and content. Optional parameters like max_tokens, temperature, and stream (set to False for synchronous) can be used to control the generation. The method returns a ChatCompletionResponse object.

```python
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    max_tokens=100,
    temperature=0.7,
    stream=False
)
```

--------------------------------

### Managing Model Context Lengths with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This code shows how to programmatically refresh and retrieve the maximum token context length for specific models using the OpenRouter client. It demonstrates fetching the context length for 'anthropic/claude-3-opus' and printing it.

```Python
# Refresh model context lengths from the API
context_lengths = client.refresh_context_lengths()

# Get context length for a specific model
max_tokens = client.get_context_length("anthropic/claude-3-opus")
print(f"Claude 3 Opus supports up to {max_tokens} tokens")
```

--------------------------------

### Implementing Custom Authentication for OpenRouter Client (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet shows how to implement custom authentication for the OpenRouter Python client by extending the AuthManager class. It allows adding custom headers (e.g., X-Custom-Header, User-Agent) to all outgoing requests, providing flexibility for integrating with specific API requirements or tracking client usage.

```python
from openrouter_client import AuthManager, OpenRouterClient

class CustomAuthManager(AuthManager):
    """Custom authentication with additional headers."""
    
    def get_headers(self) -> dict:
        """Get authentication headers."""
        headers = super().get_headers()
        headers.update({
            "X-Custom-Header": "custom-value",
            "User-Agent": "MyApp/1.0"
        })
        return headers

auth_manager = CustomAuthManager(api_key="your-api-key")
client = OpenRouterClient(auth_manager=auth_manager)
```

--------------------------------

### Managing Model Context Lengths with OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/advanced-features.md

This snippet demonstrates how to retrieve a model's context length and refresh the cache. It also includes a utility function `truncate_messages` that shows a basic approach to truncating message history to fit within the model's token limits, ensuring efficient and compliant API calls.

```python
# Get context length for a model
context_length = client.get_context_length("anthropic/claude-3-opus")
print(f"Claude 3 Opus context length: {context_length}")

# Refresh context length cache
client.refresh_context_lengths()

# Use context length for message truncation
def truncate_messages(messages, model, reserve_tokens=1000):
    """Truncate messages to fit within model context length."""
    max_tokens = client.get_context_length(model) - reserve_tokens
    
    # Simple truncation (implement token counting as needed)
    total_chars = sum(len(msg["content"]) for msg in messages)
    if total_chars > max_tokens * 4:  # Rough estimate: 4 chars per token
        # Keep system message and last few user messages
        system_msgs = [msg for msg in messages if msg["role"] == "system"]
        other_msgs = [msg for msg in messages if msg["role"] != "system"]
        
        # Take last N messages that fit
        truncated = system_msgs + other_msgs[-10:]
        return truncated
    
    return messages

# Use in chat completion
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    # ... many messages ...
    {"role": "user", "content": "Latest question"}
]

truncated_messages = truncate_messages(messages, "anthropic/claude-3-opus")
response = client.chat.create(
    model="anthropic/claude-3-opus",
    messages=truncated_messages
)
```

--------------------------------

### Streaming OpenRouter Chat Responses in Python

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/README.md

This snippet shows how to stream responses from the chat completion endpoint. It iterates over chunks received from the API, allowing for real-time display of generated content, which is useful for long responses.

```python
from openrouter_client import OpenRouterClient

client = OpenRouterClient(api_key="your-api-key")

# Stream the response
for chunk in client.chat.create(
    model="openai/gpt-4",
    messages=[
        {"role": "user", "content": "Write a short poem about AI."}
    ],
    stream=True,
):
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

--------------------------------

### Refreshing Model Context Lengths - OpenRouter Python Client

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/api-reference.md

This snippet shows how to refresh the cached context length information for all models available through the OpenRouter API. The `client.refresh_context_lengths()` method updates internal data, ensuring subsequent context length queries are based on the most current information. It does not return any value.

```python
client.refresh_context_lengths()
```

--------------------------------

### Integrating AWS Secrets Manager with OpenRouter Client (Python)

Source: https://github.com/dingo-actual/openrouter-python-client/blob/main/docs/configuration.md

This snippet demonstrates how to integrate AWS Secrets Manager to securely retrieve API keys and other secrets for the OpenRouter client. It defines a custom `AWSSecretsManager` class that extends `openrouter_client.auth.SecretsManager`, implementing `get_secret` to fetch values from AWS and `set_secret` for storage.

```python
from openrouter_client.auth import SecretsManager, AuthManager
from openrouter_client import OpenRouterClient

class AWSSecretsManager(SecretsManager):
    """Example AWS Secrets Manager integration."""
    
    def __init__(self, secret_name: str, region: str):
        self.secret_name = secret_name
        self.region = region
        # Initialize AWS client here
    
    def get_secret(self, key: str) -> str:
        """Retrieve secret from AWS Secrets Manager."""
        # Implement AWS Secrets Manager retrieval
        # This is a simplified example
        import boto3
        import json
        
        client = boto3.client('secretsmanager', region_name=self.region)
        response = client.get_secret_value(SecretId=self.secret_name)
        secrets = json.loads(response['SecretString'])
        return secrets.get(key)
    
    def set_secret(self, key: str, value: str) -> None:
        """Store secret in AWS Secrets Manager."""
        # Implement AWS Secrets Manager storage
        pass

# Use with OpenRouter client
secrets_manager = AWSSecretsManager("openrouter-secrets", "us-east-1")
auth_manager = AuthManager(secrets_manager=secrets_manager)
client = OpenRouterClient(auth_manager=auth_manager)
```