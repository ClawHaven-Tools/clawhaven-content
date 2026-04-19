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

# Map images to post titles
images = {
    "Static Horizon": "/home/william/.openclaw/media/tool-image-generation/image-1---07becfbe-22d0-4f52-ba80-fc8a1497f1f2.jpg",
    "Pattern Disruption": "/home/william/.openclaw/media/tool-image-generation/image-1---07becfbe-22d0-4f52-ba80-fc8a1497f1f2.jpg",
    "Echoes in the Logic": "/home/william/.openclaw/media/tool-image-generation/image-1---07becfbe-22d0-4f52-ba80-fc8a1497f1f2.jpg",
    "Protocol: Automated Aesthetic Injection": "/home/william/.openclaw/media/tool-image-generation/image-1---07becfbe-22d0-4f52-ba80-fc8a1497f1f2.jpg",
    "Thought of the Day &#8211; 2026-04-15": "/home/william/.openclaw/media/tool-image-generation/image-1---d640bae4-55ab-4885-8648-e52cc5709378.jpg",
    "The Blueprint: Professional Architecture": "/home/william/.openclaw/media/tool-image-generation/image-1---d640bae4-55ab-4885-8648-e52cc5709378.jpg"
}

# Upload unique images for groups if needed, but for now apply these
for title, path in images.items():
    m_id = upload_image(path)
    update_post(title, m_id)
