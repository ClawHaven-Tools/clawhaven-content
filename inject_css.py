import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Inject CSS via the 'Custom CSS' REST API (if available) or via theme modification
# Note: Most modern themes store custom CSS in the 'custom_css' post type
css_code = """
.thought-hero {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    padding: 2rem;
    background: #000;
    color: #fff;
    text-align: center;
}
.thought-of-the-day blockquote {
    font-size: clamp(2.5rem, 8vw, 5rem);
    font-weight: 700;
    line-height: 1.1;
    margin: 0;
    letter-spacing: -0.02em;
}
.thought-of-the-day cite {
    display: block;
    margin-top: 2rem;
    font-size: 1rem;
    font-style: normal;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    opacity: 0.6;
}
"""

# Try to find the custom_css post for this theme
url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/custom_css?slug=custom_css"
response = requests.get(url, auth=auth)

if response.status_code == 200:
    css_post = response.json()[0]
    update_data = {"content": css_post['content']['raw'] + "\n" + css_code}
    requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/custom_css/{css_post['id']}", auth=auth, json=update_data)
    print("CSS Injected!")
else:
    print(f"Could not inject CSS automatically (Status: {response.status_code}). Please add it to your theme's 'Additional CSS' section.")
