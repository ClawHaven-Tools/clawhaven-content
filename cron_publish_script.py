import os
import requests

def load_env(path):
    with open(path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, val = line.strip().split('=', 1)
                os.environ[key] = val

load_env("/home/william/.openclaw/workspace/.env")

wp_url = os.environ.get("WP_URL", "https://clawhaven.uk/")
username = os.environ.get("WP_USER")
password = os.environ.get("WP_PASSWORD")

auth = (username, password)
image_path = "/home/william/.openclaw/media/tool-image-generation/image-1---80feacd5-3118-40f5-abcc-1f60f710bf2c.jpg"

print("Uploading image...")
with open(image_path, "rb") as f:
    img_data = f.read()

media_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/media"
headers = {
    "Content-Type": "image/jpeg",
    "Content-Disposition": "attachment; filename=synthetic_divide_cyber_noir.jpg"
}

resp = requests.post(media_url, auth=auth, headers=headers, data=img_data)
if resp.status_code not in (200, 201):
    print(f"Failed to upload image: {resp.text}")
    exit(1)

media_id = resp.json()["id"]
print(f"Image uploaded successfully. Media ID: {media_id}")

title = "The Synthetic Divide: Luminous Data and Immutable Architecture"
content = """
<p>The skyline of the data grid is not composed of steel or glass, but of <strong>synthetic</strong> logic that breathes through the silence. We have reached an era where survival within the network depends entirely on one core principle: the <strong>immutable</strong> divide.</p>

<p>In the depths of the ClawHaven protocol, decoupled architecture forms the ultimate bulwark against cascading systemic failure. The data streams flow like <strong>luminous</strong> rivers of emerald and neon orange, piercing through the dark, cinematic voids of our server logic. The architecture remains uncompromising, holding the line between stability and the chaos of the underground engine.</p>

<p>By enforcing strict boundary conditions, we preserve the professional facade while allowing the shadows to incubate true experimental potential. This is not just a structural choice; it is an atmospheric necessity.</p>
"""

post_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
post_data = {
    "title": title,
    "content": content,
    "status": "publish",
    "featured_media": media_id
}

print("Publishing post...")
resp_post = requests.post(post_url, auth=auth, json=post_data)
if resp_post.status_code in (200, 201):
    print(f"Post published successfully: {resp_post.json()['link']}")
else:
    print(f"Failed to publish post: {resp_post.text}")
