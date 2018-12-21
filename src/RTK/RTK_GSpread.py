# https://github.com/burnash/gspread

"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

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

# region Gspread

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# endregion

import os
import ast
import pprint

# endregion

# region Constants

SHEET_NAMES_ROW_NUM = 1
SHEET_REPORTS_ROW_NUM = 2

# endregion

# region Initialize

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
creds = ServiceAccountCredentials.from_json_keyfile_dict(ast.literal_eval(os.environ.get("GSPREAD_CLIENT_SECRET")), scope)
client = gspread.authorize(creds)
sheet = client.open("RTK").sheet1
# endregion

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
    return sheet.get_all_records()[0]
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
    NewUserCol = len(getReportsDic()) +1
    sheet.update_cell(SHEET_NAMES_ROW_NUM, NewUserCol, name)
    sheet.update_cell(SHEET_REPORTS_ROW_NUM, NewUserCol, value)

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
    sheet.update_cell(SHEET_REPORTS_ROW_NUM, sheet.find(name).col, newValue)# ! not the most eff way

# endregion

# region main


def main():
    

    allData = sheet.get_all_records()
    pprint.pprint(allData)

    # sheet.update_cell(SHEET_REPORTS_ROW_NUM, sheet.find(
    #     "MohamedXyz").col, 235)  # ! not the most eff way
    # # sheet.update_cell(2,15,567)

    # allData = sheet.get_all_records()
    # pprint.pprint(allData)

# endregion

# region if __main__
if __name__ == "__main__":
    main()
# endregion
