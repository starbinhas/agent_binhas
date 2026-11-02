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
            request = {
                "model": self.model,
                "messages": self.messages
            }

            if self.tool_schemas:   # at the end, every agent will have tools and there will be no need for this check
                request["tools"] = self.tool_schemas
                request["tool_choice"] = "auto"

            response = self.client.chat.completions.create(**request)
            message = response.choices[0].message

            print(f"[agent response message]\n{message}\n\n")

            assistant_message = {
                "role": "assistant",
                "content": message.content
            }

            if message.tool_calls:      # does really need to add "tool_calls"? Isn't it in message already?
                assistant_message["tool_calls"] = [
                    tool_call.model_dump(exclude_none=True)
                    for tool_call in message.tool_calls
                ]

            self.messages.append(assistant_message)

            if not message.tool_calls:
                return message.content or ""    # is it possible to the LLM to return None?

            for tool_call in message.tool_calls:
                name = tool_call.function.name
                arguments = tool_call.function.arguments

                try:
                    args = json.loads(arguments)
                    function = self.tools[name]

                    print(f"\n[Agent] Calling: {name}")
                    print(f"[Agent] Arguments: {args}")

                    result = function(**args)

                except (ValueError, TypeError, KeyError, OSError) as error:     # is this error handler good?
                    result = {
                        "error": str(error),
                        "status": "failed"
                    }

                print(f"[Agent] Tool result: {result}")

                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": json.dumps(result)
                })

        return "Max tool rounds reached."