import os

from dotenv import load_dotenv
from zapv2 import ZAPv2

load_dotenv()

apikey = os.environ["ZAP_API_KEY"]

zap = ZAPv2(
    apikey=apikey,
    proxies={
        "http": "http://127.0.0.1:8080",
        "https": "http://127.0.0.1:8080"
    }
)

print("ZAP version:", zap.core.version)

print("Know hosts:", zap.core.hosts)