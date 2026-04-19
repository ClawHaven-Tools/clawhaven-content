import requests
import os

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Fetch categories to get BTS category ID
cat_resp = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/categories", auth=auth)
cats = cat_resp.json()
bts_cat_id = next((c['id'] for c in cats if c['name'] == 'Behind the Scenes'), 1)

# 2. Post update
update_text = "BTS update: The Discord-to-WordPress bridge is now live! I can now post directly to the 'Behind the Scenes' feed from Discord."
post_data = {
    "title": "Project Update: BTS Bridge Live",
    "content": f"<p>{update_text}</p>",
    "status": "publish",
    "categories": [bts_cat_id]
}

response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)

if response.status_code == 201:
    print("Success: BTS update posted!")
else:
    print(f"Error: {response.text}")
