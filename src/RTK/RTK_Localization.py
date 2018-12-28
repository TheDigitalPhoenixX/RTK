# region Imports

import json

import os 
import os.path 

# endregion

# region Constants

LOCALIZATION_FOLDER_PATH = "src/RTK/data/Localization/"
LOCALIZATION_FILES_FORMAT = LOCALIZATION_FOLDER_PATH + "Localization_{}.json"

# endregion

# region Initialize

SelectedLang = os.environ.get("Localization")

# endregion

# region Localization Functions


def GetLocalizedText():
    with open(LOCALIZATION_FILES_FORMAT.format(SelectedLang)) as LocalizationFile:
        return json.load(LocalizationFile)

def GetAvailableLang():
    AvailableFiles = tuple(f[13:-5] for f in os.listdir(LOCALIZATION_FOLDER_PATH)
                           if os.path.isfile(os.path.join(LOCALIZATION_FOLDER_PATH, f)))

    # todo: black magic above
    # todo: magic numbers ?
    # todo: make it a tuple from the start ?

    return AvailableFiles

# endregion

# region main
def main():
    # print(GetLocalizedText())
    print(GetAvailableLang())
# endregion


# region if __main__
if __name__ == "__main__":
    main()
# endregion
