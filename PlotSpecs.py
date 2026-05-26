from Crops import Carrot
from Crops import Cactus
from Crops import Grass
from Crops import Pumpkin
from Crops import Sunflower
from Crops import Wood
from Plots import PlotSpec
from Plots import CactusPlotStrategy
from Plots import PumpkinPlotStrategy
from Plots import SunflowerPlotStrategy

plot_specs = [
	PlotSpec(Grass,     None,                Hats.Straw_Hat),
	PlotSpec(Carrot,    None,                Hats.Traffic_Cone),
	PlotSpec(Pumpkin,   PumpkinPlotStrategy, Hats.Pumpkin_Hat),
	PlotSpec(Wood,      None,                Hats.Brown_Hat),
	PlotSpec(Sunflower, SunflowerPlotStrategy, Hats.Sunflower_Hat),
	PlotSpec(Cactus,    CactusPlotStrategy,  Hats.Cactus_Hat),
]
