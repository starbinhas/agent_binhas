from dotenv import load_dotenv

from groq import Groq

load_dotenv()

client = Groq()

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an AI agent is in one sentence."
        }
    ]
)

print(response.choices[0].message.content)