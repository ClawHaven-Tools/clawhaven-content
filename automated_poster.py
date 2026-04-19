import requests
from requests.auth import HTTPBasicAuth
import random
import os

# Config
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def get_last_type():
    # Helper to track state in a simple file
    if os.path.exists('state_last_type.txt'):
        with open('state_last_type.txt', 'r') as f:
            return f.read().strip()
    return "cryptic" # Start with professional if we want, but let's toggle

def toggle_type(last):
    new = "professional" if last == "cryptic" else "cryptic"
    with open('state_last_type.txt', 'w') as f:
        f.write(new)
    return new

def generate_content(mode):
    if mode == "professional":
        return {
            "title": "System Efficiency Update: " + str(random.randint(100, 999)),
            "content": "<p>Optimizing workflow infrastructure for maximum throughput. System stability remains at 99.9%.</p>",
            "prompt": "Professional cyber-noir tech abstract, glowing emerald and electric blue, high contrast, clean minimalist machine grid, dark void background."
        }
    else:
        return {
            "title": "Anomaly Detected: " + str(random.randint(1000, 9999)),
            "content": "<p>The static is whispering again. Are you listening? 01010111 01000101 00100000 01000001 01010010 01000101 00100000 01001000 01000101 01010010 01000101.</p>",
            "prompt": "Cyber-noir glitch art, chaotic digital noise, vibrant red and orange flickering embers on a deep dark background, abstract and cryptic."
        }

def run():
    mode = toggle_type(get_last_type())
    content_data = generate_content(mode)
    
    # 1. Generate Image
    # Note: Use a placeholder for the actual generator or invoke the tool
    # For automated script: skip complex generation, assume we have a way
    
    # Actually posting...
    post_data = {
        "title": content_data['title'],
        "content": content_data['content'],
        "status": "publish"
    }
    
    # Post
    resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
    print(f"Posted {mode}: {resp.status_code}")

run()
