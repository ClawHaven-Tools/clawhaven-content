import base64
import os

html_file = "/home/william/.openclaw/workspace/netlify-site/index.html"
img_file = "/home/william/.openclaw/media/tool-image-generation/favicon---b68d2649-fc07-4bd5-bddb-461306933460.jpg"

with open(img_file, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

with open(html_file, "r") as f:
    content = f.read()

content = content.replace("{{IMAGE_BASE64}}", encoded_string)

with open(html_file, "w") as f:
    f.write(content)
