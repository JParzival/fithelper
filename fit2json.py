import os
import json
import datetime

from utils.constants import JSONS_DIRECTORY, FIT_DIRECTORY, CURRENT_DIRECTORY
from utils.searchers_comparators import search_usable_fit_files, compare_files

def obtain_new_files_in_folder_json_format():
    """ Adds .fit files converted into JSON in a folder, adding only the non-existent ones after comparing the existent """

    os.makedirs(JSONS_DIRECTORY, exist_ok=True) #Does nothing if directory exists

    usable_fit_files = search_usable_fit_files(directory=FIT_DIRECTORY, extension=".fit")
    existent_json_fit_files = search_usable_fit_files(directory=JSONS_DIRECTORY, extension=".json")
    fit_files_to_add = compare_files(usable_fit_files, existent_json_fit_files)
    print("Adding " + str(len(fit_files_to_add)) + " files")

    for fitfile in fit_files_to_add:
        json_fit_file = fitfile + ".json"
        os.system("fitjson --pretty -f=record -o {0} {1}".format(os.path.join(JSONS_DIRECTORY, json_fit_file), os.path.join(FIT_DIRECTORY, fitfile))) #Could not run subprocess well with this kind of command, os os.system solves it


if __name__ == "__main__":
    obtain_new_files_in_folder_json_format()