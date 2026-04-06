import os
import json
from colorama import init, Fore

init(autoreset=True)

# File paths
TOKEN_FILE = "data/tokens.txt"
PROXY_FILE = "data/proxies.txt"
CONFIG_FILE = "config/config.json"
TARGETS_FILE = "data/targets.json"

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Fore.RESET

# Default config
DEFAULT_CONFIG = {
    "spam_delay": 0.1,
    "max_messages": 1000,
    "use_proxies": False,
    "proxy_type": "http"
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_CONFIG
