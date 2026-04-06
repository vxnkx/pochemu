import random
import os
from config import Colors, PROXY_FILE

class ProxyManager:
    def __init__(self, proxy_file=PROXY_FILE, proxy_type="http"):
        self.proxy_type = proxy_type.lower()
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
        
        # Handle different proxy types
        if self.proxy_type == "http":
            return {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
        
        elif self.proxy_type == "https":
            return {
                "http": f"https://{proxy}",
                "https": f"https://{proxy}"
            }
        
        elif self.proxy_type == "socks5":
            return {
                "http": f"socks5h://{proxy}",
                "https": f"socks5h://{proxy}"
            }
        
        # fallback (prevents crashes if misconfigured)
        return {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
