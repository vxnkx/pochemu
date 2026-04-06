import discord
import json
import aiohttp
from discord.ext import commands
from config import Colors, TARGETS_FILE

class DMMer(commands.Bot):
    def __init__(self, token, targets_file, message):
        intents = discord.Intents.default()
        super().__init__(command_prefix='!', intents=intents)
        self.token = token
        self.message = message
        self.targets = self.load_targets(targets_file)
        
    def load_targets(self, file_path):
        if file_path == TARGETS_FILE and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f).get('user_ids', [])
        else:
            return [tid.strip() for tid in file_path.split(',')]
    
    async def on_ready(self):
        print(f"{Colors.GREEN}[+] DMmer: {self.user}{Colors.RESET}")
        await self.mass_dm()
    
    async def mass_dm(self):
        sent = 0
        async with aiohttp.ClientSession() as session:
            for user_id in self.targets[:50]:  # Limit
                try:
                    # Create DM channel
                    payload = {"recipient_id": user_id}
                    dm_resp = await session.post(
                        "https://discord.com/api/v10/users/@me/channels",
                        headers={"Authorization": self.token},
                        json=payload
                    )
                    
                    if dm_resp.status == 200:
                        channel = await dm_resp.json()
                        await session.post(
                            f"https://discord.com/api/v10/channels/{channel['id']}/messages",
                            headers={"Authorization": self.token},
                            json={"content": self.message}
                        )
                        sent += 1
                        print(f"{Colors.GREEN}[+] DM sent to {user_id}{Colors.RESET}")
                        await asyncio.sleep(1.5)  # Rate limit
                except:
                    continue
        print(f"{Colors.YELLOW}[+] Total DMs sent: {sent}{Colors.RESET}")
        await self.close()
    
    async def run(self):
        await self.start(self.token, bot=False)
