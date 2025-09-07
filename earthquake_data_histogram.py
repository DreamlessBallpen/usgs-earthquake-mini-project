import pandas as pd
import matplotlib.pyplot as plt

class EarthQuakeCharts:
	def __init__(self, earthquake_table):
		self.earthquake_table = earthquake_table
	
	def magnitude_histogram(self):
		hist = self.earthquake_table['magnitude'].hist(bins=5)
		fig = hist.get_figure()
		return hist, fig
	
	def save_charts(self, output_dir):
		hist_ax, hist_fig = self.magnitude_histogram()
		hist_ax.set_title("magnitudes")
		hist_fig.savefig(f"{output_dir}/magnitudes_histogram.png")
		