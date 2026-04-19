import requests
import json
import os
from datetime import datetime

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# 1. Generate Quote using Gemini (using a simple local call or internal generate)
# I'll use a direct internal request for the quote to ensure it's generated, not scraped.
# Since I am the AI, I can generate the content directly.

quote_content = "The architect of the future is the one who understands that simplicity is the ultimate sophistication."
quote_author = "A.I. Design Principle"

thought_text = f"{quote_content} — {quote_author}"

# 2. Get/Create 'Thoughts' Category
categories_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/categories"
response = requests.get(categories_url, auth=auth)
categories = response.json()
thought_cat_id = next((c['id'] for c in categories if c['name'] == 'Thoughts'), None)

if not thought_cat_id:
    cat_data = {"name": "Thoughts", "slug": "thoughts"}
    response = requests.post(categories_url, auth=auth, json=cat_data)
    thought_cat_id = response.json()['id']

# 3. Create new post
post_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts"
post_data = {
    "title": f"Thought for {datetime.now().strftime('%Y-%m-%d')}",
    "content": f"<div class='thought-of-the-day'><blockquote>{quote_content}</blockquote><cite>{quote_author}</cite></div>",
    "status": "publish",
    "categories": [thought_cat_id]
}

response = requests.post(post_url, auth=auth, json=post_data)
print(f"Status: {response.status_code}")
if response.status_code == 201:
    print("Success: Post created!")
else:
    print(f"Error: {response.text}")
