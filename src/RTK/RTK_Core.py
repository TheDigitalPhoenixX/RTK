# region imports

# region Logging
import logging
import RTK.RTK_Logging as RTK_Logging
import os.path
# endregion Logging

# region RTK

import RTK.RTK_GSpread as RTK_GS

# region CD
import datetime
# endregion CD

# endregion RTK

# endregion imports

# region Constants

FILE_PATH = os.path.realpath(__file__)
ROOT_FOLDER_PATH = FILE_PATH[:-len(os.path.basename(FILE_PATH))]

# region Logging
LOG_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, os.pardir, "logs", f'{__name__}.log')  # TODO Name of the file
# endregion Logging

# region Report
REPORT_CD = 5
# endregion Report

# endregion Constants


# region Logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(RTK_Logging.GetFileHandler(LOG_FILE_PATH))
logger.addHandler(RTK_Logging.GetStreamHandler())
logger.addHandler(RTK_Logging.GetCommonFileHandler())

# endregion Logging

# region Report


def Report(Name):
    assert type(Name) == str,  str(Name) + " isn't a string"

    logger.info("Reporting " + Name)
    if Report_isOnCD(Name):
        logger.info(f"Reporting {Name} is on CD.")
        return -1
    else:
        if ReportsData.get(Name, None) == None:  # TODO EAFP
            ReportsData[Name] = 1
            RTK_GS.addUser(Name, 1)
        else:
            ReportsData[Name] += 1
            RTK_GS.updateReport(Name, ReportsData[Name])

        logger.info(f"{Name} Reported {ReportsData[Name]} times.")
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
    ReportsData_Sorted = sorted(
        ReportsData.items(), key=lambda Item: Item[1], reverse=True)

    logger.info("Returning Sorted Reports data")
    return ReportsData_Sorted
# endregion Report


# region Initialize
ReportsData = {}
LastReportTime = {}

Reports_NoCD = []


def Initialize(NoCDList=[]):  # TODO why does it exist ?
    logger.info("Initializing...")

    global ReportsData
    ReportsData = RTK_GS.getReportsDic()

    global Reports_NoCD
    Reports_NoCD = NoCDList

    logger.info("Finished initializing.")

# endregion Initialize

# region Main


def Main():
    Initialize()

    print(Report_isOnCD("Achilles221B"))
    print(Report_isOnCD("Achilles221B"))

# endregion Main


# region if __main__
if __name__ == "__main__":
    Main()
# endregion if __main__
