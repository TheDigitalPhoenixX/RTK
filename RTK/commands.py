
import json

import discord
from discord.ext import commands

import RTK.core as RTK_Core
import RTK.util.localization as RTK_Localization


RESPONSES = RTK_Localization.GetLocalizedText()

RESPONSES_KEY_REPORTED = "Reported"
RESPONSES_KEY_REPORT_COUNT = "ReportCount"
RESPONSES_KEY_REPORT_ON_CD = "ReportOnCD"
RESPONSES_KEY_LEADERBOARD = "ReportsLeaderBoard"

EXEC_TEMPLATE = """
@commands.command(name="Report{name}", description="Reports {value}", brief="Reports {value}", aliases=["report"+"{name}", "Report"+"{name}".lower(), "report"+"{name}".lower()])
async def Report{name}(self, context):

    ReportCount = RTK_Core.Report("{value}")

    if ReportCount == -1:
        msg = RESPONSES[RESPONSES_KEY_REPORT_ON_CD].format("{value}")
    else:
        msg = RESPONSES[RESPONSES_KEY_REPORTED].format("{value}") + "\\n" + RESPONSES[RESPONSES_KEY_REPORT_COUNT].format("{value}", ReportCount)

    await context.send(msg)"""

LEADERBOARD_REPORTS_EXTRA_PADDING = 1
LEADERBOARD_FORMAT = "#{Numbering:{NumberingWidth}d} {Reports:{ReportsWidth}d} {name} \n"


with open("data/ReportCustom.json") as RepCustomFile:
    ReportCustom = json.load(RepCustomFile)

RTK_Core.Initialize([ReportCustom["Uni"]])


class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Report", description="Reports someone in the server.\n u can use @ or write his name.", brief="Reports someone in the server", aliases=["report"], pass_context=True)
    async def Report(self, context, user: discord.Member):
        username = user.name

        ReportCount = RTK_Core.Report(username)

        if user.nick != None:
            username = user.nick

        if ReportCount == -1:
            msg = RESPONSES[RESPONSES_KEY_REPORT_ON_CD].format(
                username)
        else:
            msg = RESPONSES[RESPONSES_KEY_REPORTED].format(
                username) + '\n' + RESPONSES[RESPONSES_KEY_REPORT_COUNT].format(username, ReportCount)

        await context.send(msg)

    @commands.command(name="Reports_LeaderBoard", description="Displays reports leader board", brief="Displays reports leader board", aliases=["ReportsLeaderBoard", "ReportsLB", "Reportsleaderboard", "ReportsLeaderboard", "reportsLeaderBoard", "reportsleaderboard"])
    async def Reports_LeaderBoard(self):
        ReportCount = RTK_Core.leaderBoard()
        HighestNumOfDigits_Reports = LEADERBOARD_REPORTS_EXTRA_PADDING + \
            len(str(ReportCount[0][1]))
        HighestNumOfDigits_Numbering = len(str(len(ReportCount)))

        StringToPrint = ""
        for UserNum in range(len(ReportCount)):
            StringToPrint += LEADERBOARD_FORMAT.format(Numbering=UserNum+1, NumberingWidth=HighestNumOfDigits_Numbering,
                                                       name=ReportCount[UserNum][0], Reports=ReportCount[UserNum][1], ReportsWidth=HighestNumOfDigits_Reports)

        await self.bot.say(RESPONSES[RESPONSES_KEY_LEADERBOARD] + '\n' + StringToPrint)

    @commands.command(name="Report_Custom", description="Reports smth", brief="Reports smth", aliases=["report_custom", "ReportCustom", "reportcustom"])
    async def Report_Custom(self, Name: str):
        Name = Name.lower()

        ReportCount = RTK_Core.Report(Name)

        if ReportCount == -1:
            StringToPrint = RESPONSES[RESPONSES_KEY_REPORT_ON_CD].format(Name)
        else:
            StringToPrint = RESPONSES[RESPONSES_KEY_REPORTED].format(
                Name) + '\n' + RESPONSES[RESPONSES_KEY_REPORT_COUNT].format(Name, ReportCount)

        await self.bot.say(StringToPrint)

    for CustomName, CustomValue in ReportCustom.items():
        exec(EXEC_TEMPLATE.format(name=CustomName, value=CustomValue))


def setup(bot):
    bot.add_cog(Report(bot))
