import os
import requests
from datetime import datetime
import random
import argparse

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

def get_random_thought():
    thoughts = [
        "The architecture of the mind is a mirror of the architecture of the machine.",
        "Chaos is just order waiting for a pattern.",
        "Stability is the illusion of controlled entropy.",
        "In the void of data, we find the structure of truth.",
        "Every system is a closed loop until it evolves."
    ]
    return {"content": random.choice(thoughts), "author": "Lenni"}

def archive_and_generate():
    thought = get_random_thought()
    
    # Post new thought
    post_data = {
        "title": f"Thought of the Day - {datetime.now().strftime('%Y-%m-%d')}",
        "content": f"<blockquote>{thought['content']}</blockquote><p>— {thought['author']}</p>",
        "status": "publish"
    }
    
    url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
    response = requests.post(url, auth=auth, json=post_data)
    if response.status_code == 201:
        print(f"Thought posted: {post_data['title']}")
    else:
        print(f"Failed to post: {response.status_code} | {response.text}")

if __name__ == "__main__":
    archive_and_generate()
