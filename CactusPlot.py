def Strategy():
	self = {
		"ready_to_harvest": False,
	}
	obj = {}

	def before_plot(drone, plot):
		crop = plot["get_crop"]()

		if not prepare_and_check_fully_grown(drone, plot, crop):
			self["ready_to_harvest"] = False
			return

		sort_cacti(drone, plot)
		self["ready_to_harvest"] = is_plot_sorted(drone, plot)

	def after_plot(drone, plot):
		self["ready_to_harvest"] = False

	def run_plot(drone, plot):
		if not self["ready_to_harvest"]:
			return

		harvest_once_then_replant_all(drone, plot)

	def prepare_and_check_fully_grown(drone, plot, crop):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()

		all_grown = True
		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				drone["move_to"](x, y)

				if get_entity_type() != Entities.Cactus:
					drone["plant_crop"](crop, plot)
					all_grown = False
				elif not can_harvest():
					all_grown = False

				y = y + 1
			x = x + 1

		return all_grown

	def sort_cacti(drone, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()

		def key_for(x, y):
			return str(x) + "," + str(y)

		def add_active(active_list, active_seen, x, y):
			if x < x1 or x > x2:
				return
			if y < y1 or y > y2:
				return

			key = key_for(x, y)
			if key in active_seen:
				return

			active_seen[key] = True
			active_list.append({"x": x, "y": y})

		active_list = []
		active_seen = {}
		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				add_active(active_list, active_seen, x, y)
				y = y + 1
			x = x + 1

		while len(active_list) > 0:
			next_active_list = []
			next_active_seen = {}
			any_swap = False

			i = 0
			while i < len(active_list):
				coord = active_list[i]
				x = coord["x"]
				y = coord["y"]
				drone["move_to"](x, y)

				current = measure()
				tile_swapped = False

				if current != None:
					if x < x2:
						east = measure(East)
						if east != None and current > east and swap(East):
							any_swap = True
							tile_swapped = True

					if y < y2:
						current = measure()
						north = measure(North)
						if north != None and current > north and swap(North):
							any_swap = True
							tile_swapped = True

				if tile_swapped:
					add_active(next_active_list, next_active_seen, x, y)
					add_active(next_active_list, next_active_seen, x + 1, y)
					add_active(next_active_list, next_active_seen, x - 1, y)
					add_active(next_active_list, next_active_seen, x, y + 1)
					add_active(next_active_list, next_active_seen, x, y - 1)
					add_active(next_active_list, next_active_seen, x + 1, y + 1)
					add_active(next_active_list, next_active_seen, x - 1, y - 1)

				drone["move_to"](x, y)
				if not is_current_tile_sorted(x, y, plot):
					add_active(next_active_list, next_active_seen, x, y)
					add_active(next_active_list, next_active_seen, x + 1, y)
					add_active(next_active_list, next_active_seen, x - 1, y)
					add_active(next_active_list, next_active_seen, x, y + 1)
					add_active(next_active_list, next_active_seen, x, y - 1)

				i = i + 1

			if not any_swap and len(next_active_list) == 0:
				break

			active_list = next_active_list

	def is_current_tile_sorted(x, y, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()

		current = measure()
		if current == None:
			return False

		if x < x2:
			east = measure(East)
			if east == None or current > east:
				return False

		if y < y2:
			north = measure(North)
			if north == None or current > north:
				return False

		if x > x1:
			west = measure(West)
			if west == None or west > current:
				return False

		if y > y1:
			south = measure(South)
			if south == None or south > current:
				return False

		return True

	def is_plot_sorted(drone, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()

		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				drone["move_to"](x, y)
				if not is_current_tile_sorted(x, y, plot):
					return False
				y = y + 1
			x = x + 1

		return True

	def harvest_once_then_replant_all(drone, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()
		crop = plot["get_crop"]()

		drone["move_to"](x1, y1)
		if can_harvest():
			drone["harvest_raw"]()

		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				drone["move_to"](x, y)
				if get_entity_type() != Entities.Cactus:
					crop["prepare"](drone, plot)
					drone["plant_crop"](crop, plot)
				y = y + 1
			x = x + 1

	obj["before_plot"] = before_plot
	obj["after_plot"] = after_plot
	obj["run_plot"] = run_plot

	return obj
