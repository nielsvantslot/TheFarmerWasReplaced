def truncate(value):
	return value // 1

def get_plot_index(pos_x, plot_width, num_plots):
	return min(num_plots - 1, truncate(pos_x / plot_width))