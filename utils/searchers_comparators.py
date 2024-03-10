import os
from utils.constants import ACCEPTED_EXTENSIONS

def search_usable_fit_files(directory: str, extension: str):
    """ Returns a list of fit files (in .json or in .fit format), avoiding some of the unnecesary files 
    
    Parameters:
        directory (str): Path to the directory of the files
        extension (str): Extension of the file (.fit | .json)"""
    
    if extension not in ACCEPTED_EXTENSIONS:
        raise Exception("Extension not accepted: ", extension)

    return [fitfile.replace(".json", "") for fitfile in os.listdir(directory) if fitfile.endswith(extension) and "inProgressActivity" not in fitfile]

def compare_files(usable_fit_files: list, existent_json_fit_files: list):
    """ Compares two lists of files to know the difference between them 
    
    Parameters:
        usable_fit_files (list): List of fit files available to use
        existent_json_fit_files (list): List of JSON files already available (without .json extension for comparison)"""

    return list(set(usable_fit_files) - set(existent_json_fit_files))