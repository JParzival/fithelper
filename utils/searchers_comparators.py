import os

def search_usable_fit_files(directory, extension):
    """ Returns a list of fit files (in .json or in .fit format), avoiding some of the unnecesary files """

    return [fitfile.replace(".json", "") for fitfile in os.listdir(directory) if fitfile.endswith(extension) and "inProgressActivity" not in fitfile]

def compare_files(usable_fit_files, existent_fit_files):
    """ Compares two lists of files to know the difference between them """

    return list(set(usable_fit_files) - set(existent_fit_files))