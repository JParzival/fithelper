import os
import pandas as pd

from utils.helpers import open_json, append_dataframes
from utils.json_modificators import obtain_interesting_chunks, convert_interesting_chunks_to_dataframe
from utils.constants import JSONS_DIRECTORY, SAVE_DATAFRAME

def obtain_dataframe_from_jsons():
    """ Returns a unique dataframe to work with, orchestrating from JSON opening to that final dataset """
    
    dataframes_of_trainings = []
    for currentjson in os.listdir(JSONS_DIRECTORY):
        openedjson = open_json(os.path.join(JSONS_DIRECTORY, currentjson))
        interesting_chunks = obtain_interesting_chunks(openedjson)
        custom_records_object = convert_interesting_chunks_to_dataframe(interesting_chunks, os.path.join(JSONS_DIRECTORY, currentjson))
        dataframes_of_trainings.append(pd.DataFrame([x for x in custom_records_object]))
    return append_dataframes(dataframes_of_trainings)


if __name__ == "__main__":
    dataframe = obtain_dataframe_from_jsons()
    if SAVE_DATAFRAME:
        dataframe.to_csv('./dataframe.csv', index=False)