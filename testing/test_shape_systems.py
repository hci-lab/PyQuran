import pyquran
from pyquran.tools import quran
from pyquran.tools.arabic import *


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


    # passing system to count_rasm along with Sura.
    count_rasm(Sura, system)
'''

# Preparing a system
syst1 = systems.withoutDots
syst2 = systems.hamazat
defualtSyst = systems.default
newSystem = [[beh, teh, alef], 
             [jeem, hah, khah]]

# Preparing a Sura
sura  = quran.get_sura(108)

# Computing count shape matrix
countMatrix = pyquran.count_rasm(sura)

# Use columnGuide to know which coulmn
# secod parameter is optional, in this case
# the shape at index 5 is returned
# If you do not pass,  it returns all shapes,
# with the same column order.
columnGuide = pyquran.check_system(defualtSyst, 5)

print(columnGuide)
print(countMatrix)


