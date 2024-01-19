import discord
from discord.ext import commands
from colorama import Fore
import json
import datetime

with open('config.json', 'r') as file:
    config = json.load(file)

owner = config['owner'] # откройте личку чтобы бот вам мог писать

def log(a):
    print(f'{Fore.YELLOW}[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [ LOG ] {a}{Fore.WHITE}')

log("Загрузка...")

class on_ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        bot = self.bot
        print(f"""
    {Fore.MAGENTA} /$$$$$$$$ /$$                               /$$          
    | $$_____/| $$                              |__/          
    | $$      | $$ /$$   /$$  /$$$$$$  /$$   /$$ /$$  /$$$$$$ 
    | $$$$$   | $$| $$  | $$ /$$__  $$|  $$ /$$/| $$ |____  $$
    | $$__/   | $$| $$  | $$| $$  \ $$ \  $$$$/ | $$  /$$$$$$$
    | $$      | $$| $$  | $$| $$  | $$  >$$  $$ | $$ /$$__  $$
    | $$      | $$|  $$$$$$/|  $$$$$$/ /$$/\  $$| $$|  $$$$$$$
    |__/      |__/ \______/  \______/ |__/  \__/|__/ \_______/                                                                                                                                                                             """)
        user = await bot.fetch_user(owner)
        await user.send(f'Включение 🔓\nБот успешно включился, смотрит {len(bot.guilds)} серверов')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"{len(bot.guilds)} GUILDS", url="https://twitch.tv/404"))
        log(f"Работаю под {bot.user}, смотрю {len(bot.guilds)} серверов")   

def setup(bot):
    bot.add_cog(on_ready(bot))