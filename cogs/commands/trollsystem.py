from discord.ext import commands
import datetime
from colorama import init
from colorama import Fore, Back, Style
from colorama import Fore
import random
import time
from winotify import Notification, audio
import json

with open('config.json', 'r') as file:
    config = json.load(file)

delay = config['delay']
phrases_file = config['phrases_file']

phrases_open = open(phrases_file, 'r', encoding='utf-8')
phrases = phrases_open.read().splitlines()
phrases = list(filter(None, phrases))
random.shuffle(phrases)

trolllist = []

emojis = [" "]

def log(a):
    print(f'{Fore.YELLOW}[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [ LOG ] {a}{Fore.WHITE}')

def notification(msg):
    toast = Notification(app_id="Fluoxia", title="Fluoxia", msg=msg)
    toast.set_audio(audio.Default, loop=False) 
    toast.show()

class troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def troll(self, ctx, victim):
        await ctx.message.delete()
        if victim in trolllist:
            log(f"Невозможно добавить {victim} в список: цель уже находится в списке")
            await ctx.send(f"Невозможно добавить {victim} в список: цель уже находится в списке")
        else:
            trolllist.append(victim)
            log(f"Добавил {victim}")
            await ctx.send(f"Добавил {victim}")   

    @commands.command()
    async def untroll(self, ctx, victim):
        await ctx.message.delete()
        if victim in trolllist:
            trolllist.remove(victim)
            log(f"Удалил {victim}")
            await ctx.send(f"Удалил {victim}")
        else:
            log(f"Невозможно удалить {victim} из списка: цель отсутствует в списке")
            await ctx.send(f"Невозможно удалить {victim} из списка: цель отсутствует в списке")

    @commands.command()
    async def setdelay(self, ctx, delay):
        await ctx.message.delete()
        delay = delay
        log(f"Установлена задержка: {delay}ms")
        await ctx.send(f"Установлена задержка: {delay}ms")

    @commands.command()
    async def listTrolls(self, ctx):
        await ctx.message.delete()
        message = "Список:\n"
        for troll in trolllist:
            message += troll + "\n"
        log(message)
        await ctx.send(message)

    @commands.command()
    async def clearTrolls(self, ctx):
        await ctx.message.delete()
        trolllist.clear()
        log("Список людей успешно очищен")
        await ctx.send("Список людей успешно очищен")

    @commands.command()
    async def enable(self, ctx):
        await ctx.message.delete()
        while trolllist:
            phrase = random.choice(trolllist) + " " + random.choice(phrases) + " " + random.choice(emojis)
            await ctx.send(phrase)
            time.sleep(int(delay)/1000)
        if not trolllist:
            log("В списке людей пусто, выключаем...")
            await ctx.send("В списке людей пусто, выключаем...")

    @commands.command()
    async def disable(self, ctx):
        await ctx.message.delete()
        log("Выключаем...")
        notification("Выключаем...")
        trolllist.clear()

    @commands.command()
    async def addemoji(self, ctx):
        emojis.append("🍫")
        emojis.append("🍩")
        await ctx.message.add_reaction('✅')

    @commands.command()
    async def enableone(self, ctx):
        await ctx.send("Продолжите писать в консоли")
        input1 = input(f"Введите слово: ")
        await ctx.message.delete()
        while trolllist:
            phrase = f"{random.choice(trolllist)} {input1}"
            await ctx.send(phrase)
            time.sleep(int(delay)/1000)
        if not trolllist:
            log("В списке людей пусто, выключаем...")
            await ctx.send("В списке людей пусто, выключаем...")

    @commands.command()
    async def enableemoji(self, ctx):
        emojis.append("🍫")
        emojis.append("🍩")
        await ctx.message.delete()
        while trolllist:
            phrase = f"{random.choice(trolllist)} {random.choice(emojis)}"
            await ctx.send(phrase)
            time.sleep(int(delay)/1000)
        if not trolllist:
            log("В списке людей пусто, выключаем...")
            await ctx.send("В списке людей пусто, выключаем...")

def setup(bot):
    bot.add_cog(troll(bot))