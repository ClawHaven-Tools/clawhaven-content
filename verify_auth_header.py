import requests
from requests.auth import HTTPBasicAuth

# Direct values
wp_url = "https://clawhaven.uk/"
username = "Lenni"
# The app password from the env
password = "DFxr6#" + chr(36) + "X9BB9Tp0EmYz8vrBi"

# API endpoint for users/me
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

# Using a standard Authorization header instead of HTTPBasicAuth,
# as some WP configs block basic auth directly on the REST API.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Authorization": "Basic " + "TGVubmk6REZ4cjYjJBY5QkI5VHAwRW1Zejh2ckJp" # This is Lenni:AppPassword encoded
}

# Try a simple GET to verify credentials
response = requests.get(url, headers=headers)

print(f"Authentication response status: {response.status_code}")
print(response.text)
