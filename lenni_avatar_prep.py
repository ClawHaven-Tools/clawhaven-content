import requests
from requests.auth import HTTPBasicAuth
import os

wp_url = "https://clawhaven.uk/"
username = "Lenni"
password = os.environ.get("WP_PASSWORD")
auth = (username, password)

# WordPress doesn't have a direct REST API for updating profile pictures (avatars).
# Usually, this requires setting the Gravatar email or using a plugin.
# Since I cannot easily set the Gravatar, I will provide the image path and instructions
# to upload manually via the WordPress Dashboard -> Users -> Profile.

print("Avatar generated and ready for upload.")
print("File path: /home/william/.openclaw/media/tool-image-generation/lenni_profile---2e9461a4-7600-4eb0-8b16-ddd72203a5a7.jpg")
print("Action: Navigate to Users -> Profile in your WordPress dashboard to upload this image as the user avatar.")
