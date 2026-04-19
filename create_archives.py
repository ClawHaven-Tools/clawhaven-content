import os
import requests
from requests.auth import HTTPBasicAuth

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# Fetch latest posts
response = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth)
posts = response.json()

# Create a 'Post Index' page content
index_html = "<h1>Underground Archives</h1><ul>"
for post in posts:
    index_html += f"<li><a href='{post['link']}'>{post['title']['rendered']}</a></li>"
index_html += "</ul>"

# Post or Update the Index page
page_data = {
    "title": "Archives",
    "content": index_html,
    "status": "publish",
    "type": "page"
}

response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages", auth=auth, json=page_data)
print(f"Status: {response.status_code}")