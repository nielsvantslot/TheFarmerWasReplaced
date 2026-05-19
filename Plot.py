import Math

def plot(crop, strategy, hat, x1, y1, x2, y2):
	self = {
		"crop": crop,
		"strategy": strategy,
		"hat": hat,
		"x1": x1,
		"y1": y1,
		"x2": x2,
		"y2": y2,
	}

	obj = {}

	def get_crop():
		return self["crop"]

	def get_strategy():
		return self["strategy"]

	def get_hat():
		return self["hat"]

	def get_x1():
		return self["x1"]

	def get_y1():
		return self["y1"]

	def get_x2():
		return self["x2"]

	def get_y2():
		return self["y2"]

	obj["get_crop"] = get_crop
	obj["get_strategy"] = get_strategy
	obj["get_hat"] = get_hat
	obj["get_x1"] = get_x1
	obj["get_y1"] = get_y1
	obj["get_x2"] = get_x2
	obj["get_y2"] = get_y2

	return obj
