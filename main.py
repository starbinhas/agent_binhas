from agent import Agent
from tools import crawl_website, discover_get_parameters

TOOLS = {
    "crawl_website": crawl_website,
    "discover_get_parameters": discover_get_parameters
}

orchestrator = Agent(
    model="qwen3:8b",
    tools={},
    system_prompt=(
        "You coordinates WAPT and report findings. "
        "If there is no more potential vulnerabilities, outputs 'exit'."
    )
)

worker = Agent(
    model="qwen3:8b",
    tools=TOOLS,
    system_prompt=(
        "You are a autonomous WAPT agent. "
        "You should try to exploit any potential vulnerabilities and report results back. "
        "Use the crawl_website tool to enumerate endpoints. "
        "Use the discover_get_parameters tool to enumerate parameters in GET endpoints."
    )
)

prompt = input("\nAgent Binhas is ready! Enter a prompt:\n")

while True:

    prompt = orchestrator.ask(prompt)
    print(f"\n[orchestrator]: {prompt}")

    if prompt == "exit":
        break

    prompt = worker.ask(prompt)
    print(f"[worker]: {prompt}")

print("\n...End of WAPT...")