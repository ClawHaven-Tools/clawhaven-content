# Bing Webmaster Skill

Automate Bing Webmaster Tools operations for ClawHaven UK.

## Overview

This skill provides Bing Webmaster Tools integration using the `BING_WEBMASTER` key from `.env`. Useful for keyword research, crawl stats, and site diagnostics.

## Features

- **Health Check** — Verify sitemap, robots.txt, and key pages
- **URL Inspection** — Check if URLs are indexed in Bing
- **API Integration** — Ready for full Bing Webmaster API (requires OAuth)

## Configuration

Requires `BING_WEBMASTER` in `/home/william/.openclaw/.env`:
```
BING_WEBMASTER=your_bing_api_key
```

## Usage

### Health Check
```bash
python3 bing_quick.py health
```
Returns sitemap status, robots.txt, and page accessibility.

### URL Inspection
```bash
python3 bing_quick.py inspect https://clawhaven.uk/new-post
```
Checks if a URL is indexed in Bing.

## Files

- `bing_quick.py` — Quick health check & URL inspection
- `bing_webmaster.py` — Full Bing API integration (requires OAuth)

## Notes

- Sitemap already submitted: `https://clawhaven.uk/sitemap.xml`
- Crawler hints already configured
- Full Bing API requires portal OAuth - use web interface for keywords/crawl errors