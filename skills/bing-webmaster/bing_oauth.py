#!/usr/bin/env python3
"""
Bing Webmaster OAuth Handler
Two modes: Manual (copy/paste) or automatic callback

Usage: python3 bing_oauth.py
"""
import os
import sys
import time
import webbrowser
import requests

# ==================== UPDATE THESE ====================
CLIENT_ID = "YOUR_CLIENT_ID"       # Get from Bing Webmaster > API Access > OAuth
CLIENT_SECRET = "YOUR_CLIENT_SECRET"   # Get from Bing Webmaster > API Access > OAuth

# Optional: If you set up a real callback URL, use it here
# Otherwise, leave as None for manual mode
REDIRECT_URI = None  # Set to "https://your-site.com/callback" if you have one
# =====================================================

TOKEN_FILE = "/home/william/.openclaw/workspace/bing_oauth_code.txt"
ENV_FILE = "/home/william/.openclaw/.env"

# OAuth URLs
AUTH_URL_TEMPLATE = "https://www.bing.com/webmaster/oauth2/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope=webmaster&state=clawhaven"
TOKEN_URL = "https://www.bing.com/webmaster/oauth2/token"

def get_redirect_uri():
    """Get the redirect URI to use"""
    if REDIRECT_URI:
        return REDIRECT_URI
    else:
        # Use a non-working localhost - doesn't matter since we'll use manual mode
        return "http://localhost:9999/callback"

def check_for_code_file():
    """Check if auth code has been saved by callback"""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            code = f.read().strip()
        if code:
            os.remove(TOKEN_FILE)
            return code
    return None

def exchange_code_for_token(code):
    """Exchange auth code for access token"""
    redirect = get_redirect_uri()
    
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect
    }
    
    try:
        response = requests.post(TOKEN_URL, data=data, timeout=30)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            print(response.text[:500])
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_env_file(access_token, refresh_token=None):
    """Save tokens to .env file"""
    existing = {}
    
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if '=' in line and not line.startswith('#'):
                    k, v = line.split('=', 1)
                    existing[k] = v
    
    existing['BING_ACCESS_TOKEN'] = access_token
    if refresh_token:
        existing['BING_REFRESH_TOKEN'] = refresh_token
    
    with open(ENV_FILE, 'w') as f:
        f.write("# Bing Webmaster Credentials\n")
        for k, v in existing.items():
            f.write(f"{k}={v}\n")
    
    print(f"✅ Tokens saved to {ENV_FILE}")

def main():
    print("=" * 55)
    print("   BING WEBMASTER OAUTH SETUP")
    print("=" * 55)
    print()
    
    # Check for client ID
    if CLIENT_ID == "YOUR_CLIENT_ID":
        print("⚠️  STEP 1: Register OAuth app in Bing Webmaster")
        print("-" * 55)
        print("1. Go to: https://www.bing.com/webmasters")
        print("2. Sign in → Settings → API Access")  
        print("3. Click 'OAuth 2.0' → Register App")
        print("4. For Redirect URI, use any valid URL (we'll use manual)")
        print("5. Copy Client ID and Client Secret")
        print()
        print("Then edit this file and replace:")
        print("   CLIENT_ID = 'your_client_id'")
        print("   CLIENT_SECRET = 'your_client_secret'")
        print()
        print("Example redirect URI to enter in Bing:")
        print("   https://example.com/oauth/callback")
        print()
        sys.exit(1)
    
    redirect_uri = get_redirect_uri()
    auth_url = AUTH_URL_TEMPLATE.format(client_id=CLIENT_ID, redirect_uri=redirect_uri)
    
    print("⚠️  STEP 2: Authorize the application")
    print("-" * 55)
    print(f"Redirect URI: {redirect_uri}")
    print()
    
    # Check for automatic callback first
    code = check_for_code_file()
    if code:
        print("✅ Found auth code from callback!")
    else:
        print("Opening Bing OAuth in your browser...")
        webbrowser.open(auth_url)
        
        print("\n👤 Complete these steps:")
        print("   1. Sign in to Bing Webmaster (if prompted)")
        print("   2. Click 'Accept' to authorize")
        print("   3. You'll be redirected (may show error - that's OK)")
        print("   4. Copy the authorization code from the URL")
        print()
        print("   The URL will look like:")
        print("   https://example.com/oauth/callback?code=XXXXX&state=...")
        print()
        print("   Copy everything after 'code=' and before '&state='")
        print()
        
        code = input("Paste the authorization code here: ").strip()
    
    if not code:
        print("❌ No code provided")
        sys.exit(1)
    
    print("\n⚠️  STEP 3: Exchange code for token")
    print("-" * 55)
    print("Exchanging code for access token...")
    
    token_data = exchange_code_for_token(code)
    
    if token_data and 'access_token' in token_data:
        access_token = token_data['access_token']
        refresh_token = token_data.get('refresh_token')
        
        print(f"✅ Got access token!")
        
        # Save to .env
        update_env_file(access_token, refresh_token)
        
        print()
        print("=" * 55)
        print("   🎉 OAUTH SETUP COMPLETE!")
        print("=" * 55)
        print("You can now use the full Bing Webmaster API!")
        
    else:
        print("❌ Failed to get access token")
        if token_data:
            print(token_data)

if __name__ == '__main__':
    main()