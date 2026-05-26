import Maze

def Crop():
	obj = {}

	def get_name():
		return "Bush"

	def prepare(drone, plot=None):
		Maze.try_run_and_harvest_maze(drone)

	def should_harvest(drone, plot=None):
		return can_harvest()

	def plant_entity(drone, plot=None):
		return Entities.Bush

	obj["get_name"] = get_name
	obj["prepare"] = prepare
	obj["should_harvest"] = should_harvest
	obj["plant_entity"] = plant_entity

	return obj
