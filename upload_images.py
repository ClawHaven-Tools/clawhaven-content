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
    
    media_headers = {
        'Content-Type': 'image/jpeg',
        'Content-Disposition': f'attachment; filename={filename}'
    }
    media_headers.update(headers)
    
    response = requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/media",
        auth=auth,
        headers=media_headers,
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

# Mapping images to post titles
image_map = {
    "Signal Noise: Underground Transmission 01": "/home/william/.openclaw/media/tool-image-generation/signal_noise---de854132-a9ce-42ba-9649-c79eed72b4cc.jpg",
    "The Void Protocol: Deep Analysis": "/home/william/.openclaw/media/tool-image-generation/void_protocol---e9b853e8-e2f7-4497-9011-3427ad248a3b.jpg",
    "Flicker State": "/home/william/.openclaw/media/tool-image-generation/flicker_state---67790902-ce02-4ac2-b9b5-062ff1ea05a9.jpg"
}

for title, path in image_map.items():
    m_id = upload_image(path)
    update_post(title, m_id)
    print(f"Updated {title} with media {m_id}")
