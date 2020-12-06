import datetime

import RTK.util.gspread as RTK_GS

REPORT_CD = 1


def Report(Name):
    if isOnCD(Name):
        return -1
    else:
        if not ReportsData.get(Name, None):
            ReportsData[Name] = 1
            RTK_GS.addUser(Name, 1)
        else:
            ReportsData[Name] += 1
            RTK_GS.updateReport(Name, ReportsData[Name])
        LastReportTime[Name] = datetime.datetime.now()
        return ReportsData[Name]


def isOnCD(Name):
    return Name not in Reports_NoCD and \
        LastReportTime.get(Name, None) != None and \
        LastReportTime[Name] + \
        datetime.timedelta(seconds=REPORT_CD) > datetime.datetime.now()


def leaderBoard():
    ReportsData_Sorted = sorted(
        ReportsData.items(), key=lambda Item: Item[1], reverse=True)

    return ReportsData_Sorted


ReportsData = {}
LastReportTime = {}

Reports_NoCD = []


def Initialize(NoCDList=[]):

    global ReportsData
    ReportsData = RTK_GS.getReportsDic()

    global Reports_NoCD
    Reports_NoCD = NoCDList
