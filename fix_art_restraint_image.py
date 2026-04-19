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

m_id = upload_image("/home/william/.openclaw/media/tool-image-generation/art_of_restraint---ca5ff35a-f971-4f25-940e-e4c86e2b3b3e.jpg")
requests.post(
    f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/35",
    auth=auth,
    json={'featured_media': m_id}
)
print(f"Updated post 35 with media {m_id}")
