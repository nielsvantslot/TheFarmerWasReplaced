
import Ground

def do_plant():
	return

def do_harvest():
	if can_harvest():
		harvest()

def run(plot=None):
	Ground.set_grassland()
	do_harvest()
	do_plant()