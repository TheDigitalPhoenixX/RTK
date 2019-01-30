# region Imports

# region Discord

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from os import environ

# endregion Discord

# region Logging
import logging
import RTK.RTK_Logging as RTK_Logging
import os.path
# endregion Logging


# endregion Imports

# region Constants

FILE_PATH = os.path.realpath(__file__)
ROOT_FOLDER_PATH = FILE_PATH[:-len(os.path.basename(FILE_PATH))]

# region Logging
LOG_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, "logs", 'RTK.log')  # TODO Name of the file
# endregion Logging

# region Discord
COMMMAND_PREFIX = "!!"
# endregion Discord

# endregion Constants

# region Logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(RTK_Logging.GetFileHandler(LOG_FILE_PATH))
logger.addHandler(RTK_Logging.GetStreamHandler())
logger.addHandler(RTK_Logging.GetCommonFileHandler())

# endregion Logging

# region initialize

bot = commands.Bot(command_prefix=COMMMAND_PREFIX)
logger.debug("Bot Created")

bot.load_extension('RTK_Commands_Report')
logger.debug("RTK_Commands_Report added")

# endregion initialize

# region Events

@bot.event
async def on_ready():
    logger.info("RTK On")
    logger.info("--------")
    logger.info("Name: " + bot.user.name)
    logger.info("Display Name: " + bot.user.display_name)
    logger.info("ID: " + bot.user.id)
    logger.info("--------")

# endregion Events

# region Commands


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")
    logger.info("user has pinged")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    logger.info(f"{user.name} Requested Info")
    await bot.say("The user's name is: {}".format(user.name))
    await bot.say("The user's nick is: {}".format(user.nick))
    await bot.say("The user's ID is: {}".format(user.id))
    await bot.say("The user's status is: {}".format(user.status))
    await bot.say("The user's highest role is: {}".format(user.top_role))
    await bot.say("The user's joined at: {}".format(user.joined_at))

# endregion Commands

bot.run(str(os.environ.get("API_KEY")))


# TODO only accept from rtk
# TODO Shine
# TODO fix Delay
# TODO Support for multple servers
# TODO better CD
# TODO Restart or shutdown Bot