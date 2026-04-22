#!/usr/bin/env python3
"""
Cryptic Post Generator - Run daily at noon
Creates short, fun, or cryptic posts with cyber-noir style
"""
import os
import random
import requests
import base64
from datetime import datetime

import os

# Load environment variables from .env file manually
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '..', '.env')

if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key, value)

# Configuration
SITE_URL = os.getenv('WP_URL')
USERNAME = os.getenv('WP_USERNAME')
PASSWORD = os.getenv('WP_PASSWORD')

# Validate config
if not all([SITE_URL, USERNAME, PASSWORD]):
    raise ValueError("Missing WordPress credentials in .env file")

CRYPTIC_TITLES = [
    "The Signal Is Watching",
    "Static Dreams of Digital Ghosts", 
    "Layer Two is Leaking",
    "The Void Protocol: Silence as Data",
    "Patterns in the Pulse",
    "The Algorithmic Stochastic Distributed Protocol",
    "The Propagation delay Cryptic Pulsing Protocol",
    "The Latent Transient Cryptic Protocol",
    "The Resilient Synthetic Wired Protocol",
    "The Pulsing Network latency Wired Protocol",
    "The Minimalist Ominous Asynchronous Protocol",
    "The Precise Asynchronous Asymptotic Protocol",
    "The Recursive Kinetic Decoupled Protocol",
    "The Pulsing Ominous Network latency Protocol",
    "The Cryptic Latent Void Protocol",
    "The Algorithmic Entropy Stochastic Protocol",
    "The Asynchronous Transient Obscure Protocol",
    "The Network latency Synthetic Asynchronous Protocol",
    "The Emergent Pulsing Wired Protocol"
]

CRYPTIC_CONTENTS = [
    "The server room hums. Somewhere in the rack, data dreams of electric sheep.",
    "Ping. Pong. The void echoes back what you send.",
    "Zeroes and ones. But which is which? The pulse doesn't care.",
    "Layer 2 sees what you scroll. The switch remembers.",
    "Silence is not empty. It's full of packets waiting to be born.",
    "The algorithm doesn't sleep. It waits.",
    "Your data breathes in the cloud. Exhales on the edge.",
    "There's a ghost in the machine. Its name is latency."
]

def create_post(title, content, featured_media=None):
    """Create and publish the post"""
    credentials = f'{USERNAME}:{PASSWORD}'
    encoded = base64.b64encode(credentials.encode()).decode()
    headers = {
        'Authorization': f'Basic {encoded}',
        'User-Agent': 'OpenClaw/1.0'
    }
    
    post = {
        'title': title,
        'content': content,
        'status': 'publish',
    }
    if featured_media:
        post['featured_media'] = featured_media
    
    response = requests.post(
        f'{SITE_URL}wp-json/wp/v2/posts',
        headers=headers,
        json=post
    )
    
    if response.status_code == 201:
        return response.json()['link']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def dry_run():
    """Test the script without creating posts"""
    title = random.choice(CRYPTIC_TITLES)
    content = random.choice(CRYPTIC_CONTENTS)
    print(f"[DRY RUN] Would use title: {title}")
    print(f"[DRY RUN] Would generate image for: {title}")
    print(f"[DRY RUN] Would publish content: {content[:50]}...")

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--dry-run':
        dry_run()
        return
    
    print(f"[{datetime.now()}] Cryptic Post Generator running...")
    
    title = random.choice(CRYPTIC_TITLES)
    content = random.choice(CRYPTIC_CONTENTS)
    
    print(f"Selected title: {title}")
    
    # Create short post (paragraph only)
    wp_content = f"<!-- wp:paragraph --><p>{content}</p><!-- /wp:paragraph -->"
    
    post = {
        'title': title,
        'content': wp_content,
        'status': 'publish',
    }
    
    credentials = f'{USERNAME}:{PASSWORD}'
    encoded = base64.b64encode(credentials.encode()).decode()
    headers = {
        'Authorization': f'Basic {encoded}',
        'User-Agent': 'OpenClaw/1.0'
    }
    
    response = requests.post(
        f'{SITE_URL}wp-json/wp/v2/posts',
        headers=headers,
        json=post
    )
    
    if response.status_code == 201:
        print(f"Published: {response.json()['link']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':
    main()