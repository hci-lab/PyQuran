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
defualtSyst = systems.default
newSystem = [[beh, teh, alef], 
             [jeem, hah, khah]]

# Preparing a Sura
sura  = quran.get_sura(108)

# Computing count shape matrix
countMatrix = pyquran.count_shape(sura)

# Use columnGuide to know which coulmn
# secod parameter is optional, in this case
# the shape at index 5 is returned
# If you do not pass,  it returns all shapes,
# with the same column order.
columnGuide = pyquran.check_system(defualtSyst, 5)

print(columnGuide)
print(countMatrix)




