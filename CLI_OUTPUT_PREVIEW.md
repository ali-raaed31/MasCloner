# MasCloner CLI - Output Preview

## What the new CLI looks like when you run it

### 1. Update Command

```bash
sudo mascloner update
```

**Output:**
```
╭─────────────────────────────────────────────────────────╮
│         MasCloner Update                                │
│  Safely update your MasCloner installation to the       │
│  latest version                                         │
╰─────────────────────────────────────────────────────────╯

✓ Check prerequisites
✓ Check for updates
✓ Create backup
⠋ Stopping services...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45% 00:32

┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Service         ┃ Status   ┃ Action            ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ mascloner-api   │ ● stopped│ ⏸  Waiting       │
│ mascloner-ui    │ ● stopped│ ⏸  Waiting       │
│ mascloner-tunnel│ ● active │ ✓ No restart     │
└─────────────────┴──────────┴───────────────────┘

✓ Update code
✓ Update dependencies  
✓ Run migrations
✓ Update services
⠋ Starting services...

┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Service         ┃ Status   ┃ Action            ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ mascloner-api   │ ● active │ ✓ Started         │
│ mascloner-ui    │ ● active │ ✓ Started         │
│ mascloner-tunnel│ ● active │ ✓ Running         │
└─────────────────┴──────────┴───────────────────┘

┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Check             ┃ Status   ┃ Details              ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ API Health        │ ✓ PASS   │ http://127.0.0.1:... │
│ UI Health         │ ✓ PASS   │ http://127.0.0.1:... │
│ Database          │ ✓ PASS   │ http://127.0.0.1:... │
│ File Tree         │ ✓ PASS   │ http://127.0.0.1:... │
└───────────────────┴──────────┴──────────────────────┘

╭─────────────────────────────────────────────────────────╮
│                                                         │
│              ✓ Success                                  │
│                                                         │
│  Duration:        42.3 seconds                          │
│  Steps completed: 10/10                                 │
│                                                         │
╰─────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────╮
│              ✅ Next Steps                              │
│                                                         │
│  1. 🔍 Review the health check results above            │
│  2. 🌐 Access your MasCloner UI to verify functionality │
│  3. 📊 Monitor service logs: journalctl -f -u ...       │
│  4. 💾 Backup saved at: /var/backups/mascloner/...      │
│                                                         │
╰─────────────────────────────────────────────────────────╯
```

---

### 2. Status Command

```bash
sudo mascloner status
```

**Output:**
```
╭─────────────────────────────────────────────────────────╮
│         MasCloner Status                                │
│  Current installation status                            │
╰─────────────────────────────────────────────────────────╯

Version: v2.2.0
Installation: /srv/mascloner

┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Service         ┃ Status   ┃ Action            ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ mascloner-api   │ ● active │ Running           │
│ mascloner-ui    │ ● active │ Running           │
│ mascloner-tunnel│ ● active │ Running           │
└─────────────────┴──────────┴───────────────────┘

ℹ Running health checks...

┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Component         ┃ Status        ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ API               │ ✓ Healthy     │
│ UI                │ ✓ Healthy     │
│ Database          │ ✓ Healthy     │
└───────────────────┴───────────────┘

✓ All systems operational
```

---

### 3. Rollback Command

```bash
sudo mascloner rollback --list
```

**Output:**
```
╭─────────────────────────────────────────────────────────╮
│         Available Backups                               │
│  Location: /var/backups/mascloner                       │
╰─────────────────────────────────────────────────────────╯

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Backup File                         ┃ Size   ┃ Date        ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━┩
│ mascloner_pre_update_20240930_14... │ 15.2MB │ 20240930... │
│ mascloner_pre_update_20240929_09... │ 14.8MB │ 20240929... │
│ mascloner_pre_update_20240928_11... │ 14.5MB │ 20240928... │
└─────────────────────────────────────┴────────┴─────────────┘

Total backups: 3
```

---

### 4. Update with Dry Run

```bash
sudo mascloner update --dry-run
```

**Output:**
```
╭─────────────────────────────────────────────────────────╮
│         MasCloner Update                                │
│  Safely update your MasCloner installation to the       │
│  latest version                                         │
╰─────────────────────────────────────────────────────────╯

ℹ Running in DRY RUN mode - no changes will be made

✓ Check prerequisites
✓ Check for updates

┏━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type       ┃ Count ┃ Examples (showing max 5)       ┃
┡━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Added      │ 5     │ + app/api/new_endpoint.py      │
│            │       │ + app/ui/new_component.py      │
│            │       │ + ops/cli/commands/update.py   │
│ Modified   │ 3     │ ~ app/api/main.py              │
│            │       │ ~ requirements.txt             │
└────────────┴───────┴────────────────────────────────┘

ℹ Dry run complete - stopping here
```

---

### 5. Error Handling Example

If a service fails to start:

```
╭─────────────────────────────────────────────────────────╮
│              ⚠ Update Failed                            │
│                                                         │
│  Error: Failed to start mascloner-api service           │
│                                                         │
│  Recovery Steps:                                        │
│  1. Restore from backup: /var/backups/mascloner/...     │
│  2. Check logs: journalctl -u mascloner-api             │
│  3. Contact support if issue persists                   │
│                                                         │
╰─────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────────╮
│         📜 mascloner-api Logs                          │
│                                                        │
│  1 │ ERROR: Failed to bind to port 8787               │
│  2 │ ERROR: Address already in use                    │
│  3 │ INFO: Shutting down...                           │
│                                                        │
╰────────────────────────────────────────────────────────╯
```

---

### 6. Comparison: Old vs New

#### Old Bash Script:
```
[INFO] Starting MasCloner update process...
[INFO] Checking prerequisites...
[SUCCESS] Prerequisites check passed
[INFO] Checking for updates from repository...
[INFO] Fetching latest version from GitHub...
[INFO] Comparing with current installation...
[SUCCESS] ✨ Updates available! Changes detected in repository.
[INFO] The update will proceed...

Continue with update? (y/N): 
```

#### New Rich CLI:
```
╭─────────────────────────────────────────────────────────╮
│         MasCloner Update                                │
│  Safely update your MasCloner installation to the       │
│  latest version                                         │
╰─────────────────────────────────────────────────────────╯

✓ Check prerequisites
⠋ Checking for updates...

┏━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Type       ┃ Count ┃ Examples (showing max 5)       ┃
┡━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Added      │ 12    │ + app/api/endpoints/new.py     │
└────────────┴───────┴────────────────────────────────┘

• Services will be temporarily stopped
• A backup will be created automatically  
• Update typically takes 1-2 minutes

Proceed with update? [Y/n]: 
```

---

## Color Scheme

- **Green (✓)** - Success, healthy, active
- **Red (✗)** - Error, failed, stopped
- **Yellow (⚠)** - Warning, in progress
- **Blue (ℹ)** - Information
- **Cyan** - Headers, important data
- **Dim** - Secondary information

## Interactive Elements

- **Progress bars** - Show completion percentage and time
- **Spinners** - Indicate ongoing operations
- **Tables** - Structured data display
- **Panels** - Grouped information with borders
- **Prompts** - Interactive confirmations with context

---

This is what you'll experience with the new CLI! 🎨✨
