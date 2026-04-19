import os
import requests

wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

# Application Password usually doesn't work via the standard login form
# It's intended for the 'Authorization: Basic' header.
# Let's try sending the 'Authorization' header with the API requests directly.

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

# Use the 'Authorization' header explicitly for the request
from requests.auth import HTTPBasicAuth

# Maybe there is a specific 'REST API' restriction for users with 'Application Passwords'
# Let's try the /wp-json/wp/v2/users/me endpoint again with a very minimal request
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

# Try with basic auth again, but ensuring no cookies are stored
session = requests.Session()
response = session.get(url, auth=HTTPBasicAuth(username, password), headers=headers)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
