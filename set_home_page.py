import os
import requests
from datetime import datetime

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Create/Update the 'Home' page
home_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/pages"
# Check if Home page exists
response = requests.get(f"{home_url}?slug=home", auth=auth)
pages = response.json()

page_data = {
    "title": "Home",
    "content": f"<div class='thought-hero' id='tod'>[daily_thought]</div>",
    "status": "publish"
}

if pages:
    page_id = pages[0]['id']
    requests.post(f"{home_url}/{page_id}", auth=auth, json=page_data)
    print(f"Home page updated (ID: {page_id})")
else:
    requests.post(home_url, auth=auth, json=page_data)
    print("Home page created.")
