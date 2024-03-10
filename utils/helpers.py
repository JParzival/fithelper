import json
import pandas as pd

def open_json(thejson: str):
    """ Returns an opened JSON 
    
    Parameters:
        thejson (str): The path to the JSON that is going to be opened

    """
    
    with open(thejson) as file:
        return json.load(file)
    
def append_dataframes(dataframes_of_trainings: list):
    """ Returns a unique dataframe from a list of dataframes 
    
    Parameters:
        dataframes_of_trainings (list): List of pandas dataframes to be concat
        
    """
    

    return pd.concat(dataframes_of_trainings, ignore_index=True)