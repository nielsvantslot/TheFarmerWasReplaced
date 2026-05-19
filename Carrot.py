
import Fertilizer
import Ground
import Water

def do_plant():
	plant(Entities.Carrot)

def do_harvest():
	if can_harvest():
		harvest()

def run(plot=None):
	Ground.set_soil()
	Water.use()
	Fertilizer.use()
	do_harvest()
	do_plant()