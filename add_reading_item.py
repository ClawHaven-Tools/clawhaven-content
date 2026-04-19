import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Create a "Reading" / "Inspiration" Library Item
post_data = {
    "title": "Currently Inspired By: The Art of Restraint",
    "content": "<p>We're looking closely at minimalist design and bold typography. Less is more, and the focus remains on the clarity of the message.</p>",
    "status": "publish",
    "categories": [] # Maybe create a 'Reading' category?
}

# 2. Post it
response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)

if response.status_code == 201:
    print(f"Reading update published: {response.json().get('link')}")
else:
    print(f"Error: {response.text}")
