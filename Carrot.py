import Fertilizer
import Ground
import Water

def Crop():
	obj = {}

	def get_name():
		return "Carrot"

	def prepare(drone, plot=None):
		Ground.set_soil()
		Fertilizer.use()
		Water.use()

	def should_harvest(drone, plot=None):
		return can_harvest()

	def plant_entity(drone, plot=None):
		return Entities.Carrot

	obj["get_name"] = get_name
	obj["prepare"] = prepare
	obj["should_harvest"] = should_harvest
	obj["plant_entity"] = plant_entity

	return obj