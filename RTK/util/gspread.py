
"""Report To Kill Google Spread module.

This module allows RTK scripts to communicate with google sheets to save report records.
"""

import os
from ast import literal_eval

from google.oauth2.service_account import Credentials

import gspread

GSPREAD_CLIENT_SECRET = os.getenv("GSPREAD_CLIENT_SECRET")

WORKSHEET_NAME = "RTK"

SHEET_NAMES_ROW_NUM = 1
SHEET_REPORTS_ROW_NUM = 2


scope = ['https://spreadsheets.google.com/feeds',
         # 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_info(
    literal_eval(GSPREAD_CLIENT_SECRET), scopes=scope)
client = gspread.authorize(creds)
worksheet = client.open(WORKSHEET_NAME).sheet1


def getReportsDic():
    """
    Returns a dictionary containing the reports counts of the users.

    Parameters:
        None

    Returns:
        Dictionary: key: username.
                    value: report count.

    Raises:
        None
    """

    return worksheet.get_all_records()[0]


def addUser(name, value):
    """
    Adds the given name as a user with the given value as his/her report count.

    Parameters:
        name (str): the username to add.
        value (int): the value to set for the given username.

    Returns:
        None

    Raises:
        None
    """
    NewUserCol = len(getReportsDic()) + 1

    worksheet.add_cols(1)

    worksheet._properties['gridProperties']['columnCount'] += 1
    worksheet.update_cell(SHEET_NAMES_ROW_NUM, NewUserCol, name)
    worksheet.update_cell(SHEET_REPORTS_ROW_NUM, NewUserCol, value)


def updateReport(name, newValue):
    """
    Updates the report count of the given name.

    Parameters:
        name (str): the username to update.
        newValue (int): the updated value to set for the given username.

    Returns:
        None

    Raises:
        None
    """
    worksheet.update_cell(SHEET_REPORTS_ROW_NUM,
                          worksheet.find(name).col, newValue)


client.login()
