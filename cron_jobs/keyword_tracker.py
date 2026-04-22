#!/usr/bin/env python3
"""
Bing Keyword Tracker - Enhanced version with better ranking detection
Picks random adjectives, checks Bing rankings, saves history.
"""
import os
import random
import requests
import json
import re
from datetime import datetime

SITE_URL = os.getenv('WP_URL', 'https://clawhaven.uk').rstrip('/')
ADJECTIVES_FILE = '/home/william/.openclaw/workspace/adjectives.md'
OUTPUT_FILE = '/home/william/.openclaw/workspace/keywords_tracked.json'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

def load_adjectives():
    """Load noir adjectives from file"""
    if not os.path.exists(ADJECTIVES_FILE):
        return ['cryptic', 'digital', 'void', 'neural', 'pulse', 'protocol', 'entropy', 'kinetic']
    
    with open(ADJECTIVES_FILE, 'r') as f:
        lines = f.readlines()
    
    adjectives = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and line.startswith('-'):
            adj = line.lstrip('- ').strip()
            if adj:
                adjectives.append(adj)
    
    return adjectives if adjectives else ['cryptic', 'digital', 'void']

def get_bing_results(keyword):
    """Get Bing search results for keyword + site"""
    search_url = f"https://www.bing.com/search?q={keyword}+site:{SITE_URL.replace('https://', '')}"
    
    try:
        response = requests.get(search_url, headers=HEADERS, timeout=15)
        html = response.text
        
        domain = SITE_URL.replace('https://', '').replace('http://', '').split('/')[0]
        
        # Find positions where our domain appears
        positions = []
        lines = html.split('\n')
        pos = 0
        for i, line in enumerate(lines):
            if domain in line:
                # Estimate position based on result blocks
                positions.append(i // 3 + 1)
        
        if positions:
            return {
                'keyword': keyword,
                'ranked': True,
                'best_position': min(positions) if positions else None,
                'total_appearances': len(positions),
                'domain': domain
            }
        else:
            return {
                'keyword': keyword,
                'ranked': False,
                'best_position': None,
                'total_appearances': 0
            }
            
    except Exception as e:
        return {'keyword': keyword, 'error': str(e)}

def get_site_indexed_count():
    """Get total pages indexed in Bing"""
    search_url = f"https://www.bing.com/search?q=site:{SITE_URL.replace('https://', '')}"
    
    try:
        response = requests.get(search_url, headers=HEADERS, timeout=15)
        html = response.text
        
        # Look for "About X results"
        match = re.search(r'About ([\d,]+) results', html)
        if match:
            return int(match.group(1).replace(',', ''))
        
        # Alternative pattern
        match = re.search(r'([\d,]+) results?', html)
        if match:
            return int(match.group(1).replace(',', ''))
            
    except:
        pass
    
    return None

def load_history():
    """Load previous tracking data"""
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, 'r') as f:
                return json.load(f)
        except:
            return {'keywords': [], 'history': []}
    return {'keywords': [], 'history': []}

def save_data(data):
    """Save tracking data"""
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Bing Keyword Tracker")
    
    # Get site index count
    indexed = get_site_indexed_count()
    print(f"Indexed pages in Bing: {indexed or 'Unknown'}")
    
    # Load adjectives
    adjectives = load_adjectives()
    selected = random.sample(adjectives, min(3, len(adjectives)))
    print(f"Checking: {', '.join(selected)}")
    
    results = []
    for kw in selected:
        result = get_bing_results(kw)
        results.append(result)
        status = f"Ranked #{result.get('best_position', '?')}" if result.get('ranked') else "Not ranked"
        print(f"  - {kw}: {status}")
    
    # Save to history
    data = load_history()
    data['indexed_pages'] = indexed
    data['last_check'] = datetime.now().isoformat()
    data['keywords'] = results
    data['adjectives_used'] = selected
    
    # Add to history
    if 'history' not in data:
        data['history'] = []
    
    data['history'].append({
        'timestamp': datetime.now().isoformat(),
        'keywords': selected,
        'results': results,
        'indexed': indexed
    })
    
    # Keep last 30
    if len(data['history']) > 30:
        data['history'] = data['history'][-30:]
    
    save_data(data)
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()