from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
       for i in range(9999999):
            bot = self.bot
            await ctx.send(f":ping_pong: Понг!, Задержка API - {round(bot.latency * 1000)}ms")  

def setup(bot):
    bot.add_cog(ping(bot))