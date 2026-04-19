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

# 2. Get the login page to capture the login_form nonce or hidden fields
login_page = session.get(f"{wp_url.rstrip('/')}/wp-login.php")
# WordPress uses a 'redirect_to' and sometimes a hidden 'wp-submit' field. 
# Looking for a 'wp-login.php' form in the page might be too much, let's try the direct post.

# Login data
login_data = {
    "log": username,
    "pwd": password,
    "wp-submit": "Log In",
    "redirect_to": f"{wp_url.rstrip('/')}/wp-admin/",
    "testcookie": "1"
}

print("Attempting login...")
response = session.post(f"{wp_url.rstrip('/')}/wp-login.php", data=login_data)

# 3. Check for auth cookies in the response
print(f"Login status: {response.status_code}")
cookies = session.cookies.get_dict()
print(f"Detected cookies: {cookies}")

if any("wordpress_logged_in" in key for key in cookies):
    print("Success: Logged in!")
    
    # 4. Try REST API using the session
    # Note: Need the X-WP-Nonce header for REST API requests when using cookie auth
    api_url = f"{wp_url.rstrip('/')}/wp-json/wp/v2/users/me"
    
    # Get nonce
    nonce_resp = session.get(f"{wp_url.rstrip('/')}/wp-json/")
    nonce = nonce_resp.headers.get("X-WP-Nonce")
    
    headers = {"X-WP-Nonce": nonce} if nonce else {}
    
    api_resp = session.get(api_url, headers=headers)
    print(f"API status: {api_resp.status_code}")
    print(api_resp.text)
else:
    print("Failed: No session cookies detected.")
