import discord
import asyncio
import random
from discord.ext import commands
from config import Colors

class ReactionSpammer(commands.Bot):
    def __init__(self, token, channel_id, message_id):
        intents = discord.Intents.default()
        super().__init__(command_prefix='!', intents=intents)
        self.token = token
        self.channel_id = int(channel_id)
        self.message_id = int(message_id)
        self.emojis = ["😂","💀","🔥","👍","👎","❤️","😈","🌀"]
        
    async def on_ready(self):
        print(f"{Colors.GREEN}[+] Reaction spammer ready{Colors.RESET}")
        channel = self.get_channel(self.channel_id)
        msg = await channel.fetch_message(self.message_id)
        await self.reaction_flood(msg)
    
    async def reaction_flood(self, message):
        while True:
            try:
                emoji = random.choice(self.emojis)
                await message.add_reaction(emoji)
                print(f"{Colors.YELLOW}[+] {emoji}{Colors.RESET}")
                await asyncio.sleep(0.1)
            except discord.HTTPException:
                await message.clear_reactions()
                await asyncio.sleep(1)
    
    async def run(self):
        await self.start(self.token, bot=False)
