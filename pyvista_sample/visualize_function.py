import time
import pyvista as pv
import pandas as pd
from ela.visual import discrete_classes_colormap
import numpy as np
from matplotlib.colors import ListedColormap
from pyvista_sample.VisualizeDataProcess import VisualizeDataProcess as VDP

dp = VDP()


class VisualizeFunction:
    def __init__(self):
        self.drill_data_path = ''
        self.dem_data_path = ''
        # self.lithology_array_path = ''

    def generating_image(self, dem_data_path, drill_data_path, annotations, sargs):
        return

    def generating_surface_drilling(self, dem_data_path, drill_data_path):
        return

    def dem_surface(self, dem_data_path, height_adjustment_factor=20):
        grid = dp.dem_data_process(dem_data_path, height_adjustment_factor)
        return grid

    def drill_well_dict(self, drill_data_path, height_adjustment_factor=20):
        lines_dict = dp.drill_data_process(drill_data_path, height_adjustment_factor)
        return lines_dict

    def lithology_layer(self, drill_data_path, dem_data_path, storage_file_name, height_adjustment_factor=20,
                        layer_from=0, layer_to=0):
        layers = dp.lithology_layer_process(drill_data_path, dem_data_path, storage_file_name, height_adjustment_factor,
                                            layer_from, layer_to)
        return layers
