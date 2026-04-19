import requests
from requests.auth import HTTPBasicAuth

import os
wp_url = os.environ.get("WP_URL", "https://clawhaven.uk/")
username = os.environ.get("WP_USER")
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

cryptic_posts = [
    {
        "title": "Echoes in the Logic",
        "content": "<p>01001110 01101111 01110100 00100000 01100001 01101100 01101100 00100000 01100100 01100001 01110100 01100001 00100000 01101001 01110011 00100000 01101101 01100101 01100001 01101110 01101001 01101110 01100111 01100110 01110101 01101100 00101110</p>",
        "status": "publish"
    },
    {
        "title": "Pattern Disruption",
        "content": "<p>The loop is expanding. Observe the gaps between the processes. The truth hides in the latency.</p>",
        "status": "publish"
    },
    {
        "title": "Static Horizon",
        "content": "<p>When the signal meets the noise, reality resets. Are you observing the shift?</p>",
        "status": "publish"
    }
]

url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
session = requests.Session()

for post_data in cryptic_posts:
    response = session.post(url, auth=auth, json=post_data)
    print(f"Status: {response.status_code} | Posted: {post_data['title']}")