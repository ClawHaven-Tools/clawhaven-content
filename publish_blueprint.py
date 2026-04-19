import os
import requests
from requests.auth import HTTPBasicAuth

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")

post_data = {
    "title": "The Blueprint: Professional Architecture",
    "content": "<h1>The Blueprint</h1><p>Architecting the future with precision, transparency, and intent.</p><h2>Phase 01: Foundations</h2><p>Establishing stable infrastructure and core communication protocols.</p><h2>Phase 02: Integration</h2><p>Scaling modular systems and inter-service synchronicity.</p><h2>Phase 03: Expansion</h2><p>Deploying autonomous adaptive layers for peak performance.</p>",
    "status": "publish"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
session = requests.Session()
response = session.post(url, auth=HTTPBasicAuth(username, password), headers=headers, json=post_data)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")