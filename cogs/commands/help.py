from discord.ext import commands
import json

with open('config.json', 'r') as file:
    config = json.load(file)

owner = config['owner']

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        bot = self.bot
        user = await bot.fetch_user(owner)
        await ctx.message.delete()
        helpMessage = "Помощь:\n"
        helpMessage += "troll <упоминание> - добавляет цель в траль лист\n"
        helpMessage += "untroll <упоминание> - удаляет цель из траль листа\n"
        helpMessage += "setdelay <время> - устанавливает задержку между сообщениями\n"
        helpMessage += "listTrolls - показывает траль-лист\n"
        helpMessage += "clearTrolls - очищает траль-лист\n"
        helpMessage += "enable - запускает тралинг\n"
        helpMessage += "disable - очищает траль-лист и выключает тралинг\n"
        helpMessage += "enableone - введите одно слово в консоли, которое будет спамить\n"
        helpMessage += "enableemoji - запускает спам смайликами\n"
        helpMessage += "ping - узнать пинг бота\n"
        helpMessage += "changerpc <arg> - поменять статус бота Аргументы: stream = стрим статус, watch = смотрит статус, listen = статус слушает, play = статус играет\n"
        helpMessage += "killchat <count> - спамит в чат\n"
        helpMessage += "message <userid> - отправляет сообщение указанному пользователю по его id\n"
        helpMessage += "guildleave <guildid> - покинуть сервер\n"
        await user.send(helpMessage)

def setup(bot):
    bot.add_cog(help(bot))