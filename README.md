# 🌀 Pochemu

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/discord.py-2.3.2-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="discord.py">
  <img src="https://img.shields.io/badge/Status-🚀%20Ready-green" alt="Status">
</div>

**Multi-purpose Discord bot framework for testing.**

## ✨ Features

| Tool | Description | Speed |
|------|-------------|-------|
| 💬 **Message Spammer** | Flood channels with text/embeds | 10-100 msg/sec |
| 🏰 **Server Raider** | Join → Spam → Chaos → Leave | Full server takeover |
| 💣 **Account Nuker** | Delete everything, leave all servers | Complete account wipe |
| 📨 **Mass DM Sender** | Send DMs to 100+ users | Rate-limit safe |
| 😈 **Reaction Spammer** | Flood reactions on any message | 50+ reactions/sec |
| 🔍 **Token Checker** | Validate 1000+ tokens in bulk | 10 tokens/sec |

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Quick Start (5 minutes)](#quick-start)
- [Complete Setup Tutorial](#complete-setup-tutorial)
- [Tool-by-Tool Guide](#tool-by-tool-guide)
- [Configuration Files](#configuration-files)
- [Troubleshooting](#troubleshooting)
- [Advanced Usage](#advanced-usage)

---

## 🛠️ Prerequisites

### Required
Python 3.8+ ✅ Git ✅ (optional) Windows/Linux/Mac
### Install Python
**Windows:** [python.org/downloads](https://python.org/downloads) → **Add to PATH**
**Linux:** `sudo apt install python3 python3-pip`
**Mac:** `brew install python`

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Download
git clone https://github.com/vxnkx/pochemu.git
cd pochemu

# 2. Install
pip install -r requirements.txt

# 3. Run!
python main.py
Choose 1 → Enter token → Enter channel ID → Type message → SPAM!
```

📖 Complete Setup Tutorial
Step 1: Clone & Install (2 min)
```bash
git clone https://github.com/vxnkx/pochemu.git
cd pochemu
pip install -r requirements.txt
✅ Test: python main.py → See colorful menu
```
Step 2: Get Discord Token (1 min)
```bash
Open Discord in browser (not app)
Press F12 → Application tab
Local Storage → https://discord.com
Find token → Copy full value
Paste into data/tokens.txt (one per line)
Example token format:
NTAxMjM0NTY3ODkwMTIzNDU2.YOUR_PART.ABC123DEF456
```
Step 3: Setup Targets (Optional, 1 min)
```bash
Edit data/targets.json:
{
    "user_ids": ["123456789012345678", "987654321098765432"]
}
Get IDs: Discord Settings → Advanced → Developer Mode → Right-click → Copy ID
```
Step 4: Add Proxies (Optional, 1 min)
```bash
data/proxies.txt:
45.67.89.123:8080
user:pass@proxy.com:3128
```
Step 5: Launch! 🎉
```bash
python main.py
```
Menu appears → Choose 1-6 → Follow prompts → Done!

🧰 Tool-by-Tool Guide

1️⃣ Message Spammer ⭐ Easiest
Input needed: 

• Token (from Step 2)
• Channel ID (right-click channel → Copy ID)
• Message ("🌀 TEST 🌀")

Output: 1000+ messages in <10 seconds

2️⃣ Server Raider ( Most Fun )
Input needed: 

• Token
• Invite link/code (discord.gg/ABC123 → just "ABC123")
• Messages ("raid1,raid2,raid3")

What it does: 

1. Joins server
2. Spams 10 channels
3. Creates 25 spam roles
4. Changes nickname to "🌀RAIDER🌀"
5. Leaves after 60s

3️⃣ Account Nuker 💥 Destructive WIP
Input needed: 

• TARGET account's token

Destroys: 

• All messages (bulk delete)
• All servers (leave)
• All DMs (purge)
• Webhooks (delete)

4️⃣ Mass DM Sender
Input needed: 

• Token
• Targets file OR "id1,id2,id3"
• Message

Sends DMs to 50+ users safely

5️⃣ Reaction Spammer 😈
Input needed: 

• Token
• Channel ID
• Message ID (right-click message → Copy ID)

Floods 10+ reactions/second

6️⃣ Token Checker 🔍
Input needed:
• tokens.txt file path

Validates 1000+ tokens → Shows working ones

### ⚙️ Configuration Files
data/tokens.txt - YOUR TOKENS HERE
# One token per line (paste directly)
MTIzNDU2Nzg5MDEyMzQ1Njc4.YOURTOKENPART.abcDEF123ghiJKL
another.token.here.456XYZ789|

### data/proxies.txt - ANTI-BAN

# Free proxies (ip:port format, THIS IS ONLY AN EXAMPLE!)
45.67.89.123:8080
192.168.1.100:3128
user:pass@proxy.com:8080

### data/targets.json - BULK TARGETS
{
    "user_ids": ["123456789012345678","987654321098765432"],
    "guild_ids": [inputserveridhere],
    "channels": [inputchannelidhere]
}

### config/config.json - SPEED SETTINGS
{
    "spam_delay": 0.1,    // Lower = faster (0.05 = max speed)
    "max_messages": 1000, // Safety limit
    "use_proxies": false 
}

### ❗ Troubleshooting

Problem	Solution

```bash
ModuleNotFoundError = pip install -r requirements.txt
```
```bash
Invalid token =	Check F12 → Local Storage → Copy FULL token
```
```bash
403 Forbidden	= Token expired → Get new one
```
```bash
Rate limited = Add proxies OR increase delay in config
```
```bash
No module colorama = pip install colorama
```
```bash
Channel ID wrong = Enable Developer Mode → Right-click channel
```
Pro Tip: Ctrl+C stops any tool instantly

### 🚀 Advanced Usage
Bulk Token Raiding
1. Fill data/tokens.txt (100+ tokens)
2. python main.py → 2 (Raider)
3. Uses random token each run

### Proxy Rotation
1. Fill data/proxies.txt (50+ proxies)
2. Edit config.json → "use_proxies": true
3. Automatic IP rotation

### Custom Messages
main.py → Message Spammer → Type:
"🌀 Raid #{random.randint(1,999)} 🌀"

### Watchdog Mode
```bash
# Auto-restart on crash
while true; do python main.py; sleep 2; done
```
### 📊 Performance
Tool	  No Proxy	  With Proxy     Max Targets
Spammer	100 msg/s	   50 msg/s	      1 channel
Raider	1 server	   5 servers	    Unlimited
Nuker	  1 account	  10 accounts	    Unlimited
DMMER  	1/sec	         2/sec	      100 users


### ⚖️ Legal Notice

🔒 Authorized testing only
🔒 Your own accounts/servers
🔒 Educational purposes
🔒 No warranty provided

🤝 Contributing
1. Fork repo
2. Add new tools to /bots/
3. Test thoroughly
4. PR with demo video

### 📞 Support
Discord: Add new tools → Open issue
Issues: github.com/vxnkx/pochemu/issues
Made with ❤️ for Discord automation enthusiasts
https://img.shields.io/badge/version-2.0-00D2FF?style=for-the-badge&logo=discord&logoColor=white
