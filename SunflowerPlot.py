import World

def Strategy():
	self = {
		"harvest_order": [],
	}
	obj = {}

	def before_plot(drone, plot):
		candidates = scan_harvestable_sunflowers(drone, plot)
		self["harvest_order"] = build_harvest_order(drone, candidates)

	def after_plot(drone, plot):
		self["harvest_order"] = []
		return

	def wrap_distance(a, b, size):
		delta = (b - a) % size
		return min(delta, size - delta)

	def tile_distance(x1, y1, x2, y2, size):
		return wrap_distance(x1, x2, size) + wrap_distance(y1, y2, size)

	def insertion_sort_by_distance(group, from_x, from_y, world_size):
		i = 1
		while i < len(group):
			key = group[i]
			key_dist = tile_distance(from_x, from_y, key["x"], key["y"], world_size)
			j = i - 1
			while j >= 0 and tile_distance(from_x, from_y, group[j]["x"], group[j]["y"], world_size) > key_dist:
				group[j + 1] = group[j]
				j = j - 1
			group[j + 1] = key
			i = i + 1
		return group


	def scan_harvestable_sunflowers(drone, plot):
		candidates = []
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()
		crop = plot["get_crop"]()

		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				drone["move_to"](x, y)
				if get_entity_type() == Entities.Sunflower and crop["should_harvest"](drone, plot):
					size = measure()
					if size == None:
						y = y + 1
						continue

					candidates.append({
						"x": x,
						"y": y,
						"size": size,
					})
				y = y + 1
			x = x + 1

		return candidates

	def build_harvest_order(drone, candidates):
		ordered = []
		world_size = World.size()
		cx = drone["get_x"]()
		cy = drone["get_y"]()

		if len(candidates) == 0:
			return ordered

		max_size = candidates[0]["size"]
		min_size = candidates[0]["size"]
		i = 0
		while i < len(candidates):
			s = candidates[i]["size"]
			if s > max_size:
				max_size = s
			if s < min_size:
				min_size = s
			i = i + 1

		bucket_count = max_size - min_size + 1
		buckets = []
		i = 0
		while i < bucket_count:
			buckets.append([])
			i = i + 1

		i = 0
		while i < len(candidates):
			c = candidates[i]
			buckets[c["size"] - min_size].append(c)
			i = i + 1

		size = max_size
		while size >= min_size:
			group = buckets[size - min_size]
			group = insertion_sort_by_distance(group, cx, cy, world_size)
			j = 0
			while j < len(group):
				ordered.append(group[j])
				j = j + 1
			if len(group) > 0:
				cx = group[len(group) - 1]["x"]
				cy = group[len(group) - 1]["y"]
			size = size - 1

		return ordered

	def harvest_in_order(drone, plot, harvest_order):
		crop = plot["get_crop"]()
		i = 0
		while i < len(harvest_order):
			target = harvest_order[i]
			drone["move_to"](target["x"], target["y"])
			if crop["should_harvest"](drone, plot):
				drone["harvest_raw"]()
			i = i + 1

	def replant_all(drone, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()
		crop = plot["get_crop"]()

		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				drone["move_to"](x, y)
				crop["prepare"](drone, plot)
				if get_entity_type() != Entities.Sunflower:
					drone["plant_crop"](crop, plot)
				y = y + 1
			x = x + 1

	def run_plot(drone, plot):
		harvest_order = self["harvest_order"]
		harvest_in_order(drone, plot, harvest_order)
		replant_all(drone, plot)

	obj["before_plot"] = before_plot
	obj["after_plot"] = after_plot
	obj["run_plot"] = run_plot

	return obj
