import requests
from requests.auth import HTTPBasicAuth

# Direct values to ensure no env issues
wp_url = "https://clawhaven.uk/"
username = "Lenni"
# The app password
password = "DFxr6#" + chr(36) + "X9BB9Tp0EmYz8vrBi"

# API endpoint
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Try a simple GET to verify credentials
response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

print(f"Authentication response status: {response.status_code}")
print(response.text)
