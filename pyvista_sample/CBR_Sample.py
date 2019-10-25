import os
import sys

import pyvista as pv

from pyvista_sample.VisualizeDataProcess import VisualizeDataProcess

pkg_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, pkg_dir)

'''
Canberra sample of 3D visualize based on pyvista
'''

'''Import data'''
if 'ELA_DATA' in os.environ:
    data_path = os.environ['ELA_DATA']
elif sys.platform == 'win32':
    data_path = r'C:\data\Lithology'
else:
    username = os.environ['USER']
    data_path = os.path.join('/home', username, 'data', 'Lithology')


drill_data_path = os.path.join(data_path, 'Canberra', 'out', 'classified_logs.pkl')
dem_data_path = os.path.join(data_path, 'Canberra', 'out', 'dem_array_data.pkl')

"""Data process"""
dp = VisualizeDataProcess()
drill_data = dp.drill_file_read(drill_data_path)

# A convoluted way to remove nans
# vlah = {x for x in drill_data.Lithology_1_num.values if x==x}

# drill_data = drill_data[ drill_data.BoreID == 80000156 ]
# drill_data = drill_data[ drill_data.Lithology_1_num == 10.0 ]

dem_data = dp.dem_file_read(dem_data_path)
lines_dict = dp.drill_data_process(drill_data, 25, min_tube_radius=70)
grid = dp.dem_data_process(dem_data, 25)
layer = dp.lithology_layer_process(drill_data, dem_data, 'cbr', 25, 10, 16)

'''set up the scalar bar and annotations'''
annotations = {
    00.0: 'shale',
    01.0: 'clay',
    02.0: 'granite',
    03.0: 'soil',
    04.0: 'sand',
    05.0: 'porphyry',
    06.0: 'siltstone',
    07.0: 'dacite',
    08.0: 'rhyodacite',
    09.0: 'gravel',
    10.0: 'limestone',
    11.0: 'sandstone',
    12.0: 'slate',
    13.0: 'mudstone',
    14.0: 'rock',
    15.0: 'ignimbrite',
    16.0: 'tuff'
}

sargs = dict(
    n_labels=len(annotations),
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
                     n_colors=len(annotations),
                     nan_color="black",
                     clim=[0, len(annotations) - 1],
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
