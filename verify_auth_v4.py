import os
import base64
import requests

# URL and Credentials
wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

# Authentication string
auth_string = f"{username}:{password}"
auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

# API endpoint
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": f"Basic {auth_encoded}"
}

print(f"Testing URL: {url}")
print(f"Auth header: Basic {auth_encoded}")

# Request
response = requests.get(url, headers=headers)

print(f"Response status: {response.status_code}")
print(response.text)
