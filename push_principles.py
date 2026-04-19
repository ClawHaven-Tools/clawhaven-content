import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Extrapolate Principles
principles = [
    {"title": "Restraint as Strategy", "content": "When in doubt, subtract. Decorative chrome is the enemy of intent."},
    {"title": "Content-First Architecture", "content": "Design is just a vehicle for ideas. If the content isn't strong, no amount of layout will save it."},
    {"title": "Build for the Daily", "content": "A system is only as good as its daily habit. If it isn't automated, it's just a manual chore waiting to break."}
]

# 2. Post as a 'Manifesto' set
for p in principles:
    post_data = {
        "title": p['title'],
        "content": f"<div class='principle'>{p['content']}</div>",
        "status": "publish",
        "categories": [] # Should probably link to a Manifesto category
    }
    requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)

print("Principles pushed live.")
