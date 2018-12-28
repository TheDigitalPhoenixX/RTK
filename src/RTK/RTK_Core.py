# region imports

# region IO
import json
import pathlib
import datetime
import os.path
# endregion

# region RTK

import RTK.RTK_GSpread as RTK_GS

# endregion

# endregion

# region Constants

SCRIPT_NAME = "RTK_Core"

# region IO

FOLDER_NAME_DATA = "Data"
FILE_NAME_LOG = "RTK_Funcitons_Log.txt"
FILE_NAME_REPORT = "RTK_Reports.json"
FILE_NAME_LOG = "RTK_Log.txt"
#FILE_PATH_LOG = os.path.join(FOLDER_NAME_DATA, FILE_NAME_LOG)

DATETIME_FORMAT_FILE = "%Y-%m-%d %H-%M-%S"

FOLDER_NAME_PREFIX = "FOLDER_NAME"

FOLDERS_TO_CREATE = []
AllVariables = locals()
for Var in list(AllVariables.keys()):
    if Var.startswith(FOLDER_NAME_PREFIX):
        FOLDERS_TO_CREATE.append(AllVariables[Var])
del FOLDERS_TO_CREATE[-1]

# endregion

# region Report
REPORT_CD = 5
# endregion

# endregion


# region IO Functions
def Json_Read(filePath):
    Output_Log("Json_Read: Reading " + filePath)

    with open(filePath) as File:
        data = json.load(File)

    return data
# endregion

# region Logging Functions


def Output_Log(data):
    print(SCRIPT_NAME + " " + data)

    with open(FILE_NAME_LOG, "a") as OutputFile:
        OutputFile.write(
            str(datetime.datetime.now().strftime(DATETIME_FORMAT_FILE)) + ": ")
        OutputFile.write(data + "\n\n")
# endregion

# region Report


def Report(Name):
    assert type(Name) == str,  str(Name) + " isn't a string"

    Output_Log("Reporting " + Name)
    if Report_isOnCD(Name):
        Output_Log("Reporting " + Name + " is on CD")
        return -1
    else:
        if ReportsData.get(Name, None) == None:
            ReportsData[Name] = 1
            RTK_GS.addUser(Name, 1)
        else:
            ReportsData[Name] += 1
            RTK_GS.updateReport(Name, ReportsData[Name])
        Output_Log(Name + " Reported " + str(ReportsData[Name]) + " Times")
        return ReportsData[Name]


def Report_isOnCD(Name):
    if Name in Reports_NoCD:
        return False

    currentTime = datetime.datetime.now()

    isOnCD = LastReportTime.get(
        Name, None) != None and LastReportTime[Name] + datetime.timedelta(seconds=REPORT_CD) > currentTime

    LastReportTime[Name] = currentTime
    return isOnCD


def Reports_LeaderBoard():
    # todo Format
    ReportsData_Sorted = sorted(ReportsData.items(), key=lambda Item: Item[1])
    ReportsData_Sorted.reverse()

    Output_Log("Returning Sorted Reports data (LeaderBoard)")
    return ReportsData_Sorted
# endregion


# region Initialize
ReportsData = {}
LastReportTime = {}

Reports_NoCD = []


def Initialize(NoCDList=[]):
    Output_Log("Initializing...")
    
    global ReportsData
    ReportsData = RTK_GS.getReportsDic()

    global Reports_NoCD
    Reports_NoCD = NoCDList

    Output_Log("Finished initializing.")

# endregion

# region main


def Main():
    Initialize()

    print(Report_isOnCD("Achilles221B"))
    print(Report_isOnCD("Achilles221B"))

# endregion


# region if __main__
if __name__ == "__main__":
    Main()
# endregion
