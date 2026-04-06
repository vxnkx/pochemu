import random
import os
from config import Colors, PROXY_FILE

class ProxyManager:
    def __init__(self, proxy_file=PROXY_FILE):
        self.proxies = self.load_proxies(proxy_file)
    
    def load_proxies(self, file_path):
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    
    def get_random_proxy(self):
        if not self.proxies:
            return None
        proxy = random.choice(self.proxies)
        print(f"{Colors.CYAN}[Proxy] Using: {proxy}{Colors.RESET}")
        return {"http": f"http://{proxy}", "https": f"http://{proxy}"}
