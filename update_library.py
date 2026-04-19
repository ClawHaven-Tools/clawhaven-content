import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Fetch posts and generate a 'Library' content structure
response = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth)
posts = response.json()

# 2. Build Library HTML
lib_content = "<h2>Curated Principles</h2><ul>"
for post in posts[:5]:
    lib_content += f"<li><strong>{post['title']['rendered']}</strong> - <a href='{post['link']}'>Read</a></li>"
lib_content += "</ul>"

# 3. Find Library page and update it
page_resp = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages?slug=library", auth=auth)
pages = page_resp.json()

if pages:
    page_id = pages[0]['id']
    update_data = {"content": lib_content, "status": "publish"}
    requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages/{page_id}", auth=auth, json=update_data)
    print("Library page updated.")
else:
    print("Library page not found.")
