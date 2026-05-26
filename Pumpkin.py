import Fertilizer
import Ground
import Water

def Crop():
	obj = {}

	def get_name():
		return "Pumpkin"

	def prepare(drone, plot=None):
		Ground.set_soil()
		Water.use()
		Fertilizer.use()

	def should_harvest(drone, plot=None):
		return can_harvest()

	def plant_entity(drone, plot=None):
		return Entities.Pumpkin

	obj["get_name"] = get_name
	obj["prepare"] = prepare
	obj["should_harvest"] = should_harvest
	obj["plant_entity"] = plant_entity

	return obj