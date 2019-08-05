# ela

## Exploratory Lithology Analysis

[![pypi](https://img.shields.io/pypi/v/ela.svg?logo=python&logoColor=white)](https://pypi.org/project/ela/)[![license](http://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/csiro-hydrogeology/pyela/blob/master/LICENSE.txt) ![status](https://img.shields.io/badge/status-alpha-blue.svg) master: [![build](https://img.shields.io/travis/csiro-hydrogeology/pyela.svg?branch=master)](https://travis-ci.org/csiro-hydrogeology/pyela)
[![coverage](https://coveralls.io/repos/github/csiro-hydrogeology/pyela/badge.svg?branch=master)](https://coveralls.io/github/csiro-hydrogeology/pyela?branch=master)


[![codecov](https://codecov.io/gh/csiro-hydrogeology/pyela/branch/master/graph/badge.svg)](https://codecov.io/gh/csiro-hydrogeology/pyela)


[![Getting started tutorial - Bungendore 3D lithology](https://raw.githubusercontent.com/csiro-hydrogeology/pyela-doc/master/tutorials/img/3d_overlay_bungendore_clay_lithology_small.png "Getting started tutorial - Bungendore 3D lithology")](https://github.com/csiro-hydrogeology/pyela-doc/blob/master/tutorials/getting_started.ipynb)

Analysing driller’s logs is a tedious and repetitive task in many groundwater modelling projects. Automating the process of extracting useful information from driller's logs allows spending less time on manual data wrangling, more time on its interpretation, and enhances the reproducibility of the analysis.

This package combines features to:

* perform natural language processing on lithology descriptions in the logs, to detect primary and secondary lithologies
* apply supervised machine learning to interpolate lithologies across a 3D grid
* visualise interactively the 3D data

An introductory [sample workflow](https://github.com/csiro-hydrogeology/pyela-doc/blob/master/tutorials/getting_started.ipynb) gives an overview of some of these capabilities.

## License

MIT (see [License.txt](https://github.com/csiro-hydrogeology/pyela/blob/master/LICENSE.txt))

## Documentation

Tutorials are hosted [in a separate github repository](https://github.com/csiro-hydrogeology/pyela-doc)

Get a [quick tour of the visualisation part of 'ela'](https://github.com/csiro-hydrogeology/pyela/blob/master/docs/visual_tour.md).

## Installation 

As of January 2019 [ela is on pypi](https://pypi.org/project/ela/). While `pip install ela` might work on some computers, it is _unlikely that all python geospatial dependencies will install_. *We highly recommend you set up a conda environment with all dependent packages* prior to installing ela with pip or from source.

'ela' relies on several external packages, and some can be fiddly to install depending on the version of Python and these external packages. This section thus has fairly prescriptive instructions, given in the hope of limiting the risk of issues.

### Debian packages for spatial projections

`cartopy` and possibly other python packages require `proj4` version 4.9+ to be installed (libproj-dev). If your debian/ubuntu repo does not suffice (older versions) you may try:

```bash
sudo apt-get install -y libc6  
wget http://en.archive.ubuntu.com/ubuntu/pool/universe/p/proj/proj-data_4.9.3-2_all.deb
sudo dpkg -i proj-data_4.9.3-2_all.deb
wget http://en.archive.ubuntu.com/ubuntu/pool/universe/p/proj/libproj12_4.9.3-2_amd64.deb
sudo dpkg -i libproj12_4.9.3-2_amd64.deb
wget http://en.archive.ubuntu.com/ubuntu/pool/universe/p/proj/proj-bin_4.9.3-2_amd64.deb
sudo dpkg -i proj-bin_4.9.3-2_amd64.deb
wget http://en.archive.ubuntu.com/ubuntu/pool/universe/p/proj/libproj9_4.9.2-2_amd64.deb 
sudo dpkg -i libproj9_4.9.2-2_amd64.deb
wget http://en.archive.ubuntu.com/ubuntu/pool/universe/p/proj/libproj-dev_4.9.3-2_amd64.deb
sudo dpkg -i libproj-dev_4.9.3-2_amd64.deb
```

### Installation of python packages dependencies

We recommend install [Anaconda](http://docs.continuum.io/anaconda/install) to install dependencies. Note that I recommend to **not** let anaconda change your startup file and change the `PATH` environment. To activate Anaconda you first need: `source ~/anaconda3/bin/activate`. Then choose a conda environment name.

Optionally, if your anaconda installation is a bit dated, you may want to do `conda update -n base conda` and `conda update -n base anaconda-navigator`

To create the conda environment for ela on Linux:

```bash
# source ~/anaconda3/bin/activate
my_env_name=ELA
conda create --name ${my_env_name} python=3.7
conda install --name ${my_env_name} rasterio cartopy geopandas pandas nltk scikit-learn scikit-image matplotlib vtk
conda activate  ${my_env_name}
```

On Windows, using the DOS CMD prompt, assuming you installed Anaconda in user mode.

```bat
call %userprofile%\AppData\Local\Continuum\anaconda3\Scripts\activate.bat
set my_env_name=ELA
conda create --name %my_env_name% python=3.7
REM if using conda activate  %my_env_name%  I seem to loose conda from the command line, so:
conda install --name %my_env_name% conda 
conda install --name %my_env_name% rasterio cartopy geopandas pandas nltk scikit-learn scikit-image matplotlib vtk
conda activate  %my_env_name%
```

At this point we have installed all the python dependencies ela needs that are available via `conda`.

As of writing (2019-08) conda does not have pyqt5, and no suitable version of mayavi for python3. We resort to use `pip`. You may want to do first:

```bash
pip install --upgrade pip
```

For Python 3.x one needs to install pyqt5 for mayavi, as per [these instructions](https://docs.enthought.com/mayavi/mayavi/installation.html). As of Jan 2019 be aware that there is a [known issue in mayavi visual rendering with pyqt5 as a backend on Linux](https://github.com/enthought/mayavi/issues/656) and 'ela' is affected by this. Nevertheless this is not a commplete blocker for most 'ela' features so installation instructions are kept here.

```bash
pip search pyqt5 | sort -g
pip search mayavi
```

```bash
pip install pyqt5
pip install mayavi
```

At this point all mandatory dependencies for 'ela' are installed.

### Installing ELA

There are three options to access ela:

* use the latest available on pip, 
* clone and install with `setup.py`
* direct import of the package directory (this is done at runtime from e.g. a notebook)

```bash
pip search ela
pip install ela
```

Alternatively, from source with `setup.py`

```bash
pip install -r requirements.txt
python setup.py install
```

#### Optional dependencies

As of 2019-05 you can find new features using deep learning for classification in the submodule `ela.experiment`. You will need the additional dependencies:

```bash
conda install --name ${my_env_name} gensim tensorflow keras
pip install wordcloud
```

If reading xls files using pandas, need pkg `xlrd` with e.g. `conda install xlrd`

### using Jupyter-lab

You may use ela as you prefer; we recomment using "Jupyter Lab" to write notebooks. See the [Jupyter lab doc](https://jupyterlab.readthedocs.io/en/stable/) for official information. 

The following should be enough otherwise to use 'ela'

Linux:

```sh
my_env_name=ELA
conda install --name ${my_env_name} jupyterlab ipywidgets jupyter
jupyter-labextension install @jupyter-widgets/jupyterlab-manager
python -m ipykernel install --user --name ${my_env_name} --display-name "Py3 ELA"
```

Windows: 

```bat
set my_env_name=ELA
conda install --name %my_env_name% jupyterlab ipywidgets jupyter
jupyter-labextension install @jupyter-widgets/jupyterlab-manager
python -m ipykernel install --user --name %my_env_name% --display-name "Py3 ELA"
```

## Related Geoscience packages

'ela' aims to complement other Python packages for geoscience, in particular for handling bore data . It already depends on the package ['striplog'](https://github.com/agile-geoscience/striplog) and is likely to depend on ['lasio'](https://github.com/kinverarity1/lasio) in the future.

You should also check the repository [hydrogeol_utils](https://github.com/Neil-Symington/hydrogeol_utils)

## Known issues

3D interactive visualisation - Using mayavi 4.6+ on python 3.6+ may be [visually buggy](https://github.com/enthought/mayavi/issues/656) on Linux. This appears to be a low level issue running on laptop with dual Intel/NVIDIA Graphic cards.

## Troubleshooting

If in a conda environment trying to use `pip` you get:

```text
ModuleNotFoundError: No module named 'pip._internal'
```

consider:

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --force-reinstall
```