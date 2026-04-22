#!/usr/bin/env python3
"""
Bing Webmaster Tools Skill
Provides keyword research, crawl stats, and site diagnostics.
"""
import os
import json
import requests
from datetime import datetime, timedelta

# Load Bing API key from environment
BING_API_KEY = os.getenv('BING_WEBMASTER', '')
SITE_URL = os.getenv('WP_URL', 'https://clawhaven.uk').rstrip('/')

# Bing Webmaster API Base URL
BING_API_BASE = "https://www.bing.com/webmasters/api"

def get_headers():
    return {
        'Api-Key': BING_API_KEY,
        'Content-Type': 'application/json',
        'Origin': 'https://www.bing.com',
        'Referer': 'https://www.bing.com/webmasters'
    }

def get_site_url_encoded():
    """URL encode the site URL for API calls"""
    import urllib.parse
    return urllib.parse.quote(SITE_URL, safe='')

def get_keywords(limit=20):
    """Get keyword performance data"""
    if not BING_API_KEY:
        return {"error": "BING_WEBMASTER key not set in .env"}
    
    # Bing Webmaster Keywords API
    url = f"{BING_API_BASE}/KeywordService/GetKeywords"
    
    payload = {
        "siteUrl": SITE_URL,
        "filters": {
            "language": "en",
            "device": "All"
        },
        "orderBy": "Impressions",
        "orderDirection": "Desc",
        "offset": 0,
        "pageSize": limit
    }
    
    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            keywords = data.get('Keywords', [])
            
            results = []
            for kw in keywords:
                results.append({
                    'keyword': kw.get('Keyword', ''),
                    'impressions': kw.get('Impressions', 0),
                    'clicks': kw.get('Clicks', 0),
                    'ctr': round(kw.get('ClickThroughRate', 0) * 100, 2),
                    'position': round(kw.get('AveragePosition', 0), 1)
                })
            return {
                'status': 'ok',
                'site': SITE_URL,
                'keywords': results,
                'total': len(results)
            }
        else:
            return {"error": f"API error: {response.status_code}", "detail": response.text[:200]}
    except Exception as e:
        return {"error": str(e)}

def get_crawl_errors():
    """Get crawl error reports"""
    if not BING_API_KEY:
        return {"error": "BING_WEBMASTER key not set in .env"}
    
    url = f"{BING_API_BASE}/CrawlSettings/GetCrawlErrors"
    
    payload = {
        "siteUrl": SITE_URL
    }
    
    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            
            errors = data.get('CrawlErrors', [])
            warnings = data.get('CrawlWarnings', [])
            
            return {
                'status': 'ok',
                'site': SITE_URL,
                'errors': errors[:20],  # Limit to 20
                'warnings': warnings[:20],
                'error_count': len(errors),
                'warning_count': len(warnings)
            }
        else:
            return {"error": f"API error: {response.status_code}", "detail": response.text[:200]}
    except Exception as e:
        return {"error": str(e)}

def get_site_stats():
    """Get overall site health and indexing stats"""
    if not BING_API_KEY:
        return {"error": "BING_WEBMASTER key not set in .env"}
    
    url = f"{BING_API_BASE}/SiteService/GetSiteStats"
    
    payload = {
        "siteUrl": SITE_URL
    }
    
    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            return {
                'status': 'ok',
                'site': SITE_URL,
                'indexed_pages': data.get('IndexedPages', 'Unknown'),
                'crawled_pages': data.get('CrawledPages', 'Unknown'),
                'pending_urls': data.get('PendingURLs', 0),
                'last_crawl': data.get('LastCrawlDate', 'Unknown'),
                'crawl_rate': data.get('CrawlRate', 'Unknown')
            }
        else:
            return {"error": f"API error: {response.status_code}", "detail": response.text[:200]}
    except Exception as e:
        return {"error": str(e)}

def submit_url(url_to_submit):
    """Submit a URL for indexing"""
    if not BING_API_KEY:
        return {"error": "BING_WEBMASTER key not set in .env"}
    
    url = f"{BING_API_BASE}/UrlSubmissionService/SubmitUrl"
    
    payload = {
        "siteUrl": SITE_URL,
        "url": url_to_submit
    }
    
    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        if response.status_code == 200:
            data = response.json()
            return {
                'status': 'ok',
                'submitted': url_to_submit,
                'result': data
            }
        else:
            return {"error": f"API error: {response.status_code}", "detail": response.text[:200]}
    except Exception as e:
        return {"error": str(e)}

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: bing_webmaster.py <keywords|crawl|stats|submit> [url]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'keywords':
        result = get_keywords()
    elif command == 'crawl':
        result = get_crawl_errors()
    elif command == 'stats':
        result = get_site_stats()
    elif command == 'submit':
        if len(sys.argv) < 3:
            print("Error: URL required for submit command")
            sys.exit(1)
        result = submit_url(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
    
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()