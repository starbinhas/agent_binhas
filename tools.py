import os
import time

from dotenv import load_dotenv
from zapv2 import ZAPv2

def sum_calculator(a: float, b: float) -> float:
    return a + b

def crawl_website(url: str) -> list:
    
    load_dotenv()   # this seens wrong

    zap = ZAPv2(
        apikey=os.environ["ZAP_API_KEY"],
        proxies={
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080"
        }
    )

    scan_id = zap.spider.scan(
        url=url,
        recurse=True,
        subtreeonly=True,
        maxchildren=10
    )

    while int(zap.spider.status(scan_id)) < 100:    # is this good?
        print(f"web_crawler: {zap.spider.status(scan_id)}%")
        time.sleep(1)

    urls = zap.spider.results(scan_id)

    return {
        "target": url,
        "total_urls": len(urls),
        "urls": urls,
    }