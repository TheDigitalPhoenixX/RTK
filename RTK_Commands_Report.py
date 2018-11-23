# Imports
import discord
from discord.ext import commands

import RTK_Functions
# end of Imports

# Constants
TEXT_FORMAT_REPORTED = ":right_facing_fist: {} Reported :left_facing_fist:"
TEXT_FORMAT_REPORT_COUNT = "{} has been reported {} times."

TEXT_FORMAT_REPORT_ON_CD = "You just reported {}, You can't report him right now."


# Constants: Custom

REPORT_CUSTOM_SAMEH = "Achilles221B"
REPORT_CUSTOM_RIOT = "Riot"
REPORT_CUSTOM_UNI = "Ain Shams University Faculty of Engineering"
REPORT_CUSTOM_BOT = "RTK BOT"

# end of Constants: Custom
# end of Constants

# Initialize
RTK_Functions.Initialize([REPORT_CUSTOM_UNI])
# end of Initialize


class Report:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Report", description="Reports someone in the server.\n u can use @ or write his name.", brief="Reports someone in the server", aliases=["report"], pass_context=True)
    async def Report(self, ctx, user: discord.Member):  # ! what's ':'
        # todo CD
        # todo Log Requester and rep count
        username = user.name
        ReportCount = RTK_Functions.Report(username)

        if user.nick != None:
            username = user.nick

        if ReportCount == -1:
            await self.bot.say(TEXT_FORMAT_REPORT_ON_CD.format(username))
        else:

            await self.bot.say(TEXT_FORMAT_REPORTED.format(username))
            await self.bot.say(TEXT_FORMAT_REPORT_COUNT.format(username, ReportCount))

    @commands.command(name="Reports_LeaderBoard", description="Displays reports leader board", brief="Displays reports leader board", aliases=["ReportsLeaderBoard", "ReportsLB", "Reportsleaderboard", "ReportsLeaderboard", "reportsLeaderBoard", "reportsleaderboard"])
    async def Reports_LeaderBoard(self, ):
        # todo server name
        await self.bot.say(RTK_Functions.Reports_LeaderBoard())

    # Commands: Report: Custom

    @commands.command(name="Report_Custom", description="Reports smth", brief="Reports smth", aliases=["report_custom", "ReportCustom", "reportcustom"])
    async def Report_Custom(self, Name: str):
        Name = Name.lower()
        ReportCount = RTK_Functions.Report(Name)

        if ReportCount == -1:
            await self.bot.say(TEXT_FORMAT_REPORT_ON_CD.format(Name))
        else:

            await self.bot.say(TEXT_FORMAT_REPORTED.format(Name))
            await self.bot.say(TEXT_FORMAT_REPORT_COUNT.format(Name, ReportCount))

    @commands.command(name="ReportRiot", description="Reports " + REPORT_CUSTOM_RIOT , brief="Reports " + REPORT_CUSTOM_RIOT, aliases=["Reportriot", "reportRiot", "reportriot"])
    async def ReportRiot(self):  # ! Call Report_Custom
        ReportCount = RTK_Functions.Report(REPORT_CUSTOM_RIOT)

        if ReportCount == -1:
            await self.bot.say(TEXT_FORMAT_REPORT_ON_CD.format(REPORT_CUSTOM_RIOT))
        else:

            await self.bot.say(TEXT_FORMAT_REPORTED.format(REPORT_CUSTOM_RIOT))
            await self.bot.say(TEXT_FORMAT_REPORT_COUNT.format(REPORT_CUSTOM_RIOT, ReportCount))

    @commands.command(name="ReportUni", description="Reports " + REPORT_CUSTOM_UNI, brief="Reports " + REPORT_CUSTOM_UNI, aliases=["Reportuni", "reportUni", "reportuni"])
    async def ReportUni(self):  # ! Call Report_Custom
        ReportCount = RTK_Functions.Report(REPORT_CUSTOM_UNI)

        if ReportCount == -1:
            await self.bot.say(TEXT_FORMAT_REPORT_ON_CD.format(REPORT_CUSTOM_UNI))
        else:

            await self.bot.say(TEXT_FORMAT_REPORTED.format(REPORT_CUSTOM_UNI))
            await self.bot.say(TEXT_FORMAT_REPORT_COUNT.format(REPORT_CUSTOM_UNI, ReportCount))

    @commands.command(name="ReportSameh", description="Reports " + REPORT_CUSTOM_SAMEH, brief="Reports " + REPORT_CUSTOM_SAMEH, aliases=["Reportsameh", "reportSameh", "reportsameh"])
    async def ReportSameh(self):  # ! Call Report_Custom
        ReportCount = RTK_Functions.Report(REPORT_CUSTOM_SAMEH)

        if ReportCount == -1:
            await self.bot.say(TEXT_FORMAT_REPORT_ON_CD.format(REPORT_CUSTOM_SAMEH))
        else:

            await self.bot.say(TEXT_FORMAT_REPORTED.format(REPORT_CUSTOM_SAMEH))
            await self.bot.say(TEXT_FORMAT_REPORT_COUNT.format(REPORT_CUSTOM_SAMEH, ReportCount))

    @commands.command(name="ReportBot", description="Reports " + REPORT_CUSTOM_BOT, brief="Reports " + REPORT_CUSTOM_BOT, aliases=["reportBot", "Reportbot", "reportbot"])
    async def ReportBot(self):  # ! Call Report_Custom
        ReportCount = RTK_Functions.Report(REPORT_CUSTOM_BOT)

        if ReportCount == -1:
            await self.bot.say(TEXT_FORMAT_REPORT_ON_CD.format(REPORT_CUSTOM_BOT))
        else:

            await self.bot.say(TEXT_FORMAT_REPORTED.format(REPORT_CUSTOM_BOT))
            await self.bot.say(TEXT_FORMAT_REPORT_COUNT.format(REPORT_CUSTOM_BOT, ReportCount))


def setup(bot):
    bot.add_cog(Report(bot))
