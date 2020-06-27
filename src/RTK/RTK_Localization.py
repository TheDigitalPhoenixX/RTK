# region Imports

# region Localization
from os import environ
import os.path
import json
# endregion Localization

# region Logging
import logging
import RTK.RTK_Logging as RTK_Logging
# endregion Logging

# endregion Imports

# region Constants

FILE_PATH = os.path.realpath(__file__)
ROOT_FOLDER_PATH = FILE_PATH[:-len(os.path.basename(FILE_PATH))]

# region Localization
LOCALIZATION_FOLDER_PATH = os.path.join(ROOT_FOLDER_PATH, "data/Localization/")
LOCALIZATION_FILES_FORMAT = LOCALIZATION_FOLDER_PATH + "Localization_{}.json"
# endregion Localization

# region Logging
LOG_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, os.pardir, "logs", f'{__name__}.log')  # TODO Name of the file
# endregion Logging

# endregion Constants

# region Initialize

SelectedLang = environ.get("Localization")

# endregion Initialize

# region Logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addHandler(RTK_Logging.GetFileHandler(LOG_FILE_PATH))
logger.addHandler(RTK_Logging.GetStreamHandler())
logger.addHandler(RTK_Logging.GetCommonFileHandler())

# endregion Logging

# region Localization Functions


def GetLocalizedText():
    logger.info(f"Loading Localized Text: {SelectedLang}")
    with open(LOCALIZATION_FILES_FORMAT.format(SelectedLang)) as LocalizationFile:
        return json.load(LocalizationFile)

def GetAvailableLang():
    AvailableFiles = tuple(f[13:-5] for f in os.listdir(LOCALIZATION_FOLDER_PATH)
                           if os.path.isfile(os.path.join(LOCALIZATION_FOLDER_PATH, f))) # TODO magic numbers ?
    
    logger.info(f"Loaded Available Lang: {AvailableFiles}")
    return AvailableFiles

# endregion Localization Functions

# region main
def main():
    # print(GetLocalizedText())
    print(GetAvailableLang())
# endregion main


# region if __main__
if __name__ == "__main__":
    main()
# endregion if __main__
