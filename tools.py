import os
import time
import json
import subprocess

from dotenv import load_dotenv
from zapv2 import ZAPv2
from tempfile import TemporaryDirectory
from pathlib import Path
from tempfile import TemporaryDirectory


def crawl_website(url: str) -> dict:
    
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
    )

    while int(zap.spider.status(scan_id)) < 100:    # is this good?
        print(f"web_crawler: {zap.spider.status(scan_id)}%")
        time.sleep(1)

    spider_urls = zap.spider.results(scan_id)
    observed_urls = zap.core.urls(baseurl=url)

    urls = sorted(set(spider_urls + observed_urls))

    if "http://localhost:3000/rest/products/search?q=" in urls:     # only for testing, remove later
        urls = urls[:49] + {"http://localhost:3000/rest/products/search?q="}

    return {
        "target": url,
        "total_urls": len(urls),
        "urls": urls
    }

def discover_get_parameters(url: str) -> dict:

    with TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "results.json"

        command = [
            "arjun",
            "-u", url,
            "-m", "GET",
            "-o", str(output_file)
        ]

        process = subprocess.run(command)

        if output_file.exists():
            return json.loads(output_file.read_text())

        return {}

def test_sql_injection(url: str, parameter: str) -> dict:
    
    with TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "sqlmap.json"

        command = [
            "sqlmap",
            "-u", url,
            "-p", parameter,
            "--level=3",
            "--risk=1",
            "--batch",
            "--report-json", str(output_file)
        ]

        subprocess.run(command)

        return json.loads(output_file.read_text())