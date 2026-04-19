import os
import requests
import random
from dotenv import load_dotenv

# Load variables from .env
load_dotenv('/home/william/.openclaw/workspace/.env')

wp_url = os.getenv("WP_URL")
username = os.getenv("WP_USER")
password = os.getenv("WP_PASSWORD")
auth = (username, password)

# ... existing code ...
def run():
    # Verify we actually have the password
    if not password:
        print("Error: WP_PASSWORD not found in environment!")
        return

    # Rest of the logic...
    print("Environment verified.")

if __name__ == "__main__":
    run()
