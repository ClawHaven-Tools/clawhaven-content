import requests
from requests.auth import HTTPBasicAuth
import os

import os
wp_url = os.environ.get("WP_URL", "https://clawhaven.uk/")
username = os.environ.get("WP_USER")
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# WordPress Favicon is usually 'site_icon' in options
# We can update it via the 'wp/v2/settings' endpoint if accessible
# or upload as media first and then set it.

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

media_id = upload_image("/home/william/.openclaw/media/tool-image-generation/favicon---b68d2649-fc07-4bd5-bddb-461306933460.jpg")

# Update site icon setting
response = requests.post(
    f"{wp_url.rstrip('/')}/wp-json/wp/v2/settings",
    auth=auth,
    json={'site_icon': media_id}
)

if response.status_code == 200:
    print(f"Favicon updated successfully with media {media_id}")
else:
    print(f"Failed to update favicon: {response.status_code} | {response.text}")
