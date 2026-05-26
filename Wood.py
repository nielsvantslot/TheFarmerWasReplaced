import Fertilizer
import Ground
import Water
import Bush
import Tree
import Maze

wood_state = {
	"maze_triggered_this_pass": False,
	"skip_next_pass": False,
}

def reset_maze_state():
	if wood_state["skip_next_pass"]:
		wood_state["skip_next_pass"] = False
		wood_state["maze_triggered_this_pass"] = True
	else:
		wood_state["maze_triggered_this_pass"] = False

def Crop():
	bush = Bush.Crop()
	tree = Tree.Crop()
	obj = {}

	def get_name():
		return "Wood"

	def is_tree_tile(drone_obj, plot):
		if use_single_maze_bush(plot):
			return not is_maze_trigger_tile(drone_obj, plot)

		return (drone_obj["get_x"]() + drone_obj["get_y"]()) % 2 == 0

	def use_single_maze_bush(plot):
		if plot == None:
			return False

		return num_unlocked(Unlocks.Mazes) > 0

	def get_maze_trigger_position(plot):
		x2 = plot["get_x2"]()
		y2 = plot["get_y2"]()

		return x2, y2

	def is_maze_trigger_tile(drone_obj, plot):
		if not use_single_maze_bush(plot):
			return False

		tx, ty = get_maze_trigger_position(plot)
		return drone_obj["get_x"]() == tx and drone_obj["get_y"]() == ty

	def prepare(drone_obj, plot=None):
		Ground.set_grassland()
		Water.use()

		if is_maze_trigger_tile(drone_obj, plot) and not wood_state["maze_triggered_this_pass"] and can_harvest():
			Maze.try_run_and_harvest_maze(drone_obj)
			wood_state["maze_triggered_this_pass"] = True
			wood_state["skip_next_pass"] = True

	def should_harvest(drone_obj, plot=None):
		if is_tree_tile(drone_obj, plot):
			return tree["should_harvest"](drone_obj, plot)

		if use_single_maze_bush(plot):
			if is_maze_trigger_tile(drone_obj, plot):
				return bush["should_harvest"](drone_obj, plot)

			return tree["should_harvest"](drone_obj, plot)

		return bush["should_harvest"](drone_obj, plot)

	def plant_entity(drone_obj, plot=None):
		if is_tree_tile(drone_obj, plot):
			Fertilizer.use()
			return tree["plant_entity"](drone_obj, plot)

		if use_single_maze_bush(plot):
			if is_maze_trigger_tile(drone_obj, plot):
				return bush["plant_entity"](drone_obj, plot)

			Fertilizer.use()
			return tree["plant_entity"](drone_obj, plot)
		
		return bush["plant_entity"](drone_obj, plot)
	
	def reset_maze_state():
		wood_state["maze_triggered_this_pass"] = False

	obj["get_name"] = get_name
	obj["prepare"] = prepare
	obj["should_harvest"] = should_harvest
	obj["plant_entity"] = plant_entity
	obj["reset_maze_state"] = reset_maze_state

	return obj
