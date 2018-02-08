from sys import path
path.append('../core')
path.append('../tools')

from quran import *
from buckwalter import *
from pyquran import *
import arabic as ar
import functools
import time

print("\n[1] Testing get_sura()")
functionCall = ''' Al_Masad = pyquran.get_sura(110)
''' 
print("function call:")
print(functionCall)

print("Output:")
Al_Masad = get_sura(110)
print("Surat Al-Masad:")
print(Al_Masad)


print("\n-----------------------------------------------------------------\n")


print("\n[2] Testing system, count_shape()")
functionCall = '''we will count this system = [[beh, teh, theh], [jeem, hah, khah]] on سورة النصر
''' 
print("function call:")
print(functionCall)
newSystem=[[beh, teh, theh], [jeem, hah, khah]]
print("Return NP array, rows are verses, coulmns this full system :")
#this is the full system
print(list(check_system(newSystem)))

print("Output:")
print("""NOTES:
    * Column i in the following matrix corresponds to the member i in the
      previous system, list.
          Example) Column 0 corresponds to ['ب', 'ت', 'ث'] 
    * Rows = Number of Verses of Surat Al-Nasr
""")
# will count this surah
#print(get_sura(110))
print('\n', count_shape(get_sura(110), newSystem))

print("\n-----------------------------------------------------------------\n")




print("\n[3] Transliteration between Arabic and Buckwalter")
functionCall = '''#from buckwalter to arabic
print(pyquran.buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm mn Alm$rkyn", 1))
#from arabic to buckwalter
print(pyquran.buckwalter_arabic_transliteration(tools.get_sura(9)[0], False))
''' 
print("function call:")
print(functionCall)

print("Output:")
#from buckwalter to arabic
print(buckwalter_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm mn Alm$rkyn", 1))
#from arabic to buckwalter
print(buckwalter_transliteration(get_sura(9)[0], False))



print("\n-----------------------------------------------------------------\n")







print("\n[4] Testing Search()")
sequance = ['ألم تر إلى']
s = time.time()
lis =  search_sequence(sequance,mode=2)
print("Input Key is: ألم ـر إلى " + "\n")
print("Output: \n")
print("time = " + str((time.time()-s)/60) + " seconds")
print("Number of Results " + str(len(  lis[sequance[0]] )) + "\n") 
for key,val in lis.items():
    for su in val:
        print("  Sura: ", get_sura_name(su[3])," Aya: ",su[2] )
        print("  " + get_verse(su[3],su[2], False))





print("\n-----------------------------------------------------------------\n")








print("\n[5] Testing separate_token_with_dicrites()")
print("function call:")
functionCall = '''x = 'وَاشْدُدْ بِهِ أَزْرِي وَأَصْلِحْ شَانِي'
print(pyquran.separate_token_with_dicrites(x))
'''
print(functionCall)


print("Output:")
x = 'وَاشْدُدْ بِهِ أَزْرِي وَأَصْلِحْ شَانِي'
print(separate_token_with_dicrites(x))





print("\n-----------------------------------------------------------------\n")








print("\n[6] search with tashkeel pattern only") 
print("function call:")
functionCall = '''sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
tashkeel_pattern = ar.fatha + ar.sukun
results = pyquran.search_string_with_tashkeel(sentence, tashkeel_pattern)
print(results)
'''
print(functionCall)
print("Output: locations of matches -> (start index *inclusive*, end index *exclusive)")
sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
sen = separate_token_with_dicrites(sentence)
tashkeel_pattern = ar.fatha + ar.sukun
results = search_string_with_tashkeel(sentence, tashkeel_pattern)
print("""NOTE:
    Input is tashkeel pattern.
    Key is  'Fatha Sukun'

Output: 
    Results may be reversed in you terminal, But they are Fatha then Sukun""")
results = results[1]
for x in results:
    print(sen[x[0]:x[1]])



print("\n-----------------------------------------------------------------\n")







print("\n[7] get_frequency()") 
print("function call:")
functionCall = '''print('frequency of سورة النساء aya 164')
freq = get_frequency(get_verse(4,164))
print(freq)
'''
print(functionCall)
print("Output:")
print('frequency of سورة النساء aya 164')
freq = get_frequency(get_verse(4,164))
print(get_verse(4,164))

print("\nOutput ")
print(freq)





print("\n-----------------------------------------------------------------\n")







