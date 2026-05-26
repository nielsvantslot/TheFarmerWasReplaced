def Strategy():
	obj = {}

	def before_plot(drone, plot):
		return

	def after_plot(drone, plot):
		return

	def run_plot(drone, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()
		crop = plot["get_crop"]()

		x = x1
		while x <= x2:
			drone["move_to"](x, y1)

			while drone["get_y"]() <= y2:
				drone["run_crop"](crop, plot)
				if drone["get_y"]() == y2:
					break
				drone["up"]()

			x = x + 1

	obj["before_plot"] = before_plot
	obj["after_plot"] = after_plot
	obj["run_plot"] = run_plot

	return obj
