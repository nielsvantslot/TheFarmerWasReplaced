
import Bush
from Drone import drone
import Fertilizer
import Ground
import Tree
import Water

d = drone()

def is_tree_tile():
	return (d["get_x"]() + d["get_y"]()) % 2 == 0

def do_plant():
	if is_tree_tile():
		Tree.do_plant()
	else:
		Bush.do_plant()

def do_harvest():
	if is_tree_tile():
		Tree.do_harvest()
	else:
		Bush.do_harvest()

def run(plot=None):
	Ground.set_grassland()
	Water.use()
	Fertilizer.use()
	do_harvest()
	do_plant()