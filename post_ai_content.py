import os
import requests
from requests.auth import HTTPBasicAuth
import json

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

with open('/home/william/.openclaw/workspace/post_content.json', 'r') as f:
    content_data = json.load(f)

post_data = {
    "title": content_data['title'],
    "content": content_data['content'],
    "status": "publish"
}

resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
print(f"Posted AI content: {resp.status_code}")
