import os
import requests
from requests.auth import HTTPBasicAuth

wp_url = "https://clawhaven.uk/"
username = "Lenni"
# App password
password = "DFxr6#" + chr(36) + "X9BB9Tp0EmYz8vrBi"

# Adding headers to look like a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"Testing authentication for user: {username} with headers...")

# API endpoint
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"

# POST request
try:
    response = requests.get(url, auth=HTTPBasicAuth(username, password), headers=headers)
    
    if response.status_code == 200:
        print("Success: Authenticated as:", response.json().get('name'))
        # Now try to create the page
        page_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages"
        data = {
            "title": "Wiki Test Page",
            "content": "<p>This is a test placeholder page created by OpenClaw.</p>",
            "status": "publish"
        }
        create_resp = requests.post(page_url, auth=HTTPBasicAuth(username, password), headers=headers, json=data)
        if create_resp.status_code == 201:
            print("Page created successfully!")
        else:
            print(f"Error creating page: {create_resp.status_code}")
            print(create_resp.text)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Exception: {e}")
