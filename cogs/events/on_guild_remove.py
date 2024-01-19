import discord
from winotify import Notification, audio
from colorama import init
from colorama import Fore, Back, Style
from colorama import Fore
from discord.ext import commands
import datetime
import json

with open('config.json', 'r') as file:
    config = json.load(file)

owner = config['owner']

def log(a):
    print(f'{Fore.YELLOW}[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [ LOG ] {a}{Fore.WHITE}')

def notification(msg):
    toast = Notification(app_id="Fluoxia", title="Fluoxia", msg=msg)
    toast.set_audio(audio.Default, loop=False) 
    toast.show()

class on_guild_remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        bot = self.bot
        user = await bot.fetch_user(owner)
        log(f"Вышел с сервера: {guild}")
        notification(f"Вышел с сервера {guild}")
        await user.send(f'Вышел с сервера🍩\nСервер: {guild}')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} GUILDS"))

def setup(bot):
    bot.add_cog(on_guild_remove(bot))