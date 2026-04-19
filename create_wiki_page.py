import os
import base64
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")

# Prepare Authorization Header
auth_string = f"{username}:{password}"
auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": f"Basic {auth_encoded}",
    "Content-Type": "application/json"
}

# 1. Create the Wiki page
page_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages"
data = {
    "title": "Wiki",
    "content": "<h2>Welcome to the Wiki</h2><p>This is a placeholder page for our project documentation.</p>",
    "status": "publish"
}

print(f"Attempting to create Wiki page at: {page_url}")
response = requests.post(page_url, headers=headers, json=data)

if response.status_code == 201:
    print("Success: Wiki page created!")
    print(f"URL: {response.json().get('link')}")
else:
    print(f"Error {response.status_code}: {response.text}")
