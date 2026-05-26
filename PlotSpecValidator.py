CROP_METHODS = ["prepare", "should_harvest", "plant_entity"]
STRATEGY_METHODS = ["before_plot", "run_plot", "after_plot"]


def has_methods(obj, methods):
	if obj == None:
		return False

	i = 0
	while i < len(methods):
		method_name = methods[i]
		if not (method_name in obj):
			return False
		i = i + 1

	return True


def validate_plot_specs(specs):
	i = 0
	while i < len(specs):
		spec = specs[i]
		crop = spec["get_crop"]()
		strategy = spec["get_strategy"]()

		if not has_methods(crop, CROP_METHODS):
			quick_print("Invalid crop contract at spec index: " + str(i))
			return False

		if strategy != None and not has_methods(strategy, STRATEGY_METHODS):
			quick_print("Invalid strategy contract at spec index: " + str(i))
			return False

		i = i + 1

	return True
