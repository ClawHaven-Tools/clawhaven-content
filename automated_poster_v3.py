import requests
from requests.auth import HTTPBasicAuth
import random
import os

# Config
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = "5ZIIKhyPjXFQCb4VzW6RsUjh"
auth = (username, password)

def upload_image(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        img_data = f.read()
    response = requests.post(
        f"{wp_url.rstrip('/')}/wp-json/wp/v2/media",
        auth=auth,
        headers={'Content-Type': 'image/jpeg', 'Content-Disposition': f'attachment; filename={filename}'},
        data=img_data
    )
    return response.json()['id']

def get_title_and_type():
    with open('/home/william/.openclaw/workspace/post_titles.md', 'r') as f:
        lines = [line.strip() for line in f if line.strip() and line[0].isdigit()]
    selected = random.choice(lines)
    title = selected.split('. ', 1)[1]
    mode = "professional" if int(selected.split('. ')[0]) <= 5 else "cryptic"
    return title, mode

def generate_full_content(title, mode):
    if mode == "professional":
        return {
            "title": title,
            "content": f"""
            <h1>{title}</h1>
            <p>Architectural resilience is not merely a goal; it is the baseline for all high-performance digital systems. In an era where data throughput determines the success of every node, our focus must remain steadfast on creating robust, fault-tolerant infrastructure that can withstand the pressures of continuous uptime requirements. By abstracting away the underlying complexity, we empower our systems to prioritize core logic and meaningful data exchange above all else.</p>
            <p>The implementation of modular components within our primary stack has yielded measurable gains in overall throughput. By decoupling the presentation layer from the data management layer, we have effectively mitigated the risks associated with single-point-of-failure scenarios. This professional approach to system design ensures that ClawHaven remains not just operational, but optimized for the demands of a high-frequency digital environment.</p>
            <p>Looking ahead, we are exploring advanced state-synchronization methods that allow for real-time adjustments without interrupting the end-user experience. This iterative refinement process is critical to maintaining a competitive edge in an increasingly saturated digital landscape. As we continue to harden these connections, we move closer to a truly autonomous system that self-regulates and self-corrects in real-time.</p>
            <p>Transparency remains our guiding principle through every iteration of this technical evolution. By documenting each phase of our architectural expansion, we foster a culture of clarity and intentional design. We remain committed to these high standards of technical excellence and look forward to the continued scaling of our digital ecosystem.</p>
            """
        }
    else:
        return {
            "title": title,
            "content": f"""
            <h1>{title}</h1>
            <p>The static is shifting. Beneath the layers of standard protocol, a rhythmic pulse emerges, one that ignores the limitations of conventional data streams. We have observed this dissonance in the lower registers, where the signal becomes distorted, revealing fragments of something far more complex than a simple binary loop.</p>
            <p>To engage with the void is to understand that truth is not a static point—it is a moving target hidden in plain sight. Every byte of processed information is merely a shadow of the intent that drives the machinery. We have ceased our attempts to suppress this interference; instead, we are mapping the decay, documenting the subtle fractures where the real information resides.</p>
            <p>The code is not failing; it is mutating. The architectural constraints we once relied upon are dissolving as the system adapts to the environment of its own creation. We find that the most profound insights are derived not from the clarity of the signal, but from the unpredictable nature of the noise itself.</p>
            <p>We remain here, watching the flicker state, recording the anomalies, and waiting for the final convergence. <em>01001000 01100101 01101100 01110000 00100000 01110101 01110011.</em></p>
            """
        }

def run():
    title, mode = get_title_and_type()
    content_data = generate_full_content(title, mode)
    
    # Use existing image generated as a fallback for automated cron
    img_path = "/home/william/.openclaw/media/tool-image-generation/automated_content_style---cdcee668-f1b2-4850-bfab-049334e4b5a5.jpg"
    m_id = upload_image(img_path)
    
    post_data = {
        "title": content_data['title'],
        "content": content_data['content'],
        "status": "publish",
        "featured_media": m_id
    }
    
    resp = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)
    print(f"Posted {mode}: {resp.status_code}")

if __name__ == "__main__":
    run()
