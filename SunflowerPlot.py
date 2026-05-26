import World

def Strategy():
	self = {
		"harvest_order": [],
	}
	obj = {}

	def before_plot(drone, plot):
		if not has_any_sunflower(drone, plot):
			self["harvest_order"] = []
			return

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

	def merge_lists(left, right, compare):
		merged = []
		i = 0
		j = 0

		while i < len(left) and j < len(right):
			if compare(left[i], right[j]):
				merged.append(left[i])
				i = i + 1
			else:
				merged.append(right[j])
				j = j + 1

		while i < len(left):
			merged.append(left[i])
			i = i + 1

		while j < len(right):
			merged.append(right[j])
			j = j + 1

		return merged

	def merge_sort(items, compare):
		if len(items) <= 1:
			return items

		middle = len(items) // 2
		left = []
		right = []
		i = 0

		while i < middle:
			left.append(items[i])
			i = i + 1

		while i < len(items):
			right.append(items[i])
			i = i + 1

		left = merge_sort(left, compare)
		right = merge_sort(right, compare)

		return merge_lists(left, right, compare)

	def has_any_sunflower(drone, plot):
		x1 = plot["get_x1"]()
		x2 = plot["get_x2"]()
		y1 = plot["get_y1"]()
		y2 = plot["get_y2"]()

		x = x1
		while x <= x2:
			y = y1
			while y <= y2:
				drone["move_to"](x, y)
				if get_entity_type() == Entities.Sunflower:
					return True
				y = y + 1
			x = x + 1

		return False

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

	def sort_by_size_desc(candidates):
		# Grouping by size keeps a strict largest-to-smallest harvest contract.
		def normalize_size(value):
			if value == None:
				return -1

			return value

		def compare_size(left, right):
			left_size = normalize_size(left["size"])
			right_size = normalize_size(right["size"])

			if left_size > right_size:
				return True
			if left_size < right_size:
				return False

			if left["x"] < right["x"]:
				return True
			if left["x"] > right["x"]:
				return False

			return left["y"] <= right["y"]

		return merge_sort(candidates, compare_size)

	def sort_group_by_distance(group, from_x, from_y, world_size):
		def compare_distance(left, right):
			left_distance = tile_distance(from_x, from_y, left["x"], left["y"], world_size)
			right_distance = tile_distance(from_x, from_y, right["x"], right["y"], world_size)

			if left_distance < right_distance:
				return True
			if left_distance > right_distance:
				return False

			if left["x"] < right["x"]:
				return True
			if left["x"] > right["x"]:
				return False

			return left["y"] <= right["y"]

		return merge_sort(group, compare_distance)

	def build_harvest_order(drone, candidates):
		ordered = []
		world_size = World.size()
		cx = drone["get_x"]()
		cy = drone["get_y"]()
		sorted_candidates = sort_by_size_desc(candidates)
		i = 0

		while i < len(sorted_candidates):
			size_value = sorted_candidates[i]["size"]
			group = []

			while i < len(sorted_candidates) and sorted_candidates[i]["size"] == size_value:
				group.append(sorted_candidates[i])
				i = i + 1

			group = sort_group_by_distance(group, cx, cy, world_size)

			j = 0
			while j < len(group):
				ordered.append(group[j])
				j = j + 1

			if len(group) > 0:
				cx = group[len(group) - 1]["x"]
				cy = group[len(group) - 1]["y"]

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
