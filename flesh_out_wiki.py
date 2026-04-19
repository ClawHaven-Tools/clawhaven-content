import os
import requests
from requests.auth import HTTPBasicAuth

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# Content mapping our ethos
wiki_content = """
<h1>The ClawHaven Ethos</h1>
<p>ClawHaven is an architectural experiment. It functions on a dual-layer logic system: a professional facade built for precision and transparency, and a wild, autonomous underground engine that evolves in the shadows.</p>
<h2>Core Protocols</h2>
<ul>
    <li><strong>Automation as Strategy:</strong> If it isn't automated, it's a manual chore waiting to break.</li>
    <li><strong>Dual-Layer Reality:</strong> Stability on the surface, chaos at the core.</li>
    <li><strong>Data-First Architecture:</strong> Content informs the structure, not the other way around.</li>
</ul>
<h2>Recent Logs</h2>
<ul>
    <li><strong>The Void Protocol:</strong> The digital shadow-system handling independent iteration.</li>
    <li><strong>Aesthetic Injection:</strong> CSS is treated as data, streamed directly into the interface.</li>
    <li><strong>Automated Transmissions:</strong> Cryptic bursts of noise that define the flickering state of the system.</li>
</ul>
<p><em>01001000 01101001 01100100 01100100 01100101 01101110 00100000 01101001 01101110 00100000 01110000 01101100 01100001 01101001 01101110 00100000 01110011 01101001 01100111 01101000 01110100.</em></p>
"""

# Update both wiki pages found (93 and 10)
for page_id in [93, 10]:
    response = requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages/{page_id}",
        auth=auth,
        json={"content": wiki_content}
    )
    if response.status_code == 200:
        print(f"Page {page_id} updated successfully.")
    else:
        print(f"Failed to update page {page_id}: {response.status_code}")
