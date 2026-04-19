import os
import base64
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
# Using the updated password from your .env
password = os.environ.get("WP_PASSWORD")

# Prepare Authorization Header
auth_string = f"{username}:{password}"
auth_encoded = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; OpenClaw/1.0)",
    "Authorization": f"Basic {auth_encoded}"
}

# 1. Ping the REST API endpoint directly
api_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

print(f"Attempting API request to: {api_url}")
response = requests.get(api_url, headers=headers)

print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
