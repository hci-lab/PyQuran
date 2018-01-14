from tools import *
import time

# #=================================================================
# # test search_sequece function 

# # case 1 : "Search with Taskieel and return Taskieel " mode=1 - all Quran
# sequance = ['صُمٌّ بُكْمٌ عُمْيٌ فَهُمْ']
# s = time.time()
# lis =  search_sequence(sequance,mode=1)
# print((time.time()-s)/60)
# for key,val in lis.items():
#     print("===========================")
#     print(":: ",key)
#     for su in val:
#         print("soura :: ", get_sura_name(su[3])," Aya :: ",su[2] )
#         print(get_verse(su[3],su[2],True))
#     print("===========================")

    
# #case 2 : "Search without Taskieel and return without Taskieel " mode=2 - all Quran
# sequance = ['صم بكم عمي فهم']
# s = time.time()
# lis =  search_sequence(sequance,mode=2)
# print((time.time()-s)/60)
# for key,val in lis.items():
#     print("===========================")
#     print(":: ",key)
#     for su in val:
#         print("soura :: ", get_sura_name(su[3])," Aya :: ",su[2] )
#         print(get_verse(su[3],su[2],True))
#     print("===========================")
    
    
# #case 3 : "Search without Taskieel and return with Taskieel" mode=3 - all Quran
# sequance = ['صم بكم عمي فهم']
# s = time.time()
# lis =  search_sequence(sequance,mode=2)
# print((time.time()-s)/60)
# for key,val in lis.items():
#     print("===========================")
#     print(":: ",key)
#     for su in val:
#         print("soura :: ", get_sura_name(su[3])," Aya :: ",su[2] )
#         print(get_verse(su[3],su[2],True))
#     print("===========================")

    

# #case 4 : looking for word in sura
# sequance = ['أحد','الصمد']
# s = time.time()
# lis =  search_sequence(sequance,chapterNum=112,mode=3)
# print((time.time()-s)/60)
# for key,val in lis.items():
#     print("===========================")
#     print(":: ",key)
#     for su in val:
#         print("soura :: ", get_sura_name(su[3])," Aya :: ",su[2] , " Token :: ",su[1])
#         print(get_verse(su[3],su[2],True))
#     print("===========================")
# #=================================================================






# #=================================================================
# # get frequency of sentence
# print('frequency of اية 1 صورة الاخلاص:::  ')
# freq = get_frequancy(get_verse(112,1))
# print(freq)
# print("=========================")

# #get frequency of sura
# print('frequency of sura الاخلاص :::  ')
# freq = generate_frequancy_dictionary(112)
# print(freq)
# print("=========================")


# #check sura with his frequency dectionary
# print('check if dictionary of sura الاخلاص is right :::  ')
# check = check_sura_with_frequency(112,freq)
# print(check)
# print("=========================")



# #sort dictionary with related words 
# print('sorted dictionary of sura الاخلاص  :::  ')
# sorted_dict = sort_dictionary_by_similarity(freq)
# print(sorted_dict)
# print("=========================")


# #generate tex file of dictionary
# # generate_latex_table(sorted_dict,filename="sorted_dict",location=".")



# #get frequency_of_character in verse
# print('frequency of char in sura الاخلاص اية رقم 1  :::  ')
# freq = frequency_of_character(['ل','لّ'],verseNum=1,chapterNum=112,with_tashkeel=True)
# print(freq)
# print(get_verse(112,1,True))
# print("=========================")


# #=================================================================
