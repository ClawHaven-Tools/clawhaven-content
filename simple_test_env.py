import os

def load_env(path):
    with open(path, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

load_env('/home/william/.openclaw/workspace/.env')

# Test environment access
print(f"WP_USER: {os.getenv('WP_USER')}")
print(f"Password Loaded: {'Yes' if os.getenv('WP_PASSWORD') else 'No'}")
