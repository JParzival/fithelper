import json
import pandas as pd

def open_json(thejson):
    """ Returns an opened JSON """

    with open(thejson) as file:
        return json.load(file)
    
def append_dataframes(dataframes_of_trainings):
    """ Returns a unique dataframe from a list of dataframes """

    return pd.concat(dataframes_of_trainings, ignore_index=True)