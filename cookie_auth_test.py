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

# 2. Login via the standard login page
login_url = f"{wp_url.rstrip('/')}/wp-login.php"
login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "testcookie": "1"
}

print(f"Attempting login to {login_url}...")
response = session.post(login_url, data=login_data)

# 3. Verify if we have session cookies
print(f"Login status: {response.status_code}")
if "wordpress_logged_in" in session.cookies.get_dict():
    print("Success: Logged in (cookies found)!")
    
    # 4. Try REST API using the session
    api_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"
    api_resp = session.get(api_url)
    print(f"API status: {api_resp.status_code}")
    print(api_resp.text)
else:
    print("Failed: No session cookies detected.")
    print("Response text snippet:", response.text[:500])
