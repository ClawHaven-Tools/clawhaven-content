import os
import requests
from requests.auth import HTTPBasicAuth

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = "DFxr6#" + chr(36) + "X9BB9Tp0EmYz8vrBi"

url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

data = {
    "title": "Wiki Test Page",
    "content": "<p>This is a test placeholder page created by OpenClaw.</p>",
    "status": "publish"
}

response = requests.post(url, auth=HTTPBasicAuth(username, password), headers=headers, json=data)

print(f"Response status: {response.status_code}")
print(response.text)
