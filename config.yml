import discord
from discord.ext import commands
from Configuration.config import TOKEN
from handlers.command_handler import load_commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load commands
load_commands(bot)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(TOKEN)
