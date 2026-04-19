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

def update_post(post_id, media_id):
    requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{post_id}",
        auth=auth,
        json={'featured_media': media_id}
    )
    print(f"Updated post {post_id} with media {media_id}")

image_map = {
    108: "/home/william/.openclaw/media/tool-image-generation/kinetic_void---6ae736fd-0bcd-42e0-991c-50e4bac3eeee.jpg",
    107: "/home/william/.openclaw/media/tool-image-generation/fragmented_architectural---8ed6c91e-3203-4254-9cc9-9eae3485db3f.jpg",
    106: "/home/william/.openclaw/media/tool-image-generation/layer_two---23585faa-4f64-43cc-9ea2-0ba8734fb291.jpg",
    104: "/home/william/.openclaw/media/tool-image-generation/void_protocol_data---0d8536ac-7149-45f9-aae0-dc29ffff567d.jpg"
}

for post_id, path in image_map.items():
    m_id = upload_image(path)
    update_post(post_id, m_id)
