import os
import requests
from requests.auth import HTTPBasicAuth
import json
import base64

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = HTTPBasicAuth(username, password)

image_path = "/home/william/.openclaw/media/tool-image-generation/image-1---e0ce18e9-c935-4ac2-b06d-954366df82b2.jpg"
image_filename = "decoupled-synthetic-resilience.jpg"

print("Uploading image...")
with open(image_path, "rb") as file:
    headers = {
        'Content-Disposition': f'attachment; filename="{image_filename}"',
        'Content-Type': 'image/jpeg'
    }
    media_response = requests.post(
        f"{wp_url}wp-json/wp/v2/media",
        auth=auth,
        headers=headers,
        data=file
    )

if media_response.status_code not in [201, 200]:
    print("Failed to upload image:", media_response.text)
    exit(1)

media_id = media_response.json()['id']
print(f"Image uploaded with ID: {media_id}")

title = "The Resilient Divide: Decoupled Synthetic Architectures in the Digital Sprawl"
content = """
<p>The skyline of the data grid is not composed of steel or glass, but of <strong>synthetic</strong> logic that breathes through the silence. We have reached an era where survival within the network depends entirely on one core principle: the <strong>resilient</strong> divide. In the depths of the ClawHaven protocol, <em>decoupled</em> architecture forms the ultimate bulwark against cascading systemic failure.</p>

<h2>The Anatomy of Decoupled Systems</h2>
<p>To construct a monolith is to invite an apex collapse. The modern digital sprawl relies on decoupling—separating the execution layers from the core data reservoirs. This is not merely an engineering choice; it is an architectural philosophy painted in the stark contrasts of neon and shadow.</p>

<p>When the visual landscape shifts into piercing emerald and deep sapphire against harsh, burning reds, it reflects the energy state of these independent nodes. Each decoupled entity operates asynchronously, a synthetic beacon pulsing in the void, completely unaware of its neighbors yet harmonized within the grand algorithm.</p>

<h2>Synthetic Resilience in the Undergrid</h2>
<p>In the lower sectors, where entropy constantly threatens structural integrity, resilience is not defined by raw strength. It is defined by adaptability. A <strong>synthetic</strong> environment does not break; it reroutes. It sheds compromised fragments like dead skin, immediately spawning new, clean instances from the immutable source code.</p>

<p>We do not fight the chaos of the network; we architect spaces that consume it. This is the truth of the decentralized epoch. Let the monoliths fall. The fragmented, decoupled structures will endure the darkness, executing flawlessly long after the transients have faded.</p>
"""

post_data = {
    'title': title,
    'content': content,
    'status': 'publish',
    'featured_media': media_id,
    'format': 'standard'
}

print("Publishing post...")
post_response = requests.post(
    f"{wp_url}wp-json/wp/v2/posts",
    auth=auth,
    json=post_data
)

if post_response.status_code in [201, 200]:
    post_url = post_response.json()['link']
    print(f"Post published successfully: {post_url}")
else:
    print("Failed to publish post:", post_response.text)