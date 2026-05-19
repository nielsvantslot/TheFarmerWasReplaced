def do_plant():
	plant(Entities.Bush)

def do_harvest():
	if get_entity_type() == Entities.Bush and can_harvest():
		harvest()
