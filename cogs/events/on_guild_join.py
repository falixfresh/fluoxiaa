import discord
from winotify import Notification, audio
from discord.ext import commands
from colorama import init
from colorama import Fore, Back, Style
from colorama import Fore
import datetime
import time
import json
init()

with open('config.json', 'r') as file:
    config = json.load(file)

owner = config['owner']

def log(a):
    print(f'{Fore.YELLOW}[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [ LOG ] {a}{Fore.WHITE}')

def notification(msg):
    toast = Notification(app_id="Fluoxia", title="Fluoxia", msg=msg)
    toast.set_audio(audio.Default, loop=False) 
    toast.show()

class on_guild_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        bot = self.bot
        user = await bot.fetch_user(owner)
        log(f"Зашел на новый сервер: {guild}")
        notification(f"Зашел на новый сервер {guild}")
        await user.send(f'Зашел на новый сервер🍩\nСервер: {guild}')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} GUILDS"))  

def setup(bot):
    bot.add_cog(on_guild_join(bot))