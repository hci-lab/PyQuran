
import os

os.chdir('..')
from tools import *
import functools
from arabic import *

'''
#---------------------buckwalter_arabic_transliteration-------------------------
#To DO : Optimize it to just loop on the unique characters

print("-----------buckwalter_arabic_transliteration Example---------------")

#from arabic to buckwalter
print(buckwalter_arabic_transliteration(get_sura(9)[0], False))
#from buckwalter to arabic
print(buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm mn Alm$rkyn", 1))
'''
'''
#---------------------count_token -----------------------------------
print("-----------count token Example---------------")
#number of token in the first verse of Tauba Chapter
print(get_sura(9)[0])
print(count_token(get_sura(9)[0]))

print(get_sura(110))
print(count_token(get_sura(110)))
'''
'''
#---------------------count_token -----------------------------------
print("-----------get Verse count Example---------------")
#number of token in the first verse of Tauba Chapter
print(get_sura(110))
print(get_verse_count(get_sura(110)))
'''
'''
#--------------------- check_all_alphabet  -----------------------------------
newSystem=[[teh, beh, noon],[dal, thal],[jeem, hah, khah],[sad ,dad, tah, zah]]
#it will return the rest of alphabets
print(check_all_alphabet(newSystem))
'''
#--------------------- count shape  -----------------------------------

print("-----------count shape Example---------------")
newSystem=[[teh, beh, noon],[dal, thal],[jeem, hah, khah],[sad ,dad, tah, zah]]
# will count this surah
print(get_sura(110, True))
#this is the full system
print(check_system(newSystem))
#N*P numpy array, row number= verse number and coulmn number =shape number
#NOTE :arabic list will be from right to left, but numpy will be vise verse
print(count_shape(get_sura(110, True), newSystem))



