# region Imports

import json

# region Discord

import discord
from discord.ext import commands

# endregion

# region RTK

import RTK.RTK_Core as RTK_Core
import RTK.RTK_Localization

# endregion

# endregion

# region Constants

# region Responses

RESPONSES = RTK.RTK_Localization.GetLocalizedText()

RESPONSES_REPORTED = "Reported"
RESPONSES_REPORT_COUNT = "ReportCount"
RESPONSES_REPORT_ON_CD = "ReportOnCD"
RESPONSES_LEADERBOARD = "ReportsLeaderBoard"

# endregion

# region Custom

REPORT_CUSTOM_FILE_PATH = r"src\RTK\data\ReportCustom.json"

# ! Call Report_Custom
EXEC_TEMPLATE = """
@commands.command(name="Report{name}", description="Reports {value}", brief="Reports {value}", aliases=["report"+"{name}", "Report"+"{name}".lower(), "report"+"{name}".lower()])
async def Report{name}(self):
    ReportCount = RTK_Core.Report("{value}")

    if ReportCount == -1:
        await self.bot.say(RESPONSES[RESPONSES_REPORT_ON_CD].format("{value}"))
    else:
        await self.bot.say(RESPONSES[RESPONSES_REPORTED].format("{value}"))
        await self.bot.say(RESPONSES[RESPONSES_REPORT_COUNT].format("{value}", ReportCount))"""

# REPORT_CUSTOM_SAMEH = "Achilles221B"
# REPORT_CUSTOM_RIOT = "Riot"
REPORT_CUSTOM_UNI = "Ain Shams University Faculty of Engineering"
# REPORT_CUSTOM_BOT = "RTK BOT"

# endregion

# region LeaderBoard
LEADERBOARD_REPORTS_EXTRA_PADDING = 1
LEADERBOARD_FORMAT = "#{Numbering:{NumberingWidth}d} {Reports:{ReportsWidth}d} {name} \n"
# endregion

# endregion

# region Initialize
RTK_Core.Initialize([REPORT_CUSTOM_UNI])
with open(REPORT_CUSTOM_FILE_PATH) as RepCustomFile:
    ReportCustom = json.load(RepCustomFile)
# endregion

# region Report


class Report:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Report", description="Reports someone in the server.\n u can use @ or write his name.", brief="Reports someone in the server", aliases=["report"], pass_context=True)
    async def Report(self, ctx, user: discord.Member):  # ! what's ':'
        # todo CD
        # todo Log Requester and rep count
        username = user.name
        ReportCount = RTK_Core.Report(username)

        if user.nick != None:
            username = user.nick

        if ReportCount == -1:
            await self.bot.say(RESPONSES[RESPONSES_REPORT_ON_CD].format(username))
        else:

            await self.bot.say(RESPONSES[RESPONSES_REPORTED].format(username))
            await self.bot.say(RESPONSES[RESPONSES_REPORT_COUNT].format(username, ReportCount))

    @commands.command(name="Reports_LeaderBoard", description="Displays reports leader board", brief="Displays reports leader board", aliases=["ReportsLeaderBoard", "ReportsLB", "Reportsleaderboard", "ReportsLeaderboard", "reportsLeaderBoard", "reportsleaderboard"])
    async def Reports_LeaderBoard(self, ):
        # todo server name
        StringToPrint = ""
        ReportCount = RTK_Core.Reports_LeaderBoard()
        HighestNumOfDigits_Reports = LEADERBOARD_REPORTS_EXTRA_PADDING + \
            len(str(ReportCount[0][1]))
        HighestNumOfDigits_Numbering = len(str(len(ReportCount)))
        for UserNum in range(len(ReportCount)):
            StringToPrint += LEADERBOARD_FORMAT.format(Numbering=UserNum+1, NumberingWidth=HighestNumOfDigits_Numbering,
                                                       name=ReportCount[UserNum][0], Reports=ReportCount[UserNum][1], ReportsWidth=HighestNumOfDigits_Reports)
        await self.bot.say(RESPONSES[RESPONSES_LEADERBOARD])
        await self.bot.say(StringToPrint)

    # Commands: Report: Custom

    @commands.command(name="Report_Custom", description="Reports smth", brief="Reports smth", aliases=["report_custom", "ReportCustom", "reportcustom"])
    async def Report_Custom(self, Name: str):
        Name = Name.lower()
        ReportCount = RTK_Core.Report(Name)

        if ReportCount == -1:
            await self.bot.say(RESPONSES[RESPONSES_REPORT_ON_CD].format(Name))
        else:
            await self.bot.say(RESPONSES[RESPONSES_REPORTED].format(Name))
            await self.bot.say(RESPONSES[RESPONSES_REPORT_COUNT].format(Name, ReportCount))

    for custom in ReportCustom:
        exec(EXEC_TEMPLATE.format(name=custom, value=ReportCustom[custom]))
# endregion


def setup(bot):
    bot.add_cog(Report(bot))

# Todo Async ???
