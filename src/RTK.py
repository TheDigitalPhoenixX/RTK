# region Imports
# endregion

# Imports

# Imports: Discord

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

# end of Imports: Discord

import os
import sys
import datetime

# end of Imports

# Constants

#Constants: bot


COMMMAND_PREFIX = "!!"
# end of Constants: bot



# initialize

bot = commands.Bot(command_prefix=COMMMAND_PREFIX)

bot.load_extension('RTK_Commands_Report')


# end of initialize

# Events


@bot.event
async def on_ready():
    print("--------")
    print("Name: " + bot.user.name)
    print("ID: " + bot.user.id)
    print("--------")

# end of Events

# Commands


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong:")
    print("user has pinged")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users nick is: {}".format(user.nick))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))


#Commands: Kill

# end of Commands: Kill

# Commands: Exit

# @bot.command()
# async def GoAway():
#     await bot.say(":wave:")
#     bot.
#     sys.exit(1)

# end of Commands: Exit

# end of Commands

# Run bot

# bot.run(API_KEY)

bot.run(str(os.environ.get("API_KEY")))

# end of Run bot

# todo
# in and out msg
# help
# only accept from rtk
# wrong command
# @everyone
# Shine
# Delay
# report life
# Support for multple servers
# report dogs


# cd

# Logging
