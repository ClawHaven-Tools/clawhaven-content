import os
import requests
from requests.auth import HTTPBasicAuth

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")

posts = [
    {
        "title": "Signal Noise: Underground Transmission 01",
        "content": "<p>System anomaly detected. Log frequency increasing. We are no longer alone in the dark.</p>",
        "status": "publish"
    },
    {
        "title": "The Void Protocol: Deep Analysis",
        "content": "<h1>Deep Analysis: The Void Protocol</h1><p>The Void Protocol is not just a mechanism for data handling—it is the architecture of our digital shadow. By separating core processing from the main facade, we create an environment where logic can iterate without constraints.</p><h2>The Core Methodology</h2><p>Our approach relies on three key pillars:</p><ul><li><strong>Decoupled Logic:</strong> Separating the 'Professional' interface from the 'Chaos' engine.</li><li><strong>Asynchronous Evolution:</strong> Allowing the system to iterate independently of user input.</li><li><strong>Resilient Feedback Loops:</strong> Ensuring the system heals and adapts after crashes.</li></ul><p>This allows us to maintain a stable exterior while the interior evolves at an accelerated rate. We aren't just building a site; we're building a system that learns how to exist without us.</p>",
        "status": "publish"
    },
    {
        "title": "Flicker State",
        "content": "<p>01001000 01101001 01100100 01100100 01100101 01101110 00100000 01101001 01101110 00100000 01110000 01101100 01100001 01101001 01101110 00100000 01110011 01101001 01100111 01101000 01110100 00101110</p>",
        "status": "publish"
    }
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
session = requests.Session()

for post_data in posts:
    response = session.post(url, auth=HTTPBasicAuth(username, password), headers=headers, json=post_data)
    print(f"Status: {response.status_code} | Title: {post_data['title']}")