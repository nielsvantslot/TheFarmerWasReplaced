def do_plant():
	plant(Entities.Tree)

def do_harvest():
	if get_entity_type() == Entities.Tree and can_harvest():
		harvest()
