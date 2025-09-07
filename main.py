import pandas as pd
import requests
from get_earthquake_data import endpoint, response
from data_feature_parser import dfp					# [NEEDED: See below]
import earthquake_data_histogram as edh				# [NEEDED: See below]


if __name__ == "__main__":
	data = response.json()							# PART 1: Get the data from the website
	datalist = data['features']					    # PART 2: Parse the data
	parsed_data = dfp(datalist)
													  # PART 3: Normalize the parsed data, for further standardization.
	df = pd.json_normalize(						   
		data=parsed_data,
		sep="_"
		)

													  # PART 4: Cleaning data: Drop or rename nulls, convert time
													  # Upon checking: Can confirm no nulls after this.
	
   
	time_secs = df['time'] / 1000								   # P4-2-1: Converting time in milliseconds to seconds
	df['converted_time'] = pd.to_datetime(time_secs, unit='s')	   # P4-2-2: Converting time in seconds to datetime format
	
													  # Plotting a histogram of earthquake magnitudes
	fname = "output1_dataset.csv"					  # P4-3: Initial saves.
	df.to_csv(fname, index=False)
	
	eq_chart = edh.EarthQuakeCharts(df)				  # P5: Gathering insights.
	eq_chart.save_charts("output_charts")			  # Let's try this! If it works, work on uploading tomorrow.
	
# For this specific case: Taking JSON data and extracting key-value pairs to create a structured DataFrame.

# 4. Do Something Insightful
# Examples:
# Plot a histogram of earthquake magnitudes									[DONE]
# Plot top 10 locations with the most quakes
# (Optional) Convert UNIX timestamps to readable time
# (Optional) Map quakes by coordinates using seaborn.scatterplot
# 5. Write Observations
# In comments or markdown, write 2–3 simple insights
# "Most quakes are below magnitude 3."
# "Region X had 12 small quakes this week."
# 📁 Deliverables
# A Jupyter notebook or .py file with your code
# Screenshots or saved PNGs of your plots (if any)

# 05/18/2025 - TODO: working on parsing first before using json_normalize. [DONE]
# 5/20/2025 - TODO: Working on the next steps.  - Normalize the json using json_normalize. [DONE]
# 5/26/2025 - Currently working on the next set of tasks -- creating visualizations and insights.
# 6/7/2025 - Still working on the visualizations.
# 6/7/2025 - Single focus: [TODO] Figure out code to create histograms. Currently being figured out in earthquake_data_histogram.py [DONE]