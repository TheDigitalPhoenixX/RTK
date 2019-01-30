# region Imports
import logging
import os.path
# endregion Imports

# reigon Constants
FILE_PATH = os.path.realpath(__file__)
ROOT_FOLDER_PATH = FILE_PATH[:-len(os.path.basename(FILE_PATH))]

COMMON_LOG_FILE_PATH = os.path.join(
    ROOT_FOLDER_PATH, os.pardir, "logs", "main.log")  # TODO Name of the file

# endregion Constants

# region Initialize
formatter = logging.Formatter(
    "[%(asctime)s][%(name)s][%(levelname)s][%(filename)s: %(funcName)s]: %(message)s")  # TODO Proper formatting
# endregion Initialize

# region Getters
def GetFileHandler(LogFilePath):
    file_handler = logging.FileHandler(LogFilePath)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    return file_handler


def GetStreamHandler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    return stream_handler

def GetCommonFileHandler():
    file_handler = logging.FileHandler(COMMON_LOG_FILE_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    return file_handler

# endregion Getters

# TODO Rotating File Handler