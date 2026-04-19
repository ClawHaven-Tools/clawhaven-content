import os
import requests
import re

wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

login_page = session.get(f"{wp_url.rstrip('/')}/wp-login.php")
# Manual extraction of hidden fields
input_pattern = re.compile(r'<input[^>]*name=["\']([^"\']+)["\'][^>]*value=["\']([^"\']*)["\']')
hidden_fields = dict(input_pattern.findall(login_page.text))

login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "testcookie": "1"
}
login_data.update(hidden_fields)

print(f"Submitting form with fields: {list(login_data.keys())}")

response = session.post(f"{wp_url.rstrip('/')}/wp-login.php", data=login_data)

print(f"Status: {response.status_code}")
print(f"URL after POST: {response.url}")
print(f"Cookies: {session.cookies.get_dict()}")
