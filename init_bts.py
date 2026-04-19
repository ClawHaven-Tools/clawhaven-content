import os
import requests
from datetime import datetime

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Ensure 'Behind the Scenes' category exists
cat_resp = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/categories", auth=auth)
cats = cat_resp.json()
bts_cat_id = next((c['id'] for c in cats if c['name'] == 'Behind the Scenes'), None)

if not bts_cat_id:
    cat_data = {"name": "Behind the Scenes", "slug": "behind-the-scenes"}
    response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/categories", auth=auth, json=cat_data)
    bts_cat_id = response.json()['id']

# 2. Create the function to post an update
def post_bts(title, content):
    post_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
    post_data = {
        "title": title,
        "content": content,
        "status": "publish",
        "categories": [bts_cat_id]
    }
    response = requests.post(post_url, auth=auth, json=post_data)
    return response

# 3. Create a dynamic 'Project Status' indicator
def get_project_stats():
    # Placeholder for project metrics (posts count, last update)
    posts_resp = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth)
    count = len(posts_resp.json())
    return f"Active project posts: {count}. Last sync: {datetime.now().strftime('%Y-%m-%d %H:%M')}"

# Create initial status post
status = get_project_stats()
post_bts("Initial Project Status", f"<div class='project-status'>{status}</div>")

print("Behind the Scenes category ready and status post created.")
