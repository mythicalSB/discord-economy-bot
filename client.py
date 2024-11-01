from discord.ext import commands

def setup_client_events(bot):
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        await bot.process_commands(message)
