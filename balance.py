from discord.ext import commands

class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balances = {}

    @commands.command()
    async def balance(self, ctx):
        user_balance = self.balances.get(ctx.author.id, 0)
        await ctx.send(f"{ctx.author.mention}, your balance is {user_balance} coins!")

def setup(bot):
    bot.add_cog(Balance(bot))
