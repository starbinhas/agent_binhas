from agent import Agent
from tools import sum_calculator

TOOLS = {
    "sum_calculator": sum_calculator
}

agent = Agent(
    model="qwen3:8b",
    tools=TOOLS,
    system_prompt=(
        "You are a helpful AI assistant. "
        "Use sum_calculator whenever the user asks "
        "you to add numbers. "
        "Use previous conversation context only "
        "when relevant to the latest request."
    )
)

print("AI Agent ready! Type 'exit' to quit.")

while True:

    try:
        user_input = input("\nYou: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break

    if user_input.lower == "exit":
        print("Goodbye!")
        break

    if not user_input:
        continue


    answer = agent.ask(user_input)
    
    print(f"\nAgent: {answer}")