import DefaultPlotStrategy

default_plot_strategy = DefaultPlotStrategy.Strategy()

def PlotSpec(crop, strategy, hat):
	resolved_strategy = strategy
	if resolved_strategy == None:
		resolved_strategy = default_plot_strategy

	obj = {}

	def get_crop():
		return crop

	def get_strategy():
		return resolved_strategy

	def get_hat():
		return hat

	obj["get_crop"] = get_crop
	obj["get_strategy"] = get_strategy
	obj["get_hat"] = get_hat

	return obj
