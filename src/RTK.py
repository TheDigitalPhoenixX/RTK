# region Imports

# region Discord

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

# endregion

import os
import sys
import datetime

# endregion

# region Constants

COMMMAND_PREFIX = "!!"

# endregion

# region initialize

bot = commands.Bot(command_prefix=COMMMAND_PREFIX)

bot.load_extension('RTK_Commands_Report')

# endregion

# region Events

@bot.event
async def on_ready():
    print("--------")
    print("Name: " + bot.user.name)
    print("ID: " + bot.user.id)
    print("--------")

# endregion

# region Commands


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

# endregion

#region Run Bot
bot.run(str(os.environ.get("API_KEY")))
# endregion

# todo
# only accept from rtk
# wrong command
# @everyone
# Shine
# Delay
# Support for multple servers
# CD
# Logging
# Restart or shutdown Bot