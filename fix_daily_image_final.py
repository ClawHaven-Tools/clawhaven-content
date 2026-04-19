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

m_id = upload_image("/home/william/.openclaw/media/tool-image-generation/daily_build---15df1814-9771-4a0d-8d13-492dc4b30fa5.jpg")
requests.post(
    f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/38",
    auth=auth,
    json={'featured_media': m_id}
)
print(f"Updated post 38 with media {m_id}")
