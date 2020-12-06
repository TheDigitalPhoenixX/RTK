
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

COMMMAND_PREFIX = "!!"

bot = commands.Bot(command_prefix=COMMMAND_PREFIX)

bot.load_extension('RTK.commands')

bot.run(API_KEY)
