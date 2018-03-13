# Adding another searching path
from sys import path
import os

# The current path of the current module.
path_current_module = os.path.dirname(os.path.abspath(__file__))


path.append(path_current_module)
