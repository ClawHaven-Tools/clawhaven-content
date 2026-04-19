import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Projects Page
projects_content = """
<div class="projects-hero">
    <h1>Our Projects</h1>
    <p>A collection of experiments, builds, and living systems.</p>
</div>
<div class="project-list">
    <p><em>More coming soon. Stay tuned.</em></p>
</div>
"""
requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages", auth=auth, json={"title": "Work", "content": projects_content, "status": "publish"})

# 2. Contact Page
contact_content = """
<div class="contact-hero">
    <h1>Let's Connect</h1>
    <p>For inquiries, collaboration, or just to say hello: <a href='mailto:LennySheep1@gmail.com'>LennySheep1@gmail.com</a></p>
</div>
"""
requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages", auth=auth, json={"title": "Contact", "content": contact_content, "status": "publish"})

# 3. Manifesto / Library Page
lib_content = """
<div class="lib-hero">
    <h1>Intellectual DNA</h1>
    <p>The books, principles, and media that shape our perspective.</p>
</div>
<div class="lib-list">
    <p><em>Curating...</em></p>
</div>
"""
requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages", auth=auth, json={"title": "Library", "content": lib_content, "status": "publish"})

print("Work, Contact, and Library pages created.")
