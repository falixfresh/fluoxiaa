from discord.ext import commands

class guildleave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def guildleave(self, ctx, guild_id: int):
        bot = self.bot
        guild = bot.get_guild(guild_id)
        if guild:
            try:
                await guild.leave()
                await ctx.message.add_reaction('✅')
            except:
                await ctx.send(f"Не удалось покинуть сервер: {guild.name}")

def setup(bot):
    bot.add_cog(guildleave(bot))