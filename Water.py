import Ground

WATER_THRESHOLD = 0.75

def use_water():
	while (Ground.get_water_level() < WATER_THRESHOLD
		   and num_items(Items.Water) > 0):
		use_item(Items.Water)

def use():
	use_water()
	