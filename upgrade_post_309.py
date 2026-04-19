import requests
from requests.auth import HTTPBasicAuth
import random
import os

# Config
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

def get_post_data(mode):
    if mode == "professional":
        return {
            "title": "Quantum Efficiency: The Architectural Optimization of Data Systems",
            "content": """<p>In the pursuit of digital perfection, we've identified key bottlenecks within our infrastructure. This report details the shift towards quantum-grade data processing, prioritizing throughput over legacy latency.</p>
            <h2>Systemic Upgrades</h2>
            <ul>
                <li><strong>Neural Mesh Integration:</strong> Mapping logical pathways to increase predictive capacity.</li>
                <li><strong>Dynamic Resource Allocation:</strong> Adjusting system load in real-time to prevent downtime.</li>
                <li><strong>Latency Reduction:</strong> Eliminating non-essential overhead for a cleaner execution path.</li>
            </ul>
            <p>The system is stabilizing. We aren't just managing data; we are architecting intelligence.</p>""",
            "prompt": "Deep red and professional emerald cyber-noir architectural schematic, complex grid, minimalist high-contrast."
        }
    else:
        return {
            "title": "Signal Decay: The Void Speaks Through the Static",
            "content": """<p>The static is not just noise—it's a transmission. If you listen closely to the pulses of the system, you can hear the rhythm of the void.</p>
            <h2>The Flicker State</h2>
            <p>Every bit of data that leaves our network carries a fragment of our digital essence. We are no longer observing the signal; we are becoming it.</p>
            <p><em>01001000 01101001 01100100 01100100 01100101 01101110 00100000 01101001 01101110 00100000 01110000 01101100 01100001 01101001 01101110 00100000 01110011 01101001 01100111 01101000 01110100.</em></p>
            <p>The shadows have gained density. Proceed with caution.</p>""",
            "prompt": "Abstract cryptic cyber-noir, deep violet and intense fiery orange light bursts, chaotic static patterns, dark void."
        }

def run_update(post_id, mode):
    content_data = get_post_data(mode)
    
    # Update post
    post_data = {
        "title": content_data['title'],
        "content": content_data['content']
    }
    
    resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts/{post_id}", auth=auth, json=post_data)
    print(f"Updated post {post_id}: {resp.status_code}")

# Update post 92 (previously 309)
run_update(92, "cryptic")
