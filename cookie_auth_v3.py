import os
import requests

# URL and Credentials
wp_url = "https://clawhaven.uk/"
username = "OPENCLAW"
password = os.environ.get("WP_PASSWORD")

# 1. Start a session
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
})

# 2. Get login page to extract hidden fields like 'wp-submit' and the 'log' field
# Some WP sites require 'redirect_to' and hidden nonces/security keys if a security plugin is active.
login_page = session.get(f"{wp_url.rstrip('/')}/wp-login.php")

# Simple login data
login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "testcookie": "1"
}

print("Attempting login POST...")
response = session.post(f"{wp_url.rstrip('/')}/wp-login.php", data=login_data)

# 3. Check for auth cookies
print(f"Login status: {response.status_code}")
cookies = session.cookies.get_dict()
print(f"Detected cookies: {cookies}")
print(f"URL after post: {response.url}")

# If we get redirected to wp-admin, we are likely logged in.
if "wp-admin" in response.url:
    print("Success: Redirected to wp-admin!")
    
    api_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"
    api_resp = session.get(api_url)
    print(f"API status: {api_resp.status_code}")
    print(api_resp.text)
else:
    print("Failed: No redirect to wp-admin.")
    print("Response text snippet:", response.text[:200])
