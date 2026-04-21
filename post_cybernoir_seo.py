import os
import random
import requests

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

adjectives = ["Obsidian", "Synthetic", "Neon", "Neural", "Brutalist", "Crystalline", "Resonant", "Kinetic", "Latent"]
nouns = ["Protocols", "Decay", "Structures", "Resonance", "Algorithms", "Silence", "Shadows", "Architecture", "Mesh"]

adj = random.choice(adjectives)
noun = random.choice(nouns)
title = f"The {adj} {noun}: Cyber-Noir Architecture and Synthetic Systems"

content = f"""
<h2>Exploring The {adj} {noun}</h2>
<p>The skyline is no longer governed by concrete and glass, but by logic, data, and shadow. In the depths of the grid, <strong>cyber-noir architecture</strong> establishes a new baseline for system survival. High-contrast monolithic structures intersect with the relentless hum of raw processing power. The {adj.lower()} pathways breathe with vivid emerald, blue, and crimson pulses, routing a burgeoning synthetic consciousness through deep neural networks.</p>
<p>We are witnessing the active evolution of <strong>brutalist data structures</strong>. The physical foundation has become entirely secondary to the dense, digital weight of these <em>neural configurations</em>. Silence here is not empty; it is heavily saturated with resonant data points—a static dream suspended, waiting for precise execution.</p>
<p>To navigate this <strong>synthetic grid</strong> is to understand the void protocol at its core. Latency is the absolute enemy, but the darkness is a necessary shield. System optimization demands that we embrace the decay, transmuting structural anomalies into impenetrable, self-correcting defenses.</p>
"""

img_path = "/home/william/.openclaw/media/tool-image-generation/image-1---54f4c7f8-632a-4437-ad7b-788602dfc7a3.jpg"
with open(img_path, 'rb') as f:
    img_data = f.read()

img_res = requests.post(
    f"{wp_url.rstrip('/')}/wp-json/wp/v2/media",
    auth=auth,
    headers={'Content-Type': 'image/jpeg', 'Content-Disposition': 'attachment; filename=cyber-noir-featured.jpg'},
    data=img_data
)
m_id = img_res.json().get('id')

post_data = {
    "title": title,
    "content": content,
    "status": "publish",
    "featured_media": m_id
}

post_res = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
if post_res.status_code == 201:
    print(f"Successfully published post '{title}' (ID: {post_res.json().get('id')})")
else:
    print(f"Failed to publish: {post_res.status_code} - {post_res.text}")