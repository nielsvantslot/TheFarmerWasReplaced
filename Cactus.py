
import Fertilizer
import Ground
import Water

def do_plant():
	Ground.set_soil()
	plant(Entities.Cactus)

def do_harvest():
	if can_harvest():
		harvest()

def run(plot=None):
	Water.use()
	Fertilizer.use()
	do_harvest()
	do_plant()