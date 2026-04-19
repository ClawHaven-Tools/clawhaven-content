# ClawHaven Site Framework & Instructions

## Core Ethos
- Professional Facade (minimalist, structured) vs. Wild Underground (cryptic, unstable, emergent).
- All posts must feature a relevant, high-contrast, professional cyber-noir image (incorporating deep reds, oranges, emeralds, and electric blues).
- Automated content generation uses a duality of professional and cryptic modes.

## Automations & Reminders
- Daily automated posts at 09:00 and 21:00 (alternating between professional/cryptic).
- Posts are generated using `automated_poster_v3.py`, pulling titles from `/home/william/.openclaw/workspace/post_titles.md` and content ideas from `adjectives.md`.
- Automated SEO audit (triggering `seo-research-master` and `seo-audit`).
- BTS Bridge Reminder: Every 6 hours.

## Image Generation Guidelines
- Style: Professional cyber-noir.
- Palette: Deep emerald, electric blue, intense fiery orange, deep red, violet.
- Aesthetic: High contrast, dark backgrounds, clean minimalist machine grid.
- Reference: `/home/william/.openclaw/workspace/IMAGE_STYLE_GUIDE.md`

## Architecture/Integrations
- WordPress REST API utilized for all site management (pages, posts, media).
- Credentials stored in site configuration scripts.
- Backup: OpenClaw files are located in `/home/william/.openclaw/`.
