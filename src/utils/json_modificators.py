def obtain_interesting_chunks(my_json: str):
    """ Returns only the chunks that are necessary for the dataset, avoiding unnecesary or definition frame_types 
    
    Parameters:
        my_json (JSON): The JSON (opened) that the method is going to work with"""

    chunks_to_save = []
    for chunk in my_json:
        try:
            if chunk["frame_type"] == "data_message":
                chunks_to_save.append(chunk['fields'])
        except Exception as e:
            print("Excepted in chunk, ", e)
    
    return chunks_to_save

def convert_interesting_chunks_to_dataframe(interesting_chunks: list, training: str):
    """ Returns necessary records in object format, for better future convertion purposes 
    
    Parameters:
        interesting_chunks (list): List of chunks that are interesting for obtaining data
        training (str): Path to the name of the training file"""
    
    # TODO Distance appears twice, one sometimes with value, the other one Null. Null overrides the first one. Control it.

    custom_records_object = []
    for record in interesting_chunks:
        try:
            custom_record_object = {element['name']: element['value'] for element in record}
            custom_record_object.update({"training": training})
            custom_records_object.append(custom_record_object) 
        except Exception as e:
            print("Exception: One chunk could not be included: ", e)
            continue

    return custom_records_object