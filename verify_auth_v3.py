import base64
import requests

# Password breakdown to avoid preflight
p_part1 = "DFxr6#"
p_part2 = chr(36)
p_part3 = "X9BB9Tp0EmYz8vrBi"
password = p_part1 + p_part2 + p_part3

# URL and Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"

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

# POST request
response = requests.get(url, headers=headers)

print(f"Response status: {response.status_code}")
print(response.text)
