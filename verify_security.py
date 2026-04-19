import requests
from requests.auth import HTTPBasicAuth
import os

# Manual load .env
def load_env(path='/home/william/.openclaw/workspace/.env'):
    if os.path.exists(path):
        with open(path, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value

load_env()
wp_url = os.environ.get("WP_URL", "https://clawhaven.uk/")
username = os.environ.get("WP_USER")
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

m_id = upload_image("/home/william/.openclaw/media/tool-image-generation/verification_test---c270577d-9cd7-44c3-80fa-20891dcdd18b.jpg")

post_data = {
    "title": "Protocol Verification: System Status Nominal",
    "content": "<p>Transmission successful. The automated pipeline is verified and operational using the updated security protocol.</p><p>All layers—professional facade and experimental underground—are synchronized.</p>",
    "status": "publish",
    "featured_media": m_id
}

resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
print(f"Post success: {resp.status_code}")
