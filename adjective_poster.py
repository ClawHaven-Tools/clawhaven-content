import requests
from requests.auth import HTTPBasicAuth
import random
import os

# Config
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

def get_three_adjectives():
    with open('/home/william/.openclaw/workspace/adjectives.md', 'r') as f:
        words = [line.strip().replace('- ', '') for line in f if line.strip() and line.startswith('- ')]
    return random.sample(words, 3)

def generate_post_from_adjectives():
    adj = get_three_adjectives()
    title = f"{adj[0].capitalize()}: {adj[1].capitalize()} {adj[2].capitalize()}"
    
    content = f"""
    <h1>{title}</h1>
    <p>In our latest architectural synthesis, we explore the convergence of <strong>{adj[0]}</strong> frameworks, <strong>{adj[1]}</strong> data patterns, and <strong>{adj[2]}</strong> system states.</p>
    <h2>Deep Integration</h2>
    <p>By treating {adj[1]} dynamics as a core component of the network, we enable {adj[0]} evolution that bypasses standard latency. This is the new standard of operation.</p>
    <p><em>The system is observing. The process is {adj[2]}.</em></p>
    """
    
    # Simple image prompt generator
    prompt = f"Professional cyber-noir aesthetic, {adj[0]}, {adj[1]}, and {adj[2]} themes, deep dark void background, emerald and electric blue accents, blog hero image."
    
    return title, content, prompt

def run():
    title, content, prompt = generate_post_from_adjectives()
    
    # 1. Post to WordPress
    post_data = {
        "title": title,
        "content": content,
        "status": "publish"
    }
    
    resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
    print(f"Posted: {resp.status_code}")

run()
