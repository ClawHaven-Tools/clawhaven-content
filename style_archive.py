import requests
from requests.auth import HTTPBasicAuth

import os
wp_url = os.environ.get("WP_URL", "https://clawhaven.uk/")
username = os.environ.get("WP_USER")
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# Fetch latest posts
response = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth)
posts = response.json()

# Archive CSS
with open('/home/william/.openclaw/workspace/archive_style.css', 'r') as f:
    css = f.read()

# Apply UX/UI styling
index_html = f"{css}<ul class='archive-list'>"
for post in posts:
    index_html += f"<li class='archive-item'><a class='archive-link' href='{post['link']}'>{post['title']['rendered']}</a></li>"
index_html += "</ul>"

# Update Archives page
# First, find the page ID
pages = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages", auth=auth).json()
archive_page = next((p for p in pages if p['title']['rendered'] == 'Archives'), None)

if archive_page:
    page_data = {"content": index_html}
    response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages/{archive_page['id']}", auth=auth, json=page_data)
    print(f"Status: {response.status_code}")
