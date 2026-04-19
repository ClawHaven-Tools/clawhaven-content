import os
import requests
from requests.auth import HTTPBasicAuth

# Config
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# Fetch all posts to build an internal linking graph
posts = requests.get(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth).json()

# Simple internal linking strategy: link latest 3 posts in the content of the current post
for post in posts[:3]:
    # Construct link snippet for other recent posts
    links = "<div class='internal-links'><h3>Related Transmissions</h3><ul>"
    for other in posts[1:4]:
        if other['id'] != post['id']:
            links += f"<li><a href='{other['link']}'>{other['title']['rendered']}</a></li>"
    links += "</ul></div>"
    
    # Update post
    content = post['content']['rendered'] + links
    requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{post['id']}",
        auth=auth,
        json={'content': content}
    )
    print(f"Updated internal links for post: {post['title']['rendered']}")
