# Part1: Get earthquake data from the website
# This is the website it feeds into: https://earthquake.usgs.gov/earthquakes/map

import requests

endpoint = r"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"
response = requests.get(endpoint)

# Part1-1: Examine the status, if the request was successful. Examine the data structure as well.
if __name__ == "__main__":
    if response.status_code == 200:
        data = response.json()
        print("No issues. Printing the keys from our JSON data")
        print(data.keys())
    else:
        print(f"Error in fetching data: {response.status_code}")
    

