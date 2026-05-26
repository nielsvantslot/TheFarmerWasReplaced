import DefaultPlotStrategy

def Strategy():
	default_plot_strategy = DefaultPlotStrategy.Strategy()
	obj = {}

	def before_plot(drone, plot):
		cleanup_dead_pumpkins(drone, plot)

	def after_plot(drone, plot):
		return

	def run_plot(drone, plot):
		default_plot_strategy["run_plot"](drone, plot)

	def cleanup_dead_pumpkins(drone, plot):
		first_pass = True
		planted_pumpkins = 0

		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()
		pumpkin_crop = plot["get_crop"]()

		while first_pass or planted_pumpkins > 0:
			first_pass = False
			planted_pumpkins = 0
			drone["move_to"](x1, y1)

			x = x1
			while x <= x2:
				y = y1
				while y <= y2:
					if get_entity_type() == Entities.Dead_Pumpkin:
						drone["harvest_raw"]()
						drone["plant_crop"](pumpkin_crop, plot)
						planted_pumpkins = planted_pumpkins + 1

					if get_entity_type() == None:
						drone["plant_crop"](pumpkin_crop, plot)
						planted_pumpkins = planted_pumpkins + 1

					drone["up"]()
					y = y + 1

				if x < x2:
					x = x + 1
					drone["move_to"](x, y1)
				else:
					x = x + 1

	obj["before_plot"] = before_plot
	obj["after_plot"] = after_plot
	obj["run_plot"] = run_plot

	return obj
