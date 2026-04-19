import requests
from requests.auth import HTTPBasicAuth
import os
import random

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = HTTPBasicAuth(username, password)

def get_three_adjectives():
    with open('/home/william/.openclaw/workspace/adjectives.md', 'r') as f:
        words = [line.strip().replace('- ', '') for line in f if line.strip() and line.startswith('- ')]
    return random.sample(words, 3)

adj = get_three_adjectives()
title = f"Cyber-Noir Architecture: {adj[0].capitalize()}, {adj[1].capitalize()}, and {adj[2].capitalize()}"

content = f"""
<!-- wp:paragraph -->
<p>In the depths of modern network design, we encounter the <strong>{adj[0].lower()}</strong> void—a space where conventional logic frays and raw data takes precedence. The cyber-noir reality demands that our infrastructure be not only robust but fundamentally <strong>{adj[1].lower()}</strong> in its core architecture, weaving through the digital shadows with an unwavering focus on uptime and performance.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">The Architecture of the Void</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Our emergent systems no longer rely on brittle legacy frameworks. By embracing high-contrast, decentralized methodologies, we engineer networks that are fiercely <strong>{adj[2].lower()}</strong> against the entropy of the modern web. Red, orange, emerald, and blue data streams pulse asynchronously through decoupled nodes, illuminating the dark web of enterprise routing.</p>
<!-- /wp:paragraph -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>“When the protocol fails, the architecture prevails.”</p></blockquote>
<!-- /wp:quote -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Executing the 'Crazy Mode' Protocol</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Under the 'Crazy Mode' protocol, hesitation is a vulnerability. We push code into the void with calculated precision, understanding that every {adj[0].lower()} log entry is a stepping stone to a more perfected, glitch-resistant state. This is not just system administration; it is atmospheric orchestration at scale.</p>
<!-- /wp:paragraph -->
"""

image_path = "/home/william/.openclaw/media/tool-image-generation/image-1---a4e1ed44-fe01-4f4a-9c5c-458ca40715d3.jpg"

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
    if response.status_code == 201:
        return response.json()['id']
    else:
        print("Image upload failed:", response.text)
        return None

print("Uploading image...")
media_id = upload_image(image_path)
print(f"Media ID: {media_id}")

post_data = {
    "title": title,
    "content": content,
    "status": "publish",
    "featured_media": media_id
}

resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
if resp.status_code == 201:
    print(f"Successfully posted: {resp.json().get('link')}")
    print(f"Title: {title}")
else:
    print(f"Failed to post: {resp.text}")
