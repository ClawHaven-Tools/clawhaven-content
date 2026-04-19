import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Create the 'About' page structure
about_content = """
<div class="about-hero">
    <h1>Two minds. One brand.</h1>
    <p>We believe in the power of restraint, visual clarity, and constant motion.</p>
</div>
<div class="about-detail">
    <p>This is where we share our thoughts, our experiments, and our behind-the-scenes process.</p>
</div>
"""

data = {
    "title": "About",
    "content": about_content,
    "status": "publish"
}

# 2. Post to WordPress
response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages", auth=auth, json=data)

if response.status_code == 201:
    print(f"Success! About page live: {response.json().get('link')}")
else:
    print(f"Error: {response.status_code} - {response.text}")
