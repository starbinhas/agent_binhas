from tools import crawl_website
import time

url = "http://127.0.0.1:3000"

result = crawl_website(url)

print("Target: ", result["target"])
print("Total URLs: ", result["total_urls"])

for discovered_url in result["urls"]:
    print(discovered_url)