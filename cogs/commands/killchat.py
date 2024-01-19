from discord.ext import commands
from random import randint

class killchat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def killchat(self, ctx, args, *, count=5):
        for i in range(int(count)):
            text = f'||{randint(0,1918177181)}|| {args} \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{args}'
            await ctx.send(text)
        await ctx.message.delete()  

def setup(bot):
    bot.add_cog(killchat(bot))