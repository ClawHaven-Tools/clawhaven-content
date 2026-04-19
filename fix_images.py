import requests
from requests.auth import HTTPBasicAuth
import os

wp_url = "https://clawhaven.uk/"
username = "Lenni"
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

image_map = {
    "Static Horizon": "/home/william/.openclaw/media/tool-image-generation/static_horizon---91e1f296-bb46-45ad-a5e9-5b1fd3659513.jpg",
    "Pattern Disruption": "/home/william/.openclaw/media/tool-image-generation/pattern_disruption---2d865664-929a-4602-b7d3-2c79767569f0.jpg",
    "Echoes in the Logic": "/home/william/.openclaw/media/tool-image-generation/echoes_in_the_logic---6ba44a1d-eeb0-4e0e-a2ae-f3bcbc4c7553.jpg",
    "Protocol: Automated Aesthetic Injection": "/home/william/.openclaw/media/tool-image-generation/automated_injection---db0a4513-94e8-4ea6-a196-74d32c7f87e4.jpg",
    "Thought of the Day &#8211; 2026-04-15": "/home/william/.openclaw/media/tool-image-generation/thought_of_the_day---b313e29c-5d84-4405-a0d2-fce7521223a0.jpg",
    "The Blueprint: Professional Architecture": "/home/william/.openclaw/media/tool-image-generation/the_blueprint---8c6530ec-ab90-45e7-a04c-0ffcd9f933ae.jpg"
}

for title, path in image_map.items():
    m_id = upload_image(path)
    update_post(title, m_id)
