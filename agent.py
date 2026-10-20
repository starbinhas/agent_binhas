from ollama import chat

class Agent:

    def __init__(self, model, tools, system_prompt):
        self.model = model
        self.tools = tools

        self.messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def ask(self, user_input):

        self.messages.append({
            "role": "user",
            "content": user_input
        })

        max_rounds = 5

        for _ in range(max_rounds):

            response = chat(
                model=self.model,
                messages=self.messages,
                tools=list(self.tools.values()),
                think=False
            )

            self.messages.append(response.message)

            if not response.message.tool_calls:
                return response.message.content

            for tool_call in response.message.tool_calls:
                name = tool_call.function.name
                args = tool_call.function.arguments

                print(f"\n[Agent] Calling: {name}")
                print(f"\n[Agent] Arguments: {args}")

                function = self.tools.get(name)

                if function is None:
                    result = f"Error: Unknown tool'{name}'"
                else:
                    try:
                        result = function(**args)
                    except (TypeError, ValueError) as error:
                        result = f"Tool error: {error}"

                print(f"[Agent] Tool result: {result}")

                self.messages.append({
                    "role": "tool",
                    "tool_name": name,
                    "content": str(result)
                })

            return "Maximum tool rounds reached."