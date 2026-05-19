def PlotSpec(crop, strategy, hat):
	obj = {}

	def get_crop():
		return crop

	def get_strategy():
		return strategy

	def get_hat():
		return hat

	obj["get_crop"] = get_crop
	obj["get_strategy"] = get_strategy
	obj["get_hat"] = get_hat

	return obj
