import tools 
import arabic as ar
import functools
import time

print("\n[1] Testing get_sura()")
functionCall = ''' Al_Masad = tools.get_sura(111)
''' 
print("function call:")
print(functionCall)

print("Output:")
Al_Masad = tools.get_sura(111)
print("Surat Al-Masad:")
print(Al_Masad)




print("\n[2] Testing system, count_shape()")
functionCall = '''system = [[ar.kaf, ar.feh], [ar.beh, ar.teh, ar.noon], [ar.ghain, ar.ain]]
alphabetAsOneShape, alphabetCount = tools.count_shape(Al_Masad, system)
''' 
print("function call:")
print(functionCall)
newSystem=[[ar.teh, ar.beh, ar.noon],[ar.dal, ar.thal],[ar.jeem, ar.hah,
ar.khah],[ar.sad ,ar.dad, ar.tah, ar.zah]]
# will count this surah
print(tools.get_sura(110, True))






print("\n[3] Transliteration between Arabic and Buckwalter")
functionCall = '''#from buckwalter to arabic
print(tools.buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm mn Alm$rkyn", 1))
#from arabic to buckwalter
print(tools.buckwalter_arabic_transliteration(tools.get_sura(9)[0], False))
''' 
print("function call:")
print(functionCall)

print("Output:")
#from buckwalter to arabic
print(tools.buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm mn Alm$rkyn", 1))
#from arabic to buckwalter
print(tools.buckwalter_arabic_transliteration(tools.get_sura(9)[0], False))






print("\n[4] Testing Search()")
sequance = ['صم بكم عمي فهم']
s = time.time()
lis =  tools.search_sequence(sequance,mode=2)
print("time = " + str((time.time()-s)/60) + " seconds")
for key,val in lis.items():
    print("===========================")
    print(":: ",key)
    for su in val:
        print("soura :: ", tools.get_sura_name(su[3])," Aya :: ",su[2] )
        print(tools.get_verse(su[3],su[2],True))
    print("===========================")







print("\n[5] Testing separate_token_with_dicrites()")
print("function call:")
functionCall = '''x = 'وَاشْدُدْ بِهِ أَزْرِي وَأَصْلِحْ شَانِي'
print(tools.separate_token_with_dicrites(x))
'''
print(functionCall)
x = 'وَاشْدُدْ بِهِ أَزْرِي وَأَصْلِحْ شَانِي'
print(tools.separate_token_with_dicrites(x))






print("\n[6] search with tashkeel pattern only") 
print("function call:")
functionCall = '''sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
tashkeel_pattern = ar.fatha + ar.sukun
results = tools.search_string_with_tashkeel(sentence, tashkeel_pattern)
print(results)
'''
print(functionCall)
print("Output: locations of matches -> (start index *inclusive*, end index *exclusive)")
sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
tashkeel_pattern = ar.fatha + ar.sukun
results = tools.search_string_with_tashkeel(sentence, tashkeel_pattern)
print(results)





print("\n[7] get_frequancy()") 
print("function call:")
functionCall = '''print('frequency of ﺎﻳﺓ 1 سﻭﺭﺓ ﺍﻼﺧﻼﺻ:')
freq = get_frequancy(get_verse(112,1))
print(freq)
'''
print(functionCall)
print("Output:")
print('frequency of ﺎﻳﺓ 1 سﻭﺭﺓ ﺍﻼﺧﻼﺻ:')
freq = tools.get_frequancy(tools.get_verse(112,1))
print(freq)




