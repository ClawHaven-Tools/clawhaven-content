#!/usr/bin/env python3
"""
Bing Keyword Tracker - Run via cron to track site keywords
Picks 3 random words, checks rankings, saves to file for title reference.
"""
import os
import random
import requests
import json
from datetime import datetime

SITE_URL = os.getenv('WP_URL', 'https://clawhaven.uk').rstrip('/')
ADJECTIVES_FILE = '/home/william/.openclaw/workspace/adjectives.md'
OUTPUT_FILE = '/home/william/.openclaw/workspace/keywords_tracked.json'

def load_adjectives():
    """Load noir adjectives from file"""
    if not os.path.exists(ADJECTIVES_FILE):
        return ['cryptic', 'digital', 'void', 'neural', 'pulse', 'protocol', 'entropy', 'kinetic']
    
    with open(ADJECTIVES_FILE, 'r') as f:
        lines = f.readlines()
    
    # Extract adjectives (skip headers, remove dashes)
    adjectives = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and line.startswith('-'):
            adj = line.lstrip('- ').strip()
            if adj:
                adjectives.append(adj)
    
    return adjectives if adjectives else ['cryptic', 'digital', 'void']

def check_keyword_ranking(keyword):
    """Check if keyword appears in Bing for our site"""
    search_url = f"https://www.bing.com/search?q={keyword}+site:{SITE_URL}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    
    try:
        response = requests.get(search_url, headers=headers, timeout=15)
        
        # Check if our site appears in results
        site_domain = SITE_URL.replace('https://', '').replace('http://', '')
        
        if site_domain in response.text:
            # Try to find position
            lines = response.text.split('\n')
            for i, line in enumerate(lines):
                if site_domain in line:
                    return {
                        'keyword': keyword,
                        'ranked': True,
                        'position': min(i // 3 + 1, 100),  # Rough estimate
                        'found': True
                    }
        
        return {
            'keyword': keyword,
            'ranked': False,
            'position': None,
            'found': False
        }
    except Exception as e:
        return {
            'keyword': keyword,
            'ranked': False,
            'error': str(e)
        }

def load_previous_results():
    """Load previous keyword tracking data"""
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f:
                return json.load(f)
        except:
            return {'keywords': [], 'last_updated': None}
    return {'keywords': [], 'last_updated': None}

def save_results(data):
    """Save keyword tracking data"""
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    print(f"[{datetime.now()}] Bing Keyword Tracker running...")
    
    # Load previous data
    data = load_previous_results()
    
    # Pick 3 random keywords
    adjectives = load_adjectives()
    selected = random.sample(adjectives, min(3, len(adjectives)))
    
    print(f"Checking keywords: {selected}")
    
    # Check each keyword
    results = []
    for kw in selected:
        result = check_keyword_ranking(kw)
        results.append(result)
        print(f"  - {kw}: ranked={result.get('ranked', False)}")
    
    # Update data
    data['keywords'] = results
    data['last_updated'] = datetime.now().isoformat()
    data['adjectives_used'] = selected
    
    # Also keep history
    if 'history' not in data:
        data['history'] = []
    
    data['history'].append({
        'timestamp': datetime.now().isoformat(),
        'keywords': selected,
        'results': results
    })
    
    # Keep last 30 entries
    if len(data['history']) > 30:
        data['history'] = data['history'][-30:]
    
    # Save
    save_results(data)
    print(f"Results saved to {OUTPUT_FILE}")
    print(f"Total tracked: {len(data.get('history', []))} checks")

if __name__ == '__main__':
    main()