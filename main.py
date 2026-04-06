#!/usr/bin/env python3
import sys
import asyncio
import os
from colorama import init
from config import Colors, load_config
from bots import spammer, raider, nuker, dmmer, reaction_spammer

init()

def banner():
    print(f"""
{Colors.CYAN}
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                    Anyone who hurts you soon become nonexistent                   ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║ .      .       +    .       .    .      .     .  .      .       .    .       .  . ║
║ .     . +  .      .      .  +   .    .   .    .   . .     .    .      .      .  + ║
║  .       +   .     ███  █████   +   ███  ████   ███.  .      . █████    .     .   ║
║       .        +   ▒▒▒  ▒▒███    .  ▒▒▒  ▒▒███  ▒▒▒   .   .   ▒▒███ .      .     .║
║+    .   ████████   ████  ▒███████   ████  ▒███  ████   █████  ███████ .    .   +  ║
║    .   ▒▒███▒▒███ ▒▒███  ▒███▒▒███ ▒▒███  ▒███ ▒▒███  ███▒▒  ▒▒▒███▒.  .      .   ║
║   .   . ▒███ ▒███  ▒███  ▒███ ▒███  ▒███  ▒███  ▒███ ▒▒█████   ▒███ .    +    .  +║
║+   .    ▒███ ▒███  ▒███  ▒███ ▒███  ▒███  ▒███  ▒███  ▒▒▒▒███  ▒███ ███ +      .  ║
║ .    .  ████ █████ █████ ████ █████ █████ █████ █████ ██████   ▒▒█████    + .  .  ║
║ +   .   ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒     ▒▒▒▒▒   +        ║
║   +    .       .     .    https://discord.gg/HNQVkWJt   .   .   .  +    .    +    ║
║  .   .    .   +    .    .   .    .    +     .     .  .    .    .  +   .   +   .   ║
║     .           .     +       .    +    .    +  .   .   +   .     .       +     . ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║[0x00 - Hello!!!]▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█[    kxpz    ]║
╚═══════════════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
Discord Automation Toolkit v1.0
    """)

def print_menu():
    print(f"{Colors.YELLOW}Available Tools:{Colors.RESET}")
    print("1.  Message Spammer")
    print("2.  Server Raider") 
    print("3.  Account Nuker")
    print("4.  Mass DM Sender")
    print("5.  Reaction Spammer")
    print("6.  Token Checker")
    print("q.  Quit")

async def launch_tool(choice):
    config = load_config()
    
    if choice == "1":
        from bots.spammer import Spammer
        token = input(f"{Colors.BLUE}Token: {Colors.RESET}")
        channel = input(f"{Colors.BLUE}Channel ID: {Colors.RESET}")
        msg = input(f"{Colors.BLUE}Message: {Colors.RESET}") or config["default_messages"][0]
        bot = Spammer(token, channel, msg, config["spam_delay"])
        await bot.run()
        
    elif choice == "2":
        from bots.raider import Raider
        token = input(f"{Colors.BLUE}Token: {Colors.RESET}")
        invite = input(f"{Colors.BLUE}Invite Code: {Colors.RESET}")
        msgs = input(f"{Colors.BLUE}Messages (comma sep): {Colors.RESET}").split(",")
        bot = Raider(token, invite, [m.strip() for m in msgs])
        await bot.run()
        
    elif choice == "3":
        from bots.nuker import Nuker
        token = input(f"{Colors.RED}Target Token: {Colors.RESET}")
        bot = Nuker(token)
        await bot.run()
        
    elif choice == "4":
        from bots.dmmer import DMMer
        token = input(f"{Colors.BLUE}Token: {Colors.RESET}")
        targets_file = input(f"{Colors.BLUE}Targets file (or enter IDs): {Colors.RESET}") or "data/targets.json"
        msg = input(f"{Colors.BLUE}DM Message: {Colors.RESET}")
        bot = DMMer(token, targets_file, msg)
        await bot.run()
        
    elif choice == "5":
        from bots.reaction_spammer import ReactionSpammer
        token = input(f"{Colors.BLUE}Token: {Colors.RESET}")
        channel = input(f"{Colors.BLUE}Channel ID: {Colors.RESET}")
        msg_id = input(f"{Colors.BLUE}Target Message ID: {Colors.RESET}")
        bot = ReactionSpammer(token, channel, msg_id)
        await bot.run()
        
    elif choice == "6":
        from utils.token_validator import validate_tokens_bulk
        token_file = input(f"{Colors.BLUE}Tokens file: {Colors.RESET}") or "data/tokens.txt"
        await validate_tokens_bulk(token_file)

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("config"):
        os.makedirs("config")
        
    banner()
    while True:
        print_menu()
        choice = input(f"{Colors.GREEN}Choose (1-6/q): {Colors.RESET}").strip()
        if choice.lower() == 'q':
            print(f"{Colors.RED}Goodbye!{Colors.RESET}")
            break
        elif choice in ['1','2','3','4','5','6']:
            try:
                asyncio.run(launch_tool(choice))
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}[!] Stopped by user{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}[-] Error: {e}{Colors.RESET}")
