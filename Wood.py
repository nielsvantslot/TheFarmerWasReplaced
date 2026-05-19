
from Drone import drone
import Fertilizer
import Ground
import Water

d = drone()

def do_plant():
	if (d["get_x"]() + d["get_y"]()) % 2 == 0:
		plant(Entities.Tree)
	plant(Entities.Bush)

def do_harvest():
	if can_harvest():
		harvest()

def run(plot=None):
	Ground.set_grassland()
	Water.use()
	Fertilizer.use()
	do_harvest()
	do_plant()