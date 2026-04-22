#!/usr/bin/env python3
"""
Bing Webmaster Tools - URL Inspection & Quick Check
Uses Bing's public URL inspection when API isn't available.
"""
import os
import requests
import urllib.parse

BING_API_KEY = os.getenv('BING_WEBMASTER', '')
SITE_URL = os.getenv('WP_URL', 'https://clawhaven.uk').rstrip('/')

def inspect_url(url):
    """Check if a URL is indexed in Bing"""
    search_url = f"https://www.bing.com/search?q=site:{url}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
    }
    
    try:
        response = requests.get(search_url, headers=headers, timeout=15)
        
        if url.replace('https://', '') in response.text:
            return {
                'url': url,
                'indexed': True,
                'method': 'search-check'
            }
        else:
            return {
                'url': url,
                'indexed': False,
                'method': 'search-check'
            }
    except Exception as e:
        return {'error': str(e)}

def quick_health_check():
    """Quick site health check via sitemap and robots"""
    results = {}
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    # Check sitemap
    try:
        sm_resp = requests.get(f"{SITE_URL}/sitemap.xml", headers=headers, timeout=10)
        results['sitemap'] = {
            'exists': sm_resp.status_code == 200,
            'status': sm_resp.status_code
        }
    except Exception as e:
        results['sitemap'] = {'error': str(e)}
    
    # Check robots
    try:
        robots_resp = requests.get(f"{SITE_URL}/robots.txt", headers=headers, timeout=10)
        results['robots'] = {
            'exists': robots_resp.status_code == 200,
            'status': robots_resp.status_code
        }
    except Exception as e:
        results['robots'] = {'error': str(e)}
    
    # Check a few key pages
    pages = ['/', '/about', '/library']
    results['pages'] = {}
    for page in pages:
        try:
            p_resp = requests.get(f"{SITE_URL}{page}", headers=headers, timeout=10)
            results['pages'][page] = {
                'status': p_resp.status_code,
                'accessible': p_resp.status_code == 200
            }
        except Exception as e:
            results['pages'][page] = {'error': str(e)}
    
    return results

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: bing_quick.py <health|inspect> [url]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'health':
        result = quick_health_check()
    elif command == 'inspect':
        url = sys.argv[2] if len(sys.argv) > 2 else SITE_URL
        result = inspect_url(url)
    else:
        result = {'error': 'Unknown command'}
    
    import json
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()