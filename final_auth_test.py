import base64
import requests
import os

# Updated credentials from .env
wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

# Format: username:password
auth_string = f"{username}:{password}"
auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# API endpoint
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Authorization": f"Basic {auth_encoded}"
}

# Request
response = requests.get(url, headers=headers)

print(f"Authentication response status: {response.status_code}")
print(response.text)

if response.status_code == 200:
    print("Success: Authenticated!")
    # Create page
    page_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages"
    data = {
        "title": "Wiki Test Page",
        "content": "<p>This is a test placeholder page created by OpenClaw.</p>",
        "status": "publish"
    }
    create_resp = requests.post(page_url, headers=headers, json=data)
    print(f"Creation response status: {create_resp.status_code}")
    print(create_resp.text)
