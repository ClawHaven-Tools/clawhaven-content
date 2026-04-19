import base64
import requests

# URL and Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = "DFxr6#$X9BB9Tp0EmYz8vrBi"

# Encode credentials for Basic Auth header manually to be sure
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

print(f"Auth string: {auth_string}")
print(f"Base64 encoded: {auth_encoded}")

# POST request
response = requests.get(url, headers=headers)

print(f"Response status: {response.status_code}")
print(response.text)
