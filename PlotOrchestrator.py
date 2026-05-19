from Drone import drone
import World
import LaneOrchestrator

drone = drone()

def run(plot):
	x1 = plot["get_x1"]()
	x2 = plot["get_x2"]()

	drone["set_hat"](plot["get_hat"]())
	drone["move_to"](x1, plot["get_y1"]())

	plot_strategy = plot["get_strategy"]()
	if plot_strategy != None:
		plot_strategy.run(plot)

	x = x1
	while x <= x2:
		LaneOrchestrator.run(plot, x)
		x = x + 1

	next_plot_x = (x2 + 1) % World.size()

	drone["move_to"](next_plot_x, plot["get_y1"]())