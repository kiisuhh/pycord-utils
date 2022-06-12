print("[ + ] Starting...")
print("[ + ] Loading libs...")

from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from discord.ui import View, Button
from dbutil import create_db

print("[ + ] Loading enviroment variables...")

load_dotenv()


bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.all())
bot.remove_command("help")

print("[ + ] Connecting to Discord...")
@bot.event
async def on_ready():
    print("[ + ] Setting Status Message...")
    user = 0
    server = 0
    for guild in bot.guilds:
        server += 1
        user += len(guild.members)
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=f"!help | {user:,} User")
    )
    print("[ + ] Connecting to Database...")
    await create_db()

    print(f"-------------------------------\n"
          f"[ + ] Bot connected to Discord\n"
          f"> User: {bot.user.name}#{bot.user.discriminator}\n"
          f"> ID: {bot.user.id}\n"
          f"----------- ⮟ Log ⮟ ----------")

print("[ + ] Loading cogs...")
cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir("cogs/") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)

print("[ + ] Loading complete!")

#bot.run(os.getenv("TOKEN"))
bot.run(os.getenv("TESTTOKEN"))
