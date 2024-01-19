try:
    import discord
    from discord.ext import commands
except:
    print("[ ERROR ] Ошибка вы установили не все пакеты")

class changerpc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def changerpc(self, ctx, args):
        bot = self.bot
        user = ctx

        if args == "stream":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"{len(bot.guilds)} GUILDS", url="https://twitch.tv/404"))
            await user.send("Бот успешно сменил статус на стримит")
        elif args == "watch":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} GUILDS"))
            await user.send("Бот успешно сменил статус на смотрит")
        elif args == "listen":
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} GUILDS"))
            await user.send("Бот успешно сменил статус на слушает")
        elif args == "play":
            await bot.change_presence(activity=discord.Game(name=f"{len(bot.guilds)} GUILDS"))
            await user.send("Бот успешно сменил статус на играет")
        else:
            await ctx.send(f"Аргументы\nstream = стрим статус\nwatch = смотрит статус\nlisten = статус слушает\nplay = статус играет")   

def setup(bot):
    bot.add_cog(changerpc(bot))