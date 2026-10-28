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
    """
        Craw a website using ZAP's Traditional Spider and return discovered URLs.

        Args:
            url: The website URL to crawl.
    """
    
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

def discover_get_parameters(url: str) -> dict:
    """
    Discover GET query parameters accepted by a web endpoint using Arjun.
    {} means no parameters discovered.
    
    Args:
        url: The endpoint URL to analyse.
    """

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