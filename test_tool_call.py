from ollama import chat
from tools import sum_calculator

MODEL = "qwen3:8b"

messages = [
    {
        "role": "system",
        "content": "When adding numbers, answer with both tool call and content telling the user you are calculating and always use sum_calculator."
    },
    {
        "role": "user",
        "content": "What is 249459257 + 283985725? Use the calculator."
    }
]

response = chat(
    model=MODEL,
    messages=messages,
    tools=[sum_calculator],
    think=False
)

print(f"First response: {response.message.content}")
messages.append(response.message)

print(messages)

if response.message.tool_calls:
    for tool_call in response.message.tool_calls:

        name = tool_call.function.name
        args = tool_call.function.arguments

        type(args)
        print(args)

        print(f"Tool requested: {name}")
        print(f"Arguments: {args}")

        if name != "sum_calculator": # does it make sense?
            raise ValueError(f"Unkown tool: {name}")

        result = sum_calculator(**args)

        print(f"Tool result: {result}")

        messages.append({
            "role": "tool",
            "tool_name": name,
            "content": str(result)
        })

    final_response = chat(
        model=MODEL,
        messages=messages,
        tools=[sum_calculator],
        think=False
    )

    print(f"\nAgent: {final_response.message.content}")
else:
    print("Agent:", response.message.content)