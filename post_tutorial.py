import os
import requests

# Credentials
wp_url = "https://clawhaven.uk/"
username = "Lenni" # The actual WordPress user
password = os.environ.get("WP_PASSWORD") # App Password
auth = (username, password)

post_content = """
<h2>How We Automated Our Brand with AI and WordPress</h2>
<p>We wanted to move fast—"crazy mode" fast. We needed a system where AI could automatically publish content, manage our brand's "Thought of the Day," and bridge the gap between our internal workspace and our live WordPress site. Here is how we did it.</p>

<h3>The Winning Workflow</h3>
<ol>
    <li><strong>Application Passwords:</strong> We bypassed standard login forms entirely. In your WordPress Dashboard, go to <em>Users -> Profile</em> and scroll down to "Application Passwords." Generate one there.</li>
    <li><strong>The Authentication Secret:</strong> The most important lesson? The username you use for the REST API is <strong>your WordPress username</strong> (the one you log in with), NOT the "Application Password" name you give it.</li>
    <li><strong>The Header:</strong> We used Basic Authentication with the following format: <code>Authorization: Basic base64(username:password)</code>.</li>
</ol>

<h3>Troubleshooting (The Roadblocks)</h3>
<ul>
    <li><strong>403 Forbidden:</strong> This was our first wall. It was caused by the server's WAF (ModSecurity). If you see 403s, check your hosting firewall logs.</li>
    <li><strong>401 Unauthorized:</strong> This happened when we guessed the wrong username. Remember: use your primary WordPress username, even when using an App Password.</li>
    <li><strong>REST API Stripping:</strong> Some hosting environments strip the <code>Authorization</code> header. If that happens, you might need to add a rule to your <code>.htaccess</code> or Nginx config to pass it through.</li>
</ul>

<p>Now, our AI can push updates directly from Discord, and we never have to touch the WP Admin interface unless we want to.</p>
"""

post_data = {
    "title": "How We Built an AI-Driven Brand in Crazy Mode",
    "content": post_content,
    "status": "publish"
}

response = requests.post(f"{wp_url.rstrip('/')}/wp-json/wp/v2/posts", auth=auth, json=post_data)

if response.status_code == 201:
    print(f"Post Published: {response.json().get('link')}")
else:
    print(f"Error: {response.text}")
