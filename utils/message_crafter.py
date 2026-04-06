import discord
import random

def create_embed_spam(title="Spam", description="🌀", color=0xff0000):
    embed = discord.Embed(title=title, description=description, color=color)
    embed.add_field(name="Status", value="RAIDING", inline=True)
    return embed

def generate_spam_messages(count=10):
    templates = [
        "🌀 TEST 🌀",
        "discord raid active",
        "server compromised",
        f"message #{random.randint(1,999)}"
    ]
    return random.choices(templates, k=count)
