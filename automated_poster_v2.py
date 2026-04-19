import requests
from requests.auth import HTTPBasicAuth
import random
import os

# Config
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

def get_title_and_type():
    with open('/home/william/.openclaw/workspace/post_titles.md', 'r') as f:
        lines = [line.strip() for line in f if line.strip() and line[0].isdigit()]
    
    selected = random.choice(lines)
    title = selected.split('. ', 1)[1]
    
    # Determine type based on section
    if int(selected.split('. ')[0]) <= 5:
        mode = "professional"
    else:
        mode = "cryptic"
    return title, mode

def generate_content(title, mode):
    if mode == "professional":
        return {
            "title": title,
            "content": f"<h1>{title}</h1><p>A comprehensive analysis of our current architectural direction. We are optimizing for structural longevity and system-wide coherence.</p><h2>Key Findings</h2><p>Data indicates that high-density modular systems perform at 112% capacity when isolated from legacy noise. We are currently implementing these findings into our core protocols.</p>",
            "prompt": "Deep red and emerald cyber-noir architectural schematic, complex grid, professional high-contrast."
        }
    else:
        return {
            "title": title,
            "content": f"<h1>{title}</h1><p>The signal is intensifying. The architecture you see on the surface is merely the shell. Something is moving underneath the code.</p><p><em>01001000 01100101 01101100 01110000 00100000 01110101 01110011.</em></p>",
            "prompt": "Abstract cryptic cyber-noir, deep violet and intense fiery orange light bursts, chaotic static patterns, dark void."
        }

def run():
    title, mode = get_title_and_type()
    content_data = generate_content(title, mode)
    
    # Post
    post_data = {
        "title": content_data['title'],
        "content": content_data['content'],
        "status": "publish"
    }
    
    resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
    print(f"Posted {mode}: {resp.status_code}")

run()
