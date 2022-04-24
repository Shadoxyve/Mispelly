import discord
import sys
import os
from dotenv import load_dotenv
from discord.ext import commands

# Gets the token from .env file
load_dotenv()
token = os.getenv('TOKEN')

# Loads the Intents
intents = discord.Intents.all()

# Disables Log writing of python
sys.dont_write_bytecode = True

# Bot Command prefix and default status
bot = commands.Bot(command_prefix='-', intents=intents, status=discord.Status.dnd, activity = discord.Activity(type=discord.ActivityType.watching, name="your soul"))

# Remove's default Help command
bot.remove_command("help") 

# Loads AutoMod Events and Commands
for filename in os.listdir("./AutoMod"):
        if filename.endswith('.py'):
            bot.load_extension(f'AutoMod.{filename[:-3]}')

# Loads Giveaways Commands and Events
for filename in os.listdir("./Giveaway"):
        if filename.endswith('.py'):
            bot.load_extension(f'Giveaway.{filename[:-3]}')

# Loads Logging Events
for filename in os.listdir("./Logger"):
        if filename.endswith('.py'):
            bot.load_extension(f'Logger.{filename[:-3]}')

# Loads Extra Commands
for filename in os.listdir("./Miscellaneous"):
        if filename.endswith('.py'):
            bot.load_extension(f'Miscellaneous.{filename[:-3]}')

# Loads Moderation Commands and Events
for filename in os.listdir("./Moderation"):
        if filename.endswith('.py'):
            bot.load_extension(f'Moderation.{filename[:-3]}')

# Loads Ticket Commands and Events
for filename in os.listdir("./Tickets"):
        if filename.endswith('.py'):
            bot.load_extension(f'Tickets.{filename[:-3]}')

# Loads Verification Commands and Events
for filename in os.listdir("./Verify"):
        if filename.endswith('.py'):
            bot.load_extension(f'Verify.{filename[:-3]}')

bot.run(token)