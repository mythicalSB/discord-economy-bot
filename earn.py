from discord.ext import commands
import random

class Earn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def earn(self, ctx):
        earnings = random.randint(10, 50)
        await ctx.send(f"{ctx.author.mention} earned {earnings} coins!")

def setup(bot):
    bot.add_cog(Earn(bot))
