from discord.ext import commands

class message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def message(self, ctx, user_id, *, messagge):
        bot = self.bot
        user = await bot.fetch_user(user_id)

        await user.send(messagge)   

def setup(bot):
    bot.add_cog(message(bot))