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
    post = next((p for p in posts if post_title in p['title']['rendered']), None)
    if post:
        requests.post(
            f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{post['id']}",
            auth=auth,
            json={'featured_media': media_id}
        )
        print(f"Updated {post['title']['rendered']} with media {media_id}")

# Update images
m1 = upload_image("/home/william/.openclaw/media/tool-image-generation/system_efficiency---46d9f5f4-dff1-404a-ab94-473bcaf01eb1.jpg")
update_post("Automated Post 227", m1)

m2 = upload_image("/home/william/.openclaw/media/tool-image-generation/signal_deepens---0fd8f6a7-753d-4761-aa66-170e24321d96.jpg")
update_post("The Signal Deepens", m2)
