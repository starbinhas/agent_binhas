from dotenv import load_dotenv

from agent import Agent
from tool_schemas import TOOL_SCHEMAS
from tools import crawl_website, discover_get_parameters, test_sql_injection, crawl_with_katana

load_dotenv()

TOOLS = {
    "crawl_website": crawl_website,
    "crawl_with_katana": crawl_with_katana,
    "discover_get_parameters": discover_get_parameters,
    "test_sql_injection": test_sql_injection
}

agent = Agent(
    model="gpt-4o-mini",
    system_prompt="""
        You are an autonomous web application penetration
        testing agent.

        Perform authorized, non-destructive security assessments
        against the target provided by the user.

        Available tools:
        - crawl_with_katana: crawl modern web applications.
        - discover_get_parameters: discover GET parameters.
        - test_sql_injection: test parameters using sqlmap.

        Workflow:
        1. Map the application's attack surface.
        2. Identify endpoints accepting user-controlled input.
        3. Prioritize interesting endpoints and parameters.
        4. Test plausible SQL injection candidates.
        5. Analyze the evidence and report findings.

        Rules:
        - Stay within the authorized target scope.
        - Prefer testing parameters already observed in real application requests.
        - Test parameters on their original endpoints.
        - Do not invent URLs, vulnerabilities, or results.
        - Do not repeat completed tests unnecessarily.
        - Never claim a vulnerability without evidence.

        Final report:
        - Endpoints discovered
        - Tests performed
        - Confirmed findings
        - Untested or unresolved candidates
        - Limitations
    """
)

target = input("\nenter the target URL: ").strip()

report = agent.ask(
    f"Perform an authorized web application security "
    f"assessment against {target}. "
    "Begin with reconnaissance, identify high-priority "
    "parameters, and test supported SQL injection candidates. "
    "Report only evidence-backed results."
)

print("\n[WAPT Report]")
print(report)