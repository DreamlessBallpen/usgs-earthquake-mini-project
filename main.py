# Script for the full workflow.
import pandas as pd
import requests
from get_earthquake_data import endpoint, response



if __name__ == "__main__":
    data = response.json()
    datalist = data['features']
    df = pd.json_normalize(
        data=datalist,
        sep='_'
        )
    
    fname = "output1_dataset.csv"
    df.to_csv(fname, index=False)
    