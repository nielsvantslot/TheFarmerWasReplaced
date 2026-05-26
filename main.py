from Plots import PlotFactory
from Plots import PlotOrchestrator
from Plots import validate_plot_specs
from PlotSpecs import plot_specs
import Wood

import World

if validate_plot_specs(plot_specs):
	plot_factory = PlotFactory()
	world_size = -1
	plots = []

	while True:
		current_world_size = World.size()

		if current_world_size != world_size:
			plots = plot_factory["create_all"](plot_specs, current_world_size)
			world_size = current_world_size

		Wood.reset_maze_state()

		plot_index = 0
		while plot_index < len(plots):
			if World.size() != world_size:
				break

			PlotOrchestrator.run(plots[plot_index])
			plot_index = plot_index + 1