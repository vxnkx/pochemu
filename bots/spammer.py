import discord
import asyncio
from discord.ext import commands
from config import Colors

class Spammer(commands.Bot):
    def __init__(self, token, channel_id, message, delay=0.1):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
        self.token = token
        self.channel_id = int(channel_id)
        self.message = message
        self.delay = delay
        self.sent = 0
        
    async def on_ready(self):
        print(f"{Colors.GREEN}[+] Spammer ready: {self.user}{Colors.RESET}")
        channel = self.get_channel(self.channel_id)
        await self.spam(channel)
    
    async def spam(self, channel):
        while self.sent < 1000:  # Safety limit
            try:
                await channel.send(self.message)
                self.sent += 1
                print(f"{Colors.GREEN}[+] #{self.sent}: {self.message[:30]}...{Colors.RESET}")
                await asyncio.sleep(self.delay)
            except Exception as e:
                print(f"{Colors.RED}[-] Error: {e}{Colors.RESET}")
                await asyncio.sleep(1)
        await self.close()
    
    async def run(self):
        await self.start(self.token, bot=False)
