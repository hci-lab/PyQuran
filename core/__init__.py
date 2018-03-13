# Adding another searching path
from sys import path
import os

# The current path of the current module.
path_current_module = os.path.dirname(os.path.abspath(__file__))
tools_modules = '../tools/'
tools_path = os.path.join(path_current_module, tools_modules)

path.append(tools_path)

