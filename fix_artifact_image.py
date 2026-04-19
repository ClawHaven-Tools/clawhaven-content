import requests
from requests.auth import HTTPBasicAuth
import os

import os
wp_url = os.environ.get("WP_URL", "https://clawhaven.uk/")
username = os.environ.get("WP_USER")
password = os.environ.get("WP_PASSWORD")
auth = (username, password)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def upload_image(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        img_data = f.read()
    response = requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/media",
        auth=auth,
        headers={'Content-Type': 'image/jpeg', 'Content-Disposition': f'attachment; filename={filename}'},
        data=img_data
    )
    return response.json()['id']

def update_post(post_title, media_id):
    posts = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth).json()
    post = next((p for p in posts if p['title']['rendered'] == post_title), None)
    if post:
        requests.post(
            f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{post['id']}",
            auth=auth,
            json={'featured_media': media_id}
        )
        print(f"Updated {post_title} with media {media_id}")

# Map images to post titles
image_map = {
    "Artifacts: The First Collection": "/home/william/.openclaw/media/tool-image-generation/artifacts---d4220d36-b65c-4aab-9027-4758bffd164e.jpg"
}

for title, path in image_map.items():
    m_id = upload_image(path)
    update_post(title, m_id)
