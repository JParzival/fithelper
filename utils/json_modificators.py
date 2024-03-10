def obtain_interesting_chunks(my_json):
    """ Returns only the chunks that are necessary for the dataset, avoiding unnecesary or definition frame_types """

    chunks_to_save = []
    for chunk in my_json:
        try:
            if chunk["frame_type"] == "data_message":
                chunks_to_save.append(chunk['fields'])
        except Exception as e:
            print("Excepted in chunk, ", e)
    
    return chunks_to_save

def convert_interesting_chunks_to_dataframe(interesting_chunks, training):
    """ Returns necessary records in object format, for better future convertion purposes """

    custom_records_object = []
    for record in interesting_chunks:
        custom_record_object = {element['name']: element['value'] for element in record}
        custom_record_object.update({"training": training})
        custom_records_object.append(custom_record_object)
    return custom_records_object