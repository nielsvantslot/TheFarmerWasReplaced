import Ground

def Crop():
	obj = {}

	def get_name():
		return "Grass"

	def prepare(drone, plot=None):
		Ground.set_grassland()

	def should_harvest(drone, plot=None):
		return can_harvest()

	def plant_entity(drone, plot=None):
		return None

	obj["get_name"] = get_name
	obj["prepare"] = prepare
	obj["should_harvest"] = should_harvest
	obj["plant_entity"] = plant_entity

	return obj