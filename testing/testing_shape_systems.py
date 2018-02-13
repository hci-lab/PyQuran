from sys import path
path.append('../tools/')
path.append('../core/')

import systems
import pyquran
import quran
from arabic import *


'''
example
=======


    # pre-defined system
    systems.withoutDotSystem

    # another pre-defined system
    systems.hamazatSystem


    # user defined system
    newSystem = [[beh, teh, theh], 
                 [jeem, hah, khah]]


    # passing system to count_shape along with Sura.
    count_shape(Sura, system)
'''

# Preparing a system
syst1 = systems.withoutDotSystem
syst2 = systems.hamazatSystem
newSystem = [[beh, teh, alef], 
             [jeem, hah, khah]]

# Preparing a Sura
sura  = quran.get_sura(108)

# Computing count shape matrix
countMatrix = pyquran.count_shape(sura, syst1)

# Use columnGuide to know which coulmn
columnGuide = pyquran.check_system(syst1, 5)

print(columnGuide)
print(countMatrix)




