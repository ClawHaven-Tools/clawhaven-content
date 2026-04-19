import os
import requests
from bs4 import BeautifulSoup

wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

# Get login form
login_page = session.get(f"{wp_url.rstrip('/')}/wp-login.php")
soup = BeautifulSoup(login_page.text, 'html.parser')

# Find form hidden inputs
login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "testcookie": "1"
}
for input_tag in soup.find_all('input'):
    if input_tag.get('name') and input_tag.get('value'):
        login_data[input_tag['name']] = input_tag['value']

# Correct field mapping for form submission
login_data['log'] = username
login_data['pwd'] = password
login_data['wp-submit'] = "Log In"

print(f"Submitting form data: {login_data.keys()}")

# POST login
response = session.post(f"{wp_url.rstrip('/')}/wp-login.php", data=login_data)

print(f"Status: {response.status_code}")
print(f"URL: {response.url}")
print(f"Cookies: {session.cookies.get_dict()}")
