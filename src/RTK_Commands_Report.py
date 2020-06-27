# region Imports

import json
import os.path

# region Discord

import discord
from discord.ext import commands

# endregion

# region RTK

import RTK.RTK_Core as RTK_Core
import RTK.RTK_Localization as RTK_Localization

# endregion

# region Logging
import logging
import RTK.RTK_Logging as RTK_Logging
# endregion Logging

# endregion Imports

# region Constants

FILE_PATH = os.path.realpath(__file__)
ROOT_FOLDER_PATH = FILE_PATH[:-len(os.path.basename(FILE_PATH))]

# region Logging
LOG_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, "logs", f'{__name__}.log')  # TODO Name of the file
# endregion Logging

# region Responses

RESPONSES = RTK_Localization.GetLocalizedText()

RESPONSES_KEY_REPORTED = "Reported"
RESPONSES_KEY_REPORT_COUNT = "ReportCount"
RESPONSES_KEY_REPORT_ON_CD = "ReportOnCD"
RESPONSES_KEY_LEADERBOARD = "ReportsLeaderBoard"

# endregion Responses

# region Custom

REPORT_CUSTOM_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, "RTK/data/ReportCustom.json")

# TODO Call Report_Custom
EXEC_TEMPLATE = """
@commands.command(name="Report{name}", description="Reports {value}", brief="Reports {value}", aliases=["report"+"{name}", "Report"+"{name}".lower(), "report"+"{name}".lower()])
async def Report{name}(self):
    logger.info("Reporing {name} : {value}")
    ReportCount = RTK_Core.Report("{value}")

    if ReportCount == -1:
        StringToPrint = RESPONSES[RESPONSES_KEY_REPORT_ON_CD].format("{value}")
    else:
        StringToPrint = RESPONSES[RESPONSES_KEY_REPORTED].format("{value}") + "\\n" + RESPONSES[RESPONSES_KEY_REPORT_COUNT].format("{value}", ReportCount)

    logger.info(f"Saying {{StringToPrint}}")
    await self.bot.say(StringToPrint)"""

# endregion Custom

# region LeaderBoard
LEADERBOARD_REPORTS_EXTRA_PADDING = 1
LEADERBOARD_FORMAT = "#{Numbering:{NumberingWidth}d} {Reports:{ReportsWidth}d} {name} \n"
# endregion LeaderBoard

# endregion Constants

# region Logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(RTK_Logging.GetFileHandler(LOG_FILE_PATH))
logger.addHandler(RTK_Logging.GetStreamHandler())
logger.addHandler(RTK_Logging.GetCommonFileHandler())

# endregion Logging

# region Initialize

with open(REPORT_CUSTOM_FILE_PATH) as RepCustomFile:
    ReportCustom = json.load(RepCustomFile)
    logger.debug("Loaded CustomReports json")
RTK_Core.Initialize([ReportCustom["Uni"]])  # TODO is it needed ?
# TODO Load Exceptions from a file

# endregion Initialize

# region Report


class Report:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Report", description="Reports someone in the server.\n u can use @ or write his name.", brief="Reports someone in the server", aliases=["report"], pass_context=True)
    async def Report(self, ctx, user: discord.Member):  # ! what's ':'
        username = user.name
        logger.info(f"Reporing {username} (nick: {user.nick})")
        ReportCount = RTK_Core.Report(username)

        if user.nick != None:
            username = user.nick

        if ReportCount == -1:
            StringToPrint = RESPONSES[RESPONSES_KEY_REPORT_ON_CD].format(username)
        else:
            StringToPrint = RESPONSES[RESPONSES_KEY_REPORTED].format(username) + '\n' + RESPONSES[RESPONSES_KEY_REPORT_COUNT].format(username, ReportCount)

        logger.info(f"Saying {StringToPrint}")
        await self.bot.say(StringToPrint)

    @commands.command(name="Reports_LeaderBoard", description="Displays reports leader board", brief="Displays reports leader board", aliases=["ReportsLeaderBoard", "ReportsLB", "Reportsleaderboard", "ReportsLeaderboard", "reportsLeaderBoard", "reportsleaderboard"])
    async def Reports_LeaderBoard(self):
        # TODO server name
        ReportCount = RTK_Core.Reports_LeaderBoard()
        HighestNumOfDigits_Reports = LEADERBOARD_REPORTS_EXTRA_PADDING + \
            len(str(ReportCount[0][1]))
        HighestNumOfDigits_Numbering = len(str(len(ReportCount)))

        StringToPrint = ""
        for UserNum in range(len(ReportCount)):
            StringToPrint += LEADERBOARD_FORMAT.format(Numbering=UserNum+1, NumberingWidth=HighestNumOfDigits_Numbering,
                                                       name=ReportCount[UserNum][0], Reports=ReportCount[UserNum][1], ReportsWidth=HighestNumOfDigits_Reports)
        
        await self.bot.say(RESPONSES[RESPONSES_KEY_LEADERBOARD] + '\n' + StringToPrint)

    # Commands: Report: Custom

    @commands.command(name="Report_Custom", description="Reports smth", brief="Reports smth", aliases=["report_custom", "ReportCustom", "reportcustom"])
    async def Report_Custom(self, Name: str):
        Name = Name.lower()
        logger.info(f"Custom Reporing {Name}")
        ReportCount = RTK_Core.Report(Name)

        if ReportCount == -1:
            StringToPrint = RESPONSES[RESPONSES_KEY_REPORT_ON_CD].format(Name)
        else:
            StringToPrint = RESPONSES[RESPONSES_KEY_REPORTED].format(Name) + '\n' + RESPONSES[RESPONSES_KEY_REPORT_COUNT].format(Name, ReportCount)

        logger.info(f"Saying {StringToPrint}")
        await self.bot.say(StringToPrint)

    for CustomName, CustomValue in ReportCustom.items():
        exec(EXEC_TEMPLATE.format(name=CustomName, value=CustomValue))
        logger.info(f"Added Custom Report: {CustomName}: {CustomValue}")
# endregion Report


def setup(bot):
    bot.add_cog(Report(bot))

# Todo Async ???
