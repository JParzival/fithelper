import json
import os
import pandas as pd
import pytest
from unittest.mock import mock_open, patch
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../")
from src.utils.helpers import open_json, append_dataframes

###########################################################
# OPEN JSON                                               #            
###########################################################

# Mocking the built-in open function
@pytest.mark.parametrize("file_content, expected_result", [
    ('{"key": "value"}', {'key': 'value'}),
    ('{"number": 42}', {'number': 42})
])
def test_open_json_existing_file(file_content, expected_result):
    file_path = 'test.json'

    with patch('builtins.open', mock_open(read_data=file_content)) as mock_file:
        result = open_json(file_path)

    assert result == expected_result
    mock_file.assert_called_once_with(file_path)

# Test case for handling non-existing file
def test_open_json_non_existing_file():
    with pytest.raises(FileNotFoundError):
        open_json('non_existing_file.json')

# Test case for handling JSON decode error
def test_open_json_invalid_json():
    invalid_json_content = 'not a valid JSON'
    file_path = 'test.json'

    with patch('builtins.open', mock_open(read_data=invalid_json_content)):
        with pytest.raises(json.JSONDecodeError):
            open_json(file_path)

# Test case for other exceptions during file opening
def test_open_json_other_exception():
    with patch('builtins.open', side_effect=OSError):
        with pytest.raises(OSError):
            open_json('test.json')



###########################################################
# APPEND DATAFRAMES                                       #            
###########################################################


# Test case for a single dataframe
def test_append_dataframes_single_dataframe():
    # Create a sample dataframe
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = append_dataframes([df])
    assert result.equals(df)

# Test case for multiple dataframes
def test_append_dataframes_multiple_dataframes():
    # Create sample dataframes
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})
    df3 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

    # Concatenate dataframes
    expected_result = pd.concat([df1, df2, df3], ignore_index=True)
    result = append_dataframes([df1, df2, df3])

    # Assert equality
    assert result.equals(expected_result)

# Test case for dataframes with different columns
def test_append_dataframes_different_columns():
    # Create sample dataframes
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'C': [4, 5, 6], 'D': [7, 8, 9]})

    # Concatenate dataframes
    expected_result = pd.concat([df1, df2], ignore_index=True)
    result = append_dataframes([df1, df2])

    # Assert equality
    assert result.equals(expected_result)

# Test case for dataframes with overlapping columns
def test_append_dataframes_overlapping_columns():
    # Create sample dataframes
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})

    # Concatenate dataframes
    expected_result = pd.concat([df1, df2], ignore_index=True)
    result = append_dataframes([df1, df2])

    # Assert equality
    assert result.equals(expected_result)