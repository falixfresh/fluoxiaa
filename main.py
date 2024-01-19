# fluoxia v0.1

try:
    from discord.ext import commands
    import json
except:
    print("для работы нужен discord.py 1.7.3")
    print("команда чтобы установить > pip install discord.py==1.7.3 discord==1.7.3 ")

with open('config.json', 'r') as file:
    config = json.load(file)

token = config['token']
prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, help_command=None, self_bot=True)

def load():
    bot.load_extension("cogs.test")
    bot.load_extension("cogs.events.on_ready")
    bot.load_extension("cogs.events.on_guild_join")
    bot.load_extension("cogs.events.on_guild_remove")
    bot.load_extension("cogs.commands.ping")
    bot.load_extension("cogs.commands.help")
    bot.load_extension("cogs.commands.changerpc")
    bot.load_extension("cogs.commands.message")
    bot.load_extension("cogs.commands.killchat")
    bot.load_extension("cogs.commands.guildleave")
    bot.load_extension("cogs.commands.trollsystem")

load()

bot.run(token, bot=False)
