# Program Name: Program10-NumpyInstallation


# The two main tools that install Python packages are pip and conda. Their functionality partially overlaps (e.g. both can install numpy), however, they can also work together. 

# The first difference is that conda is cross-language and it can install Python, while pip is installed for a particular Python on your system and installs other packages to that same Python install only. This also means conda can install non-Python libraries and tools you may need (e.g. compilers, CUDA, HDF5), while pip can’t.

# The second difference is that pip installs from the Python Packaging Index (PyPI), while conda installs from its own channels (typically “defaults” or “conda-forge”). PyPI is the largest collection of packages by far, however, all popular packages are available for conda as well.

# Conda: If you use conda, you can install NumPy from the defaults or conda-forge channels:
'''
    conda create -n my-env
    conda activate my-env
    conda install numpy
'''


'''
Pip:
pip install numpy
'''

# pip install numpy # write this in terminal


'''
Verifying the NumPy Installation:
After installing NumPy, verify the installation by running the following in a Python shell or script:
'''

import numpy as np
print(np.__version__)
# This should print the installed version of NumPy without errors.


