from Drone import drone

drone = drone()

def run(plot, lane_x):
	y1 = plot["get_y1"]()
	y2 = plot["get_y2"]()

	drone["move_to"](lane_x, y1)

	while drone["get_y"]() <= y2:
		plot["get_crop"]().run(plot)
		if drone["get_y"]() == y2:
			break
		if drone["get_y"]() < y2:
			drone["up"]()
