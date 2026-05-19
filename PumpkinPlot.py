from Drone import drone
from Crops import Pumpkin

drone = drone()

def run(plot):
	cleanup_dead_pumpkins(plot)

def cleanup_dead_pumpkins(plot):
	first_pass = True
	planted_pumpkins = 0

	x1 = plot["get_x1"]()
	x2 = plot["get_x2"]()
	y1 = plot["get_y1"]()
	y2 = plot["get_y2"]()
	
	while first_pass or planted_pumpkins > 0:
		first_pass = False
		planted_pumpkins = 0
		drone["move_to"](x1, y1)

		x = x1

		while x <= x2:
			y = y1

			while y <= y2:
				if get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
					Pumpkin.do_plant()
					planted_pumpkins = planted_pumpkins + 1
				if get_entity_type() == None:
					Pumpkin.do_plant()
					planted_pumpkins = planted_pumpkins + 1
				drone["up"]()
				y = y + 1

			if x < x2:
				x = x + 1
				drone["move_to"](x, y1)
			else:
				x = x + 1
