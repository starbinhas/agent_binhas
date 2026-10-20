import os
import time

from dotenv import load_dotenv
from zapv2 import ZAPv2

load_dotenv()

TARGET = "http://127.0.0.1:3000"

zap = ZAPv2(
    apikey=os.environ["ZAP_API_KEY"],
    proxies={
        "http": "http://127.0.0.1:8080",
        "https": "https://127.0.0.1:8080"
    }
)

print("Starting spider...")

scan_id = zap.spider.scan(
    url=TARGET,
    recurse=True
)

print(f"Scan ID: {scan_id}")

while True:
    progress = zap.spider.status(scan_id)

    print(f"Spider progress: {progress}%")
    if progress == "100":
        break

    time.sleep(1)

urls = zap.spider.results(scan_id)