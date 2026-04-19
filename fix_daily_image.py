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
    # Note: Using part of the title or matching as best as possible
    post = next((p for p in posts if 'Build for the Daily' in p['title']['rendered']), None)
    if post:
        requests.post(
            f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{post['id']}",
            auth=auth,
            json={'featured_media': media_id}
        )
        print(f"Updated {post['title']['rendered']} with media {media_id}")

m_id = upload_image("/home/william/.openclaw/media/tool-image-generation/daily_build---15df1814-9771-4a0d-8d13-492dc4b30fa5.jpg") # Note: corrected filename mapping if needed
update_post("Build for the Daily", m_id)
