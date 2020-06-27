# https://github.com/burnash/gspread

"""Report To Kill Google Spread module.

This module allows RTK scripts to communicate with google sheets to save report records.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""

# region Imports

# region Logging
import logging
import RTK.RTK_Logging as RTK_Logging
# endregion Logging

# region Gspread

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# endregion Gspread

from os import environ
from ast import literal_eval
import os.path

# endregion Imports

# region Constants

# region GSpread
WORKSHEET_NAME = "RTK"

SHEET_NAMES_ROW_NUM = 1
SHEET_REPORTS_ROW_NUM = 2
# endregion GSpread

FILE_PATH = os.path.realpath(__file__)
ROOT_FOLDER_PATH = FILE_PATH[:-len(os.path.basename(FILE_PATH))]

# region Logging
LOG_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, os.pardir, "logs", f'{__name__}.log')  # TODO Name of the file
# endregion Logging

# endregion Constants

# region Logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(RTK_Logging.GetFileHandler(LOG_FILE_PATH))
logger.addHandler(RTK_Logging.GetStreamHandler())
logger.addHandler(RTK_Logging.GetCommonFileHandler())

# endregion Logging

# region Initialize

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(literal_eval(environ.get("GSPREAD_CLIENT_SECRET")), scope)
client = gspread.authorize(creds)
worksheet = client.open(WORKSHEET_NAME).sheet1

# endregion Initialize

# region Functions

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
    logger.debug("Returning Reports Dic")
    try:
        return worksheet.get_all_records()[0]
    except gspread.exceptions.APIError:
        client.login()
        logger.exception("gspread.exceptions.APIError Caught")
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
    NewUserCol = len(getReportsDic()) + 1 # TODO a lot of calls
    try:
        # logger.debug(f"Before: {worksheet.col_count}")
        worksheet.add_cols(1)
        # temp = worksheet.resize(cols=worksheet.col_count + 1)
        # logger.debug(temp)
        worksheet._properties['gridProperties']['columnCount'] += 1
        worksheet.update_cell(SHEET_NAMES_ROW_NUM, NewUserCol, name)
        worksheet.update_cell(SHEET_REPORTS_ROW_NUM, NewUserCol, value)
        # logger.debug(f"After: {worksheet.col_count}")
    except gspread.exceptions.APIError:
        logger.exception("gspread.exceptions.APIError Caught")
        client.login()
        worksheet.add_cols(1)
        worksheet._properties['gridProperties']['columnCount'] += 1
        worksheet.update_cell(SHEET_NAMES_ROW_NUM, NewUserCol, name)
        worksheet.update_cell(SHEET_REPORTS_ROW_NUM, NewUserCol, value)

    logger.info(f"Added user {name} with value {value} at Col {NewUserCol}")
    

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
    try:
        worksheet.update_cell(SHEET_REPORTS_ROW_NUM, worksheet.find(name).col, newValue)# ! not the most eff way
    except gspread.exceptions.APIError:
        logger.exception("gspread.exceptions.APIError Caught")
        client.login()
        worksheet.update_cell(SHEET_REPORTS_ROW_NUM, worksheet.find(name).col, newValue)# ! not the most eff way

    logger.info(f"Updated User {name} to value {newValue}")

# endregion Functions

# region main


def main():
    
    worksheet.add_cols(1)

    # allData = sheet.get_all_records()
    # print(allData)

    # allData = sheet.get_all_records()
    # pprint.pprint(allData)

# endregion main

# region if __main__
if __name__ == "__main__":
    main()
# endregion if __main__
