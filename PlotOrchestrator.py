from Drone import drone
import World
import DefaultPlotStrategy

drone = drone()
default_plot_strategy = DefaultPlotStrategy.Strategy()

def run(plot):
	x1 = plot["get_x1"]()
	x2 = plot["get_x2"]()

	drone["set_hat"](plot["get_hat"]())
	drone["move_to"](x1, plot["get_y1"]())

	plot_strategy = plot["get_strategy"]()
	if plot_strategy == None:
		plot_strategy = default_plot_strategy

	plot_strategy["before_plot"](drone, plot)
	plot_strategy["run_plot"](drone, plot)
	plot_strategy["after_plot"](drone, plot)

	next_plot_x = (x2 + 1) % World.size()

	drone["move_to"](next_plot_x, plot["get_y1"]())