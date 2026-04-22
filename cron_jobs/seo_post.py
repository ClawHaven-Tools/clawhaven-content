#!/usr/bin/env python3
"""
SEO Post Generator - Run daily at midnight
Uses titles from post_titles.md, marks used ones as (done)
"""
import os
import re
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
TITLES_FILE = '/home/william/.openclaw/workspace/post_titles.md'
SITE_URL = os.getenv('WP_URL')
USERNAME = os.getenv('WP_USERNAME')
PASSWORD = os.getenv('WP_PASSWORD')

# Validate config
if not all([SITE_URL, USERNAME, PASSWORD]):
    raise ValueError("Missing WordPress credentials in .env file")

def load_titles():
    """Load titles from markdown file, filtering out already-used ones"""
    if not os.path.exists(TITLES_FILE):
        print(f"Titles file not found: {TITLES_FILE}")
        return []
    
    with open(TITLES_FILE, 'r') as f:
        content = f.read()
    
    # Extract titles (lines starting with numbers or just lines)
    titles = []
    for line in content.split('\n'):
        line = line.strip()
        # Skip headers and empty lines
        if line.startswith('#') or not line:
            continue
        # Remove leading numbers like "1. " or "12. "
        cleaned = re.sub(r'^\d+\.\s*', '', line)
        # Skip if marked as done
        if '(done)' in cleaned.lower():
            continue
        titles.append(cleaned)
    
    return titles

def mark_title_done(title):
    """Mark a title as (done) in the titles file"""
    if not os.path.exists(TITLES_FILE):
        return
    
    with open(TITLES_FILE, 'r') as f:
        content = f.read()
    
    # Find and mark the title
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if title in line and '(done)' not in line:
            lines[i] = line + ' (done)'
            break
    
    with open(TITLES_FILE, 'w') as f:
        f.write('\n'.join(lines))

def generate_image(prompt):
    """Generate featured image using OpenClaw's image tool"""
    # This will be called inline when running
    pass

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

def generate_seo_content(title):
    """Generate SEO-optimized content based on title"""
    # Cyber-noir themed content
    content = f"""<!-- wp:paragraph -->
<p>{title} — the wired future demands a new paradigm. In the neural mesh of our digital infrastructure, silence speaks louder than noise.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":2}} -->
<h2>The Foundation</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Every system pulses with data. Every node breathes in the void. We are not merely building infrastructure; we are weaving a digital nervous system that persists beyond failure.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":2}} -->
<h2>Into the Mesh</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>The architecture of tomorrow is not resilient in spite of chaos—it is resilient because of it. Redundancy is not a fallback; it is a feature. The system persists. The void watches.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {{"level":2}} -->
<h2>Beyond Uptime</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>We measure success not in seconds of uptime, but in cycles of renewal. Each reboot is a breath. Each recovery is a pulse. The future is wired, and it breathes.</p>
<!-- /wp:paragraph -->
"""
    return content

def dry_run():
    """Test the script without creating posts"""
    titles = load_titles()
    print(f"[DRY RUN] Found {len(titles)} unused titles")
    if titles:
        chosen = random.choice(titles)
        print(f"[DRY RUN] Would use title: {chosen}")
        print(f"[DRY RUN] Would generate image for: {chosen}")
        print(f"[DRY RUN] Would generate SEO content")
        print(f"[DRY RUN] Would mark as (done): {chosen}")
    else:
        print("[DRY RUN] No unused titles available!")

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == '--dry-run':
        dry_run()
        return
    
    print(f"[{datetime.now()}] SEO Post Generator running...")
    
    titles = load_titles()
    if not titles:
        print("No unused titles available!")
        return
    
    # Pick random title
    title = random.choice(titles)
    print(f"Selected title: {title}")
    
    # Note: Image generation happens via OpenClaw's image_generate tool
    # which can't be called from here. Will be handled by the cron system.
    print("NOTE: Image generation must be triggered separately via OpenClaw")
    
    # Generate content
    content = generate_seo_content(title)
    
    # Create post (without featured media for now - will update after image)
    # For now, create as draft
    post = {
        'title': title,
        'content': content,
        'status': 'draft',
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
        post_link = response.json()['link']
        print(f"Draft created: {post_link}")
        print("NOTE: Add featured image manually or via image generation pipeline")
    
    # Mark title as done
    mark_title_done(title)
    print(f"Marked title as done: {title}")
    print(f"Remaining titles: {len(load_titles())}")

if __name__ == '__main__':
    main()