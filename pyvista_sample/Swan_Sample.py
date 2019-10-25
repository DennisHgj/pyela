import os
import sys

import pyvista as pv

from pyvista_sample.VisualizeDataProcess import VisualizeDataProcess

# start = time.clock()
'''
Swan coastal sample of 3D image based on pyvista
'''

'''Import data'''
pkg_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, pkg_dir)
# drill_data_path = r"C:\Users\Dennis.H\Desktop\CSIRO_data\swan_coastal\classified_logs.pkl"
# dem_data_path = r"C:\Users\Dennis.H\Desktop\CSIRO_data\swan_coastal\dem_array_data.pkl"
if 'ELA_DATA' in os.environ:
    data_path = os.environ['ELA_DATA']
elif sys.platform == 'win32':
    data_path = r'C:\data\Lithology'
else:
    username = os.environ['USER']
    data_path = os.path.join('/home', username, 'data', 'Lithology')

drill_data_path = os.path.join(data_path, 'swan_coastal', 'classified_logs.pkl')
dem_data_path = os.path.join(data_path, 'swan_coastal', 'dem_array_data.pkl')
"""Data process"""
dp = VisualizeDataProcess()
drill_data = dp.drill_file_read(drill_data_path)
dem_data = dp.dem_file_read(dem_data_path)
lines_dict = dp.drill_data_process(drill_data, 25, min_tube_radius=70)
grid = dp.dem_data_process(dem_data, 25)
layer = dp.lithology_layer_process(drill_data, dem_data, 'swan', 25, 7, 10)

'''set up the scalar bar and annotations'''
annotations = {
    0.00: "Sand",
    1.00: "Clay",
    2.00: "Quartz",
    3.00: "Shale",
    4.00: "Sandstone",
    5.00: "Coal",
    6.00: "Pebbles",
    7.00: "silt",
    8.00: "pyrite",
    9.00: "Grit",
    10.00: "limestone",
}

sargs = dict(
    n_labels=11,
    bold=False,
    interactive=False,
    label_font_size=8,
    fmt="%.1f",
    font_family="arial",
    vertical=True,
    position_x=1,
    position_y=0.45,
    height=0.5,
)

'''visualized by Pyvista'''
plotter = pv.Plotter()

'''Two ways of visualizing borehole data, as several meshes or combine as one mesh'''
'''meshes'''
'''
for well in lines_dict.keys():
    plotter.add_mesh(lines_dict.get(well),
                     scalars=dp.scalar_prop_name,
                     scalar_bar_args=sargs,
                     annotations=annotations,
                     show_edges=False,
                     edge_color="white",
                     n_colors=11,
                     nan_color="black",
                     clim=[0, 10],
                     opacity=1,
                     )
'''

'''one mesh'''
borehole_data = pv.PolyData()
for well in lines_dict.keys():
    borehole_data.boolean_add(lines_dict.get(well), inplace=True)
plotter.add_mesh(borehole_data,
                 scalars=dp.scalar_prop_name,
                 scalar_bar_args=sargs,
                 annotations=annotations,
                 show_edges=False,
                 edge_color="white",
                 n_colors=len(annotations),
                 nan_color="black",
                 clim=[0, len(annotations) - 1],
                 opacity=1,
                 )

plotter.add_mesh(layer, scalars="Lithology", n_colors=len(annotations), clim=[0, len(annotations) - 1],
                 show_scalar_bar=False)
plotter.add_mesh(grid, opacity=0.9)
plotter.show_bounds(grid, show_xaxis=True, show_yaxis=True, show_zaxis=False)
plotter.show_axes()
plotter.show()
plotter.close()
