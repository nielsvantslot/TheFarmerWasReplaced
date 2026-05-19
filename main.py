from Crops import *
from Plots import *

import World

plot_specs = [
	PlotSpec(Grass,     None,        Hats.Straw_Hat),
	PlotSpec(Carrot,    None,        Hats.Traffic_Cone),
	PlotSpec(Pumpkin,   PumpkinPlot, Hats.Pumpkin_Hat),
	PlotSpec(Wood,      None,        Hats.Brown_Hat),
	PlotSpec(Sunflower, None,        Hats.Sunflower_Hat),
	PlotSpec(Cactus,    None,        Hats.Cactus_Hat),
]

plot_factory = PlotFactory()
world_size = -1
plots = []

while True:
	current_world_size = World.size()

	if current_world_size != world_size:
		plots = plot_factory["create_all"](plot_specs, current_world_size)
		world_size = current_world_size

	plot_index = 0
	while plot_index < len(plots):
		if World.size() != world_size:
			break

		PlotOrchestrator.run(plots[plot_index])
		plot_index = plot_index + 1