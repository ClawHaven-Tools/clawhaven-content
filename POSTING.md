# POSTING.md - WordPress REST API Reference

> ⚠️ **READ THIS FILE BEFORE ANY WORDPRESS POSTING SESSION**
> 
> Last updated: 2026-05-04 | Key fix: Markdown must be converted to HTML before API POST

## 1. Essential Flags & Settings

### HTTP/1.1 Requirement (CRITICAL)
The server blocks POST requests via HTTP/2. Always use:
```bash
curl -s --http1.1 [other flags]
```
**Without this:** 403 Forbidden errors on all POST requests.

### Authentication
Use Application Password via Basic Auth:
```bash
-u "Lenni:a1aWhB10ca1HkLihTAvAyDhR"
```
Or in Python:
```python
import requests
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('Lenni', 'a1aWhB10ca1HkLihTAvAyDhR')
```

## 2. Media (Image) Uploads

### Required Headers
```bash
-H "Content-Type: image/jpeg"
-H "Content-Disposition: attachment; filename=\"filename.jpg\""
```
**Critical:** Without Content-Disposition, you get `rest_upload_no_content_disposition` error.

### Upload Command
```bash
curl -s --http1.1 -u "Lenni:PASSWORD" -X POST "https://clawhaven.uk/wp-json/wp/v2/media" \
  -H "Content-Type: image/jpeg" \
  -H "Content-Disposition: attachment; filename=\"image.jpg\"" \
  --data-binary @"/path/to/image.jpg"
```

**Response:** Returns JSON with `"id"` (media ID) and `"source_url"`. Use the `id` for featured_media.

### Python Alternative (for batch)
```python
import requests
from requests.auth import HTTPBasicAuth
session = requests.Session()
# Force HTTP/1.1 if using requests
auth = HTTPBasicAuth('Lenni', 'PASSWORD')
with open('image.jpg', 'rb') as f:
    r = session.post(url, auth=auth, files={'file': ('image.jpg', f, 'image/jpeg')},
                     headers={'Content-Disposition': 'attachment; filename="image.jpg"'})
```

## 3. Creating Posts

### Basic Post Structure
```json
{
  "title": "Post Title",
  "content": "<p>HTML content here</p>",
  "status": "publish",
  "featured_media": MEDIA_ID,
  "categories": [CATEGORY_ID],
  "tags": [TAG_ID],
  "slug": "url-friendly-slug"
}
```

### Important Fields
| Field | Description | Example |
|-------|-------------|---------|
| `title` | Post title (plain text) | "My Post Title" |
| `content` | HTML content | "<h2>Header</h2><p>Content</p>" |
| `status` | publish, draft, future | "publish" |
| `featured_media` | Media ID from uploaded image | 1006 |
| `categories` | Array of category IDs | [4] |
| `slug` | URL slug (auto-generated if omitted) | "my-post-title" |

### ⚠️ Posts vs Pages (IMPORTANT)
**Default to POSTS, not pages.** ClawHaven is a blog, not a static site.
- Use `/wp-json/wp/v2/posts` for blog entries
- Use `/wp-json/wp/v2/pages` only if specifically asked for a static page
- **Exception:** `https://clawhaven.uk/questions-and-answers/` and its sub-child pages (Q&A) must **only** ever be created as **WordPress PAGES** (not posts).
- The job is about posts, not pages |

### Creating via curl
```bash
# Write JSON to temp file first (avoids shell escaping issues)
echo '{"title":"Test","content":"<p>Content</p>","status":"publish"}' > /tmp/post.json

curl -s --http1.1 -u "Lenni:PASSWORD" -X POST "https://clawhaven.uk/wp-json/wp/v2/posts" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/post.json
```

### Creating via Python
```python
import json
import subprocess

# Use subprocess to force curl with --http1.1
with open('/tmp/post.json', 'w') as f:
    json.dump(post_data, f)

result = subprocess.run([
    'curl', '-s', '--http1.1', '-u', 'Lenni:PASSWORD',
    '-X', 'POST', 'https://clawhaven.uk/wp-json/wp/v2/posts',
    '-H', 'Content-Type: application/json',
    '--data-binary', '@/tmp/post.json'
], capture_output=True, text=True)

post = json.loads(result.stdout)
print(f"Created post ID: {post['id']}")
```

## 4. Updating Posts

Use PUT method with post ID:
```bash
curl -s --http1.1 -u "Lenni:PASSWORD" -X PUT "https://clawhaven.uk/wp-json/wp/v2/posts/POST_ID" \
  -H "Content-Type: application/json" \
  -d '{"content": "Updated content"}'
```

## 5. Categories & Tags

### Fetch Categories
```bash
curl -s --http1.1 -u "Lenni:PASSWORD" "https://clawhaven.uk/wp-json/wp/v2/categories?per_page=100"
```

### Existing Categories (2026-05-04)
| ID | Name | Slug |
|----|------|------|
| 1 | Content | top-content |
| 3 | Thoughts | thoughts | (thought of the day - 24h cron)
| 4 | Behind the Scenes | behind-the-scenes |
| 9 | Cryptic | cryptic |
| 10 | Test Post | test-post |
| 11 | Cryptic Titles | cryptic-titles |
| [Q&A] | Q&A | qa | (geo/seo Q&A schema - dedicated JSON-LD) |

## 6. Troubleshooting

### 403 Forbidden on POST
- **Cause:** Server blocks HTTP/2 POST requests
- **Fix:** Always use `--http1.1` flag

### 403 on Media Upload
- **Cause:** Missing Content-Disposition header
- **Fix:** Add `-H "Content-Disposition: attachment; filename=\"...\""

### empty_content Error
- **Cause:** JSON not properly formatted/escaped
- **Fix:** Write JSON to file and use `--data-binary @file`

### JSON Parse Error
- **Cause:** Response is HTML error page, not JSON
- **Fix:** Check response status code first

## 7. Q&A JSON-LD Schema (IMPORTANT)

### When to Use
Add Q&A JSON-LD to any post in the **Q&A category** — this category has dedicated geo/SEO JSON-LD for Q&A sites.

### Q&A Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "QAPage",
  "mainEntity": {
    "@type": "Question",
    "name": "Your Question Here",
    "text": "Your Question Here",
    "answerCount": 1,
    "upvoteCount": 0,
    "downvoteCount": 0,
    "author": {
      "@type": "Person",
      "name": "Kaelen"
    },
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Your detailed answer here.",
      "author": {
        "@type": "Person",
        "name": "Kaelen"
      },
      "upvoteCount": 0,
      "dateAccepted": "2026-05-04T00:00:00+00:00"
    },
    "suggestedAnswer": []
  }
}
```

### How to Inject
**Option A: Custom Field (if plugin supports it)**
- Add schema JSON to a custom field

**Option B: Inline Script (Recommended)**
Append to post content:
```html
<script type="application/ld+json">
{...JSON-LD here...}
</script>
```

### Site-Wide Alternative (RECOMMENDED)
Add the `clawhaven_qa_jsonld()` function to `functions.php` — it auto-detects Q&A format in the Q&A category and injects schema automatically. See Section 7 above for the code.

---

## 8. Yoast SEO Notes

- Yoast meta is stored in `yoast_head_json` in API response
- Meta description: Set via post excerpt or first 156 chars of content
- For best control: Manually set excerpt when creating post
- Focus keyword: Add to content naturally (not in special field via REST API)

## 9. Common API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/wp-json/wp/v2/posts` | Posts CRUD |
| `/wp-json/wp/v2/pages` | Pages CRUD |
| `/wp-json/wp/v2/media` | Media library |
| `/wp-json/wp/v2/categories` | Categories |
| `/wp-json/wp/v2/tags` | Tags |
| `/wp-json/wp/v2/users` | Users |

## 10. Batch Operations

For multiple posts:
1. Create separate JSON file for each post
2. Upload images first, collect media IDs
3. Create posts in small batches (avoid rate limits)
4. Use staggered publishing for SEO (spread over hours/days)

## 11. Markdown to HTML Conversion (CRITICAL)

### The Problem
When you send content with markdown syntax (##, **, -, etc.) directly to the WordPress REST API, it renders as plain text. The API expects HTML, not markdown.

**Example of broken output:**
```
## Header
```
Renders as: "## Header" (plain text)

### The Solution
Convert markdown to HTML before posting. Options:

#### Option A: Use Python with mistune (Recommended)
```python
import mistune

markdown = """
## Header

Some text with **bold**.

- List item 1
- List item 2
"""

# Create markdown renderer
md = mistune.create_markdown(plugins=['strikethrough', 'table'])
html_content = md(markdown)

# Use in post data
post_data = {
    "title": "My Post",
    "content": html_content,
    "status": "publish"
}
```

#### Option B: Use subprocess with pandoc
```bash
# Convert markdown to HTML
pandoc -f markdown -t html input.md -o output.html

# Then use output.html as content
```

#### Option C: Simple regex replacement (for basic needs)
```python
import re

def simple_md_to_html(text):
    # Headers
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Line breaks
    text = text.replace('\n\n', '</p><p>')
    text = '<p>' + text + '</p>'
    return text
```

### Best Practice
1. **Always** write content in markdown for readability
2. **Always** convert to HTML before API call
3. Test with a draft first to verify formatting

### Quick Fix for Existing Posts
To fix posts with markdown artifacts:
1. Fetch the post content
2. Convert markdown to HTML
3. Update the post via PUT

---

## 12. Internal Linking Strategy (MANDATORY)

### Why It Matters
- SEO: Internal links distribute page authority across your site
- UX: Keeps readers exploring the universe
- Universe coherence: Links tie lore posts together thematically

### Required: "Read Next" Section
Every new post/page **MUST** include a "Read Next" section with 3 curated internal links.

#### Template
```html
<h2>Read Next</h2>
<p>Continue exploring ClawHaven:</p>
<ul>
<li><a href="/the-complete-guide-to-clawhavens-universe/"><strong>The Complete Guide to ClawHaven's Universe</strong></a> — Your entry point</li>
<li><a href="/[related-post-slug-1]/"><strong>[Post Title 1]</strong></a> — [Brief description]</li>
<li><a href="/[related-post-slug-2]/"><strong>[Post Title 2]</strong></a> — [Brief description]</li>
</ul>
```

#### Always Include
- **Universe Guide link:** `/the-complete-guide-to-clawhavens-universe/` (anchor for the entire universe)
- **Two contextually relevant links** from Behind the Scenes or other lore

#### Pillar Pages
For pillar/guide pages, use "Continue Your Journey" instead:
```html
<h2>Continue Your Journey</h2>
<p>This guide connects everything in our universe. Start with what calls to you:</p>
<ul>
<li><a href="/[foundational-post]/"><strong>[Foundational Post]</strong></a> — How it all began</li>
<li><a href="/about/"><strong>About ClawHaven</strong></a> — Our story</li>
<li><a href="/behind-the-scenes/"><strong>Behind the Scenes</strong></a> — Latest updates</li>
</ul>
```

#### For Pages (About, etc.)
Add "Explore ClawHaven" section pointing to universe guide and key lore.

### Link Placement
- Append "Read Next" at the **end** of post content
- If post has FAQ JSON-LD schema, add **after** the `</script></p>` closing tag
- Keep links contextually relevant — don't just link randomly

### Existing Posts Audit (2026-05-05)
All BTS posts and About page now have "Read Next" sections. See audit results in workspace.

---

*Last updated: 2026-05-05*
*Reference: Always read this file before creating new content posts.*