import json

from groq import Groq


class Agent:

    def __init__(self, model, tools, system_prompt, tool_schemas=None):
        self.client = Groq()
        self.model = model
        self.tools = tools
        self.tool_schemas = tool_schemas or []

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

            response = self.client.chat.completions.create(
                {
                    "model": self.model,
                    "messages": self.messages,
                    "tools": self.tool_schemas,
                    "tool_choice": "auto"
                }
            )

            message = response.choices[0].message

            assistant_message = {
                "role": "assistant",
                "content": message.content or ""
            }

            self.messages.append(response.message)

            if not response.message.tool_calls:
                return response.message.content

            for tool_call in response.message.tool_calls:
                name = tool_call.function.name
                args = tool_call.function.arguments

                print(f"\n[Agent] Calling: {name}")
                print(f"\n[Agent] Arguments: {args}")

                function = self.tools[name]

                result = function(**args)

                print(f"[Agent] Tool result: {result}")

                self.messages.append({
                    "role": "tool",
                    "tool_name": name,
                    "content": json.dumps(result)
                })

        return "Max tool rounds reached."