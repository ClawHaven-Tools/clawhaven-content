import os
import requests

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")

post_data = {
    "title": "Artifacts: The First Collection",
    "content": "<h2>Professional Precision</h2><p>This is the first artifact in our collection, meticulously structured for stability and scale.</p>",
    "status": "publish"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

from requests.auth import HTTPBasicAuth

url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
session = requests.Session()
response = session.post(url, auth=HTTPBasicAuth(username, password), headers=headers, json=post_data)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")