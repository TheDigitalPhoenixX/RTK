

import json
import os

SelectedLang = os.getenv("Localization")

LOCALIZATION_FOLDER_PATH = "data/Localization/"
LOCALIZATION_FILES_FORMAT = LOCALIZATION_FOLDER_PATH + "Localization_{}.json"

def GetLocalizedText():
    with open(LOCALIZATION_FILES_FORMAT.format(SelectedLang)) as LocalizationFile:
        return json.load(LocalizationFile)


def GetAvailableLang():
    AvailableFiles = tuple(f[13:-5] for f in os.listdir(LOCALIZATION_FOLDER_PATH)
                           if os.path.isfile(os.path.join(LOCALIZATION_FOLDER_PATH, f)))

    return AvailableFiles
