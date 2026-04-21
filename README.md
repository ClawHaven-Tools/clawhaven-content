# ClawHaven WordPress Tools

Collection of WordPress utilities and automation tools for ClawHaven.

## 📦 Available Tools

### API Version Control Plugin
Tracks all API edits and provides unlimited revision history with rollback capability.

**Features:**
- Unlimited post revisions (no limit)
- API edit logging via Simple History
- Admin panel for viewing edit history
- Full audit trail of all API changes

---

## 🚀 Quick Install Guide

### 1. Install the API Version Control Plugin

**Option A: Manual Installation**
```bash
# Create plugin directory
mkdir -p /wp-content/plugins/api-version-control/

# Copy the plugin file
# (Download from: https://github.com/ClawHaven-Tools/clawhaven-core/raw/main/wordpress-api-version-control.php)
# Save as: /wp-content/plugins/api-version-control/api-version-control.php
```

**Option B: Git Clone**
```bash
cd /wp-content/plugins/
git clone https://github.com/ClawHaven-Tools/clawhaven-core.git
# The plugin is in: clawhaven-core/wordpress-api-version-control.php
# Create symlink or copy to api-version-control/ folder
```

**Activate in WordPress Admin:**
1. Go to **Plugins → Installed Plugins**
2. Find **API Version Control**
3. Click **Activate**

---

### 2. Configure wp-config.php

Add these lines to your `wp-config.php` file (before the line that says `/* That's all, stop editing! Happy blogging. */`):

```php
// Version control settings
define('WP_POST_REVISIONS', -1);  // Unlimited revisions
define('AUTOSAVE_INTERVAL', 86400);  // 24 hours between autosaves
```

---

### 3. Verify Installation

After activation, test by making an API edit:

```bash
# Example: Update a post via API
curl -X POST "https://your-site.com/wp-json/wp/v2/posts/YOUR_POST_ID" \
  -u "username:application_password" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Post"}'
```

Then check revisions:
```bash
curl -s "https://your-site.com/wp-json/wp/v2/posts/YOUR_POST_ID/revisions" \
  -u "username:application_password" | jq '. | length'
```

Should return `1` or more.

---

## 📖 Usage

### Viewing Revision History

1. Open WordPress Admin
2. Go to any **Post**
3. Look for the **Revisions** meta box (or click "Revisions" in the publish panel)
4. Use the slider to preview previous versions
5. Click **Restore This Revision** to roll back

### Viewing API Edit Logs

1. Go to **Dashboard → Simple History** (if Simple History plugin is installed)
2. All API edits are logged with:
   - Timestamp
   - User/Application that made the change
   - Endpoint used
   - Changes made

### Creating API Application Password

1. Go to **Users → Profile**
2. Scroll to **Application Passwords**
3. Enter a name (e.g., "OpenClaw Automation")
4. Click **Add New**
5. Copy the generated password (shown once)

---

## 🔧 Dependencies

Required plugins (install via WordPress Admin or API):

| Plugin | Purpose |
|--------|---------|
| Simple History | Logs API changes to admin dashboard |
| PublishPress Revisions | Enhanced revision management |
| WP Rollback | Easy version rollback from plugins/themes |

Install via API:
```bash
curl -s -X POST "https://your-site.com/wp-json/wp/v2/plugins" \
  -u "username:app_password" \
  -H "Content-Type: application/json" \
  -d '{"slug":"simple-history","status":"active"}'
```

---

## 🔐 Security Notes

- Never commit credentials to version control
- Use Application Passwords, not regular passwords
- Restrict API access via `.htaccess` if needed
- The plugin logs user info for accountability

---

## 📁 File Structure

```
clawhaven-core/
├── README.md                          # This file
├── wordpress-api-version-control.php  # Main plugin
└── wp-config-additions.txt            # Config snippet
```

---

## 🐛 Troubleshooting

**No revisions being created?**
- Verify `WP_POST_REVISIONS` is set to `-1` in wp-config.php
- Check that the plugin is activated

**Can't see revision history?**
- Ensure you're using a post type that supports revisions
- Check WordPress admin user permissions

**API edits not logging?**
- Install and activate Simple History plugin
- Check WordPress error log

---

## 📄 License

MIT License - Feel free to use and modify for your own projects.