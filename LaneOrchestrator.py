from Drone import drone
import DefaultPlotStrategy

drone = drone()
default_strategy = DefaultPlotStrategy.Strategy()

def run(plot, lane_x):
	# Compatibility shim: run a one-lane pseudo-plot using the default strategy.
	def get_lane_x1():
		return lane_x

	def get_lane_x2():
		return lane_x

	pseudo_plot = {
		"get_x1": get_lane_x1,
		"get_x2": get_lane_x2,
		"get_y1": plot["get_y1"],
		"get_y2": plot["get_y2"],
		"get_crop": plot["get_crop"],
	}

	default_strategy["run_plot"](drone, pseudo_plot)
