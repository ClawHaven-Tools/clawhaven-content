import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Fetch the latest thought post
post_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts?categories=1&per_page=1" # Assumes ID 1 for 'Thoughts' or similar
# Let's find the 'Thoughts' category ID first to be safe
cat_resp = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/categories", auth=auth)
cats = cat_resp.json()
thought_id = next((c['id'] for c in cats if c['name'] == 'Thoughts'), 1)

# Fetch the post content
posts_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts?categories={thought_id}&per_page=1"
response = requests.get(posts_url, auth=auth)
latest_post = response.json()[0]

# 2. Update the post content to include the 'thought-hero' wrapper class
update_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{latest_post['id']}"
new_content = f"<div class='thought-hero'>{latest_post['content']['rendered']}</div>"
update_data = {"content": new_content}

update_resp = requests.post(update_url, auth=auth, json=update_data)

if update_resp.status_code == 200:
    print("Success: Updated the post with hero class!")
else:
    print(f"Error updating post: {update_resp.status_code}")
