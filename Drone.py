import World

_instance = None

def drone():
	global _instance
	if _instance != None:
		return _instance

	self = {
		"x": get_pos_x(),
		"y": get_pos_y(),
		"hat": None,
	}

	obj = {}

	# =========================
	# Internal helpers
	# =========================

	def step(direction):
		size = World.size()
		move(direction)

		if direction == North:
			self["y"] = (self["y"] + 1) % size

		elif direction == South:
			self["y"] = (self["y"] - 1) % size

		elif direction == East:
			self["x"] = (self["x"] + 1) % size

		elif direction == West:
			self["x"] = (self["x"] - 1) % size


	def direction_x(tx):
		size = World.size()

		dx = (tx - self["x"]) % size

		if dx == 0:
			return None

		if dx < size - dx:
			return East

		return West


	def direction_y(ty):
		size = World.size()

		dy = (ty - self["y"]) % size

		if dy == 0:
			return None

		if dy < size - dy:
			return North

		return South


	# =========================
	# Public API
	# =========================

	def move_to(x, y):
		while self["x"] != x:
			d = direction_x(x)

			if d == None:
				break

			step(d)

		while self["y"] != y:
			d = direction_y(y)

			if d == None:
				break

			step(d)


	def up():
		step(North)


	def down():
		step(South)


	def left():
		step(West)


	def right():
		step(East)
	
	def get_x():
		return self["x"]
	
	def get_y():
		return self["y"]

	def set_hat(hat):
		if hat == None:
			return

		self["hat"] = hat

		change_hat(hat)


	# =========================
	# Expose methods
	# =========================

	obj["move_to"] = move_to
	obj["up"] = up
	obj["down"] = down
	obj["left"] = left
	obj["right"] = right
	obj["get_x"] = get_x
	obj["get_y"] = get_y
	obj["set_hat"] = set_hat

	# optional state exposure
	obj["state"] = self

	_instance = obj

	return _instance