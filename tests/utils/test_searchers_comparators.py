import os
import pytest
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
from src.utils.searchers_comparators import search_usable_fit_files, compare_files

###########################################################
# SEARCH USABLE FIT FILES                                 #            
###########################################################

# Test case for search_usable_fit_files with valid input
def test_search_usable_fit_files_valid_input(tmp_path):
    # Create sample fit and json files in the directory
    directory = tmp_path
    fit_files = ['file1.fit', 'file2.fit', 'file3.fit', 'file4.fit', 'file5.fit', 'inProgressActivity.json']
    for file_name in fit_files:
        with open(os.path.join(directory, file_name), 'w') as f:
            f.write('Some content')

    # Call the function
    result = search_usable_fit_files(directory, ".fit")

    # Check the result
    assert result == ['file1.fit', 'file2.fit', 'file3.fit', 'file4.fit', 'file5.fit']

# Test case for search_usable_fit_files with invalid extension
def test_search_usable_fit_files_invalid_extension(tmp_path):
    directory = tmp_path
    with pytest.raises(Exception):
        search_usable_fit_files(directory, ".txt")


###########################################################
# COMPARE FILES                                           #            
###########################################################

"""For these tests, remember the params of the compare files method

Parameters:
        usable_fit_files (list): List of fit files available to use
        existent_json_fit_files (list): List of JSON files already available (without .json extension for comparison)
"""

# Test case for compare_files with valid inputs
def test_compare_files_valid_inputs():
    usable_fit_files = ['file1.fit', 'file2.fit', 'file3.fit']
    existent_json_fit_files = ['file1.fit', 'file3.fit']
    result = compare_files(usable_fit_files, existent_json_fit_files)
    assert result == ['file2.fit']

# Test case for compare_files with empty lists
def test_compare_files_empty_lists():
    result = compare_files([], [])
    assert result == []

# Test case for compare_files with all common files
def test_compare_files_all_common_files():
    usable_fit_files = ['file1.fit', 'file2.fit', 'file3.fit']
    existent_json_fit_files = ['file1.fit', 'file2.fit', 'file3.fit']
    result = compare_files(usable_fit_files, existent_json_fit_files)
    assert result == []

# Test case for compare_files with all different files
def test_compare_files_all_different_files():
    usable_fit_files = ['file1.fit', 'file2.fit', 'file3.fit']
    existent_json_fit_files = ['file4.fit', 'file5.fit', 'file6.fit']
    result = compare_files(usable_fit_files, existent_json_fit_files)
    for testfile in result:
        assert testfile in ['file1.fit', 'file2.fit', 'file3.fit']