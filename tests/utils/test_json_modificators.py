import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + os.path.join("..", ".."))
from src.utils.json_modificators import obtain_interesting_chunks, convert_interesting_chunks_to_dataframe

###########################################################
# OBTAIN INTERESTING CHUNKS                               #            
###########################################################

@pytest.fixture
def sample_json():
    return [
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "definition", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}},
        {"frame_type": "data_message", "fields": {"field1": "value1", "field2": "value2"}}
    ]

# Test case for valid chunks
def test_obtain_interesting_chunks_valid(sample_json):
    expected_chunks = [
        {"field1": "value1", "field2": "value2"},
        #{"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"},
        {"field1": "value1", "field2": "value2"}
    ]
    result = obtain_interesting_chunks(sample_json)
    assert result == expected_chunks

# Test case for chunks with irrelevant frame types
def test_obtain_interesting_chunks_irrelevant_frame_type(sample_json):
    sample_json[0]['frame_type'] = "other_type" #Changed 0, and 1 irrelevant
    result = obtain_interesting_chunks(sample_json)
    assert len(result) == 8

# Test case for empty JSON
def test_obtain_interesting_chunks_empty_json():
    result = obtain_interesting_chunks([])
    assert result == []


###########################################################
# CONVERT INTERESTING CHUNKS TO DATAFRAME                 #            
###########################################################
    
# Test case for valid chunks
def test_convert_interesting_chunks_to_dataframe_valid():
    interesting_chunks = [
        [{'name': 'field1', 'value': 'value1'}, {'name': 'field2', 'value': 'value2'}],
        [{'name': 'field1', 'value': 'value3'}, {'name': 'field2', 'value': 'value4'}]
    ]
    training = "sample_training"

    expected_result = [
        {'field1': 'value1', 'field2': 'value2', 'training': 'sample_training'},
        {'field1': 'value3', 'field2': 'value4', 'training': 'sample_training'}
    ]
    
    result = convert_interesting_chunks_to_dataframe(interesting_chunks, training)
    assert result == expected_result

# Test case for malformed data in chunks
def test_convert_interesting_chunks_to_dataframe_malformed_data():
    interesting_chunks = [
        [{'name': 'field1', 'value': 'value1'}, {'name': 'field2', 'value': 'value2'}],
        [{'name': 'field1', 'value': 'value3'}]  # Missing 'field2'
    ]
    training = "sample_training"

    expected_result = [
        {'field1': 'value1', 'field2': 'value2', 'training': 'sample_training'},
        {'field1': 'value3', 'training': 'sample_training'}
    ]
    
    result = convert_interesting_chunks_to_dataframe(interesting_chunks, training)
    assert result == expected_result

# Test case for empty interesting chunks
def test_convert_interesting_chunks_to_dataframe_empty_chunks():
    interesting_chunks = []
    training = "sample_training"

    expected_result = []
    
    result = convert_interesting_chunks_to_dataframe(interesting_chunks, training)
    assert result == expected_result