from sys import path
path.append('../core')
path.append('../tools')

#from pyquran import *
import pyquran
import quran
import arabic

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt  

#newsystem = systems.hamazatSystem
# This is how you use the system object.
# I have saved all the current system in an object.
systems = arabic.systems
#A = count_shape(get_sura(110), newsystem)
A = pyquran.count_shape(quran.get_sura(110), systems.hamazat)

#newsystem = systems.withoutDotSystem
#A = count_shape(get_sura(110), newsystem)
A = pyquran.count_shape(quran.get_sura(110), systems.withoutDots)

pyquran.check_system(systems.hamazat)

print(systems.withoutDots)
print(systems.hamazat)
print(systems.default)
