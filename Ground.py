def is_grassland():
	return get_ground_type() == Grounds.Grassland

def set_grassland():
	if not is_grassland():
		till()

def is_soil():
	return get_ground_type() == Grounds.Soil

def set_soil():
	if not is_soil():
		till()

def get_water_level():
	return get_water()