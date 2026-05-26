def try_run_and_harvest_maze(drone):
	if num_unlocked(Unlocks.Mazes) <= 0:
		return False

	if get_entity_type() != Entities.Bush:
		return False

	start_x = drone["state"]["x"]
	start_y = drone["state"]["y"]

	amount = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
	if amount <= 0:
		return False

	if not use_item(Items.Weird_Substance, amount):
		return False

	harvested = harvest_treasure_in_current_maze(drone)
	if harvested:
		drone["move_to"](start_x, start_y)

	return harvested


def harvest_treasure_in_current_maze(drone):
	treasure = measure()
	if treasure == None:
		return False

	target_x = treasure[0]
	target_y = treasure[1]
	world_size = get_world_size()

	state = drone["state"]
	start_key = key_for(state["x"], state["y"])
	visited = {start_key: True}
	blocked = {}
	path = [{"x": state["x"], "y": state["y"]}]

	while len(path) > 0:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return True

		current = path[len(path) - 1]
		cx = current["x"]
		cy = current["y"]
		directions = ordered_directions(cx, cy, target_x, target_y, world_size)
		moved = False

		i = 0
		while i < len(directions):
			direction = directions[i]
			blocked_key = edge_key(cx, cy, direction)
			if blocked_key in blocked:
				i = i + 1
				continue

			nx, ny = neighbor_position(cx, cy, direction, world_size)
			next_key = key_for(nx, ny)

			if next_key in visited:
				i = i + 1
				continue

			if move_checked(drone, direction):
				visited[next_key] = True
				path.append({"x": nx, "y": ny})
				moved = True
				break

			blocked[blocked_key] = True
			i = i + 1

		if moved:
			continue

		if len(path) == 1:
			break

		previous = path[len(path) - 2]
		back_direction = direction_from_to(cx, cy, previous["x"], previous["y"], world_size)
		if back_direction == None:
			break

		if not move_checked(drone, back_direction):
			break

		path.pop()

	return False


def move_checked(drone, direction):
	moved = move(direction)
	if not moved:
		return False

	state = drone["state"]
	world_size = get_world_size()

	if direction == North:
		state["y"] = (state["y"] + 1) % world_size
	elif direction == South:
		state["y"] = (state["y"] - 1) % world_size
	elif direction == East:
		state["x"] = (state["x"] + 1) % world_size
	elif direction == West:
		state["x"] = (state["x"] - 1) % world_size

	return True


def ordered_directions(x, y, tx, ty, world_size):
	preferred = []
	used = {}

	x_direction = preferred_x_direction(x, tx, world_size)
	y_direction = preferred_y_direction(y, ty, world_size)

	if x_direction != None:
		preferred.append(x_direction)
		used[direction_name(x_direction)] = True

	if y_direction != None:
		dir_name = direction_name(y_direction)
		if not (dir_name in used):
			preferred.append(y_direction)
			used[dir_name] = True

	all_directions = [North, East, South, West]
	i = 0
	while i < len(all_directions):
		direction = all_directions[i]
		dir_name = direction_name(direction)
		if not (dir_name in used):
			preferred.append(direction)
			used[dir_name] = True
		i = i + 1

	return preferred


def preferred_x_direction(x, tx, world_size):
	dx = (tx - x) % world_size
	if dx == 0:
		return None
	if dx < world_size - dx:
		return East
	return West


def preferred_y_direction(y, ty, world_size):
	dy = (ty - y) % world_size
	if dy == 0:
		return None
	if dy < world_size - dy:
		return North
	return South


def neighbor_position(x, y, direction, world_size):
	if direction == North:
		return x, (y + 1) % world_size
	if direction == South:
		return x, (y - 1) % world_size
	if direction == East:
		return (x + 1) % world_size, y
	return (x - 1) % world_size, y


def direction_from_to(x1, y1, x2, y2, world_size):
	if (x1 + 1) % world_size == x2 and y1 == y2:
		return East
	if (x1 - 1) % world_size == x2 and y1 == y2:
		return West
	if (y1 + 1) % world_size == y2 and x1 == x2:
		return North
	if (y1 - 1) % world_size == y2 and x1 == x2:
		return South
	return None


def key_for(x, y):
	return str(x) + "," + str(y)


def edge_key(x, y, direction):
	return key_for(x, y) + ":" + direction_name(direction)


def direction_name(direction):
	if direction == North:
		return "N"
	if direction == East:
		return "E"
	if direction == South:
		return "S"
	return "W"
