import Math
import Plot

def PlotFactory():
	obj = {}

	def create(spec, x1, y1, x2, y2):
		return Plot.plot(
			spec["get_crop"](),
			spec["get_strategy"](),
			spec["get_hat"](),
			x1, y1, x2, y2
		)

	def create_all(specs, world_size):
		plot_width = world_size / len(specs)
		plots = []
		i = 0
		while i < len(specs):
			plots.append(create(
				specs[i],
				Math.truncate(i * plot_width),
				0,
				Math.truncate((i + 1) * plot_width) - 1,
				world_size - 1
			))
			i += 1
		return plots

	obj["create"] = create
	obj["create_all"] = create_all

	return obj
