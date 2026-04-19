import os
import requests

# URL and Credentials
wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

# 1. Try listing users without authentication (if permitted, to see if API works)
api_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users"

print(f"Attempting to list users from: {api_url}")
response = requests.get(api_url)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"User ID: {user.get('id')}, Username: {user.get('slug')}")
else:
    print(f"Response: {response.text}")
