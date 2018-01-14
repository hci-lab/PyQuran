from tools import *
import functools
from arabic import *


#---------------------buckwalter_arabic_transliteration-------------------------
#To DO : Optimize it to just loop on the unique characters

print("-----------buckwalter_arabic_transliteration Example---------------")

#from arabic to buckwalter
print(buckwalter_arabic_transliteration(get_sura(9)[0], False))
#from buckwalter to arabic
print(buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm mn Alm$rkyn", 1))


#---------------------count_token -----------------------------------
print("-----------count token Example---------------")
#number of token in the first verse of Tauba Chapter
print(get_sura(9)[0])
print(count_token(get_sura(9)[0]))

print(get_sura(110))
print(count_token(get_sura(110)))

#---------------------count_token -----------------------------------
print("-----------get Verse count Example---------------")
#number of token in the first verse of Tauba Chapter
print(get_sura(110))
print(get_verse_count(get_sura(110)))

#--------------------- count shape  -----------------------------------

print("-----------count shape Example---------------")
#newSystem=[[teh,beh,teh,noon],[dal,thal],[jeem,hah,khah],[sad,dad,tah,zah],
# [ain,ghain]]
    #newSystem=[['r']]
    #print (shape(newSystem))

alphabetAsOneShape, alphabetCount =count_shape(['إذا جاء نصر الله والفتح', 'ورأيت الناس يدخلون في دين الله أفواجا', 'فسبح بحمد ربك واستغفره إنه كان توابا'],[[beh, teh, theh], [jeem, hah, khah]])


printf = functools.partial(print, end=" ")
for key in alphabetAsOneShape:  # .encode("utf-8")
    for val in alphabetAsOneShape[key]:
        printf(val)
    print(" : " + str(alphabetCount[key]))
