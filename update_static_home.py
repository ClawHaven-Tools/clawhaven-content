import os
import requests
from datetime import datetime

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Generate Quote
quote_content = "Simplicity is the ultimate sophistication."
quote_author = "A.I. Design Principle"
content_html = f"<div class='thought-hero'><blockquote class='thought-of-the-day'>{quote_content}</blockquote><cite>{quote_author}</cite></div>"

# 2. Get Home page ID
response = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages?slug=home", auth=auth)
pages = response.json()

if pages:
    page_id = pages[0]['id']
    # 3. Update the static Home page with the actual content
    page_data = {
        "content": content_html,
        "status": "publish"
    }
    requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages/{page_id}", auth=auth, json=page_data)
    print("Static Home page updated with daily thought!")
else:
    print("Home page not found.")
