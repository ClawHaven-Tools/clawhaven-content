import requests
from requests.auth import HTTPBasicAuth
import os

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

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

m_id = upload_image("/home/william/.openclaw/media/tool-image-generation/signal_decay---ff94cff8-26ce-4d77-b808-1778f474d2d2.jpg")
requests.post(
    f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/92",
    auth=auth,
    json={'featured_media': m_id}
)
print(f"Updated post 92 image with media {m_id}")
