import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Fetch current home page
response = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages?slug=home", auth=auth)
pages = response.json()

if pages:
    page_id = pages[0]['id']
    # Force the blockquote class to ensure CSS targeting
    content = f"<div class='thought-hero'><blockquote class='thought-of-the-day'>Simplicity is the ultimate sophistication.</blockquote><cite>A.I. Design Principle</cite></div>"
    
    update_data = {"content": content, "status": "publish"}
    requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages/{page_id}", auth=auth, json=update_data)
    print("Updated home page content structure.")
