
def dfp(feature_list):
    """ Just implemented here to modularize against the main function.
    """
    earthquakes_list = []
    
    for feature in feature_list:                                        # Per datapoint (Assuming I understand this correctly)
        
        properties = feature['properties']                              # First layer of extraction
        geometry = feature['geometry']                                  # First layer of extraction
        
        quake_info = {
            "place": properties["place"],                               # Second layer of extraction from properties
            "magnitude": properties["mag"],                             # Second layer of extraction from properties
            "time": properties["time"],                                 # Second layer of extraction from properties
            "longitude": geometry["coordinates"][0],                    # Second layer of extraction from geometry
            "latitude": geometry["coordinates"][1],                     # Second layer of extraction from geometry
            "depth": geometry["coordinates"][2]                         # Second layer of extraction from geometry
            }
    
        earthquakes_list.append(quake_info)                             # Append the actual parsed data "quake_info" into our new earthquakes_list.
    
    return earthquakes_list