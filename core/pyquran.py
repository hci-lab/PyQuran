"""Main PyQuran Library  Module

* Data: Sat Nov 18 03:30:41 EET 2017

This module contains tools for `Quranic Analysis`
(More expressive description later) 

"""
# Adding another searching path
from sys import path
path.append('../tools/')

import numpy
import operator
from audioop import reverse
import difflib as dif
from itertools import chain
import functools
from collections import Counter, defaultdict
from arabic import *
import re
from pyarabic.araby import strip_tashkeel, strip_tatweel,separate,strip_tatweel
from searchHelper import *
from buckwalter import *
from quran import *
import sys


def parse_sura(n, alphabets=['ل', 'ب']):
    """parses the sura and returns a matrix (ndarray),
    the rows number equals to the ayat number,
    and the columns number equals to the length of alphabets

    What it does:
        it calculates number of occurrences of each on of letters
        in the alphabets for each aya.

        If `A` is a ndarray, 
        then A[i,j] is the number of occurrences of the letter 
        alphabets[j] in the aya i.

    Args:
        param1 (int): the ordered number of sura in The Mus'haf.
        param2 ([str]): a list of alphabets

    Returns:
        ndarray: with dimensions (a * m), where
        `a` is the number of ayat el-sura and
        `m` is the number of letters passed to the function through alphabets[]

    Issue:
        1. A list of Arabic letters maybe flipped by your editor,
           so, the first char will be the most-right one,
           unlike a list of English char, the first element 
           is the left-most one.

        2. I didn't make alphabets[] 29 by default. 
           Just try it by filling the alphabets with some letters.
    
    """
    # getting the nth sura
    sura  = get_sura(n)
    # getting the ndarray dimensions 
    a = len(sura)
    m = len(alphabets)
    # building ndarray with appropriate dimensions 
    A = numpy.zeros((a,m), dtype=numpy.int)


    # Filling ndarray with alphabets[] occurrences
    i = 0 # number of current aya
    j = 0 # occurrences
    for aya in sura:
        for letter in alphabets:
            A[i,j] = aya.count(letter)
            j += 1
        j = 0
        i += 1
 
    return A





def get_frequency(sentence):
    """it take sentence that you want to compute it's 
       words frequency.

    Args:
        sentence (string): sentece that compute it's frequency. 

    Returns:
        dict: {str: int}
    """
    # split sentence to words     
    word_list = sentence.split()
    #compute count of uniqe words 
    frequency = Counter(word_list)
    #sort frequency descending
    sorted_freq = dict(sorted(frequency.items(),key=operator.itemgetter(1),reverse=True))
    return sorted_freq
    

    
def generate_frequency_dictionary(suraNumber=None):
    """It takes and ordered number of a sura, and returns the dictionary:
       * key is the word.  value is its frequency in the Sura.
       - If you don't pass any parameter, then the entire Quran is targeted.
       - This function have to work on the Quran with تشكيل, because it's an..
         important factor.

    Args:
        suraNumber (int): it's optional 

    Returns:
        dict: {str: int}
    """
    frequency = {}
    #get all Quran if suraNumber is None
    if suraNumber == None:
        #get all Quran as one sentence
        Quran = ' '.join([' '.join(get_sura(i)) for i in range(1,115)])
        #get all Quran frequency
        frequency=get_frequency(Quran)
    #get frequency of suraNumber
    else:
        #get sura from QuranCorpus
        sura = get_sura(sura_number=suraNumber)
        ayat = ' '.join(sura)
        #get frequency of sura 
        frequency = get_frequency(ayat)

    return frequency


def check_sura_with_frequency(sura_num,freq_dec):
    """this function check if frequency dictionary of specific sura is
    compatible with original sura in shapes count

    Args:
        suraNumber (int): sura number 

    Returns:
        Boolean: True :- if compatible 
                 Flase :- if not
    """
    #get number of chars in frequency dec
    num_of_chars_in_dec = sum([len(word)*count for word,count in freq_dec.items()])
    #get number of chars in  original sura
    num_of_chars_in_sura = sum([len(aya.replace(' ',''))  for aya in get_sura(sura_num)])
    # print(num_of_chars_in_dec ,"    ", num_of_chars_in_sura)
    if num_of_chars_in_dec == num_of_chars_in_sura:
        return True
    else:
        return False
    
    



def sort_dictionary_by_similarity(frequency_dictionary,threshold=0.8):
    """this function using to cluster words using similarity 
       and sort every bunch of word  by most common and sort bunches 
       descending in same time 
    
       Args:
          frequency_dictionary (dict): frequency dictionary that need to sort
       Returns:
          dict : sorted dictionary 
    """
    # list of dictionaries and every dictionary has similar words and we will call every dictionary as 'X'
    list_of_dics = []
    # this dictionary key is a position of 'X' and value the sum of frequencies of 'X'
    list_of_dics_counts = dict()
    #counter of X's
    dic_num=0
    #lock list used to lock word that added in 'X'
    occurrence_list = set()
    #loop on all words to cluster them
    for word,count in frequency_dictionary.items():
        #check if word is locked from some 'X' or not
        if word not in occurrence_list:
            #this use to sum all of frequencies of this 'X'
            sum_of_freqs = count
            #create new 'X' and add the first word
            sub_dic = dict({word:count}) 
            #add word in occurrence list to lock it
            occurrence_list.add(word)
            #loop in the rest word to get similar word
            for sub_word,sub_count in frequency_dictionary.items():
                #check if word lock or not
                if sub_word not in occurrence_list:
                    #compute similarity probability 
                    similarity_prob = dif.SequenceMatcher(None,word,sub_word).ratio()
                    # check if prob of word is bigger than threshold or not
                    if similarity_prob >= threshold:
                        #add sub_word as a new word in this 'X'
                        sub_dic[sub_word] = sub_count
                        # lock this new word
                        occurrence_list.add(sub_word)
                        # add the frequency of this new word to sum_of_freqs
                        sum_of_freqs +=sub_count
            #append 'X' in list of dictionaries
            list_of_dics.append(sub_dic)
            #append position and summation of this 'X' frequencies
            list_of_dics_counts[dic_num] = sum_of_freqs
            # increase number of dictionaries 
            dic_num +=1
    #sort list of dictionaries count (sort X's descending) The most frequent
    list_of_dics_counts = dict(sorted(list_of_dics_counts.items(),key=operator.itemgetter(1),reverse=True))
    #new frequency dictionary that will return 
    new_freq_dic =dict()
    #loop to make them as one dictionary after sorting
    for position in list_of_dics_counts.keys():
        new_sub_dic = dict(sorted(list_of_dics[position].items(),key=operator.itemgetter(1),reverse=True))
        for word,count in new_sub_dic.items():
            new_freq_dic[word] = count

    return new_freq_dic        



def generate_latex_table(dictionary,filename,location="."):
    """generate latex code of table of frequency 
    
    Args:
        dictionary (dict): frequency dictionary
        filename (string): file name 
        location (string): location to save , the default location is same directory
    Returns:
        Boolean: True :- if Done 
                 Flase :- if something wrong with folder name    
        
    """
    head_code = """\\documentclass{article}
%In the preamble section include the arabtex and utf8 packages
\\usepackage{arabtex}
\\usepackage{utf8}
\\usepackage{longtable}    
\\usepackage{color, colortbl}
\\usepackage{supertabular}
\\usepackage{multicol}
\\usepackage{geometry} 
\\geometry{left=.1in, right=.1in, top=.1in, bottom=.1in}

\\begin{document}
\\begin{multicols}{6}
\\setcode{utf8}

\\begin{center}"""
            
    tail_code = """\\end{center}
\\end{multicols}
\\end{document}"""
      
    begin_table = """\\begin{tabular}{ P{2cm}  P{1cm}} 
\\textbf{words}    & \\textbf{\\#}  \\\\
\\hline
\\\\[0.01cm]"""
    end_table= """\\end{tabular}"""
    rows_num = 40
    if location != '.':
         filename = location +"/"+ filename
    
    try:     
        file  = open(filename+'.tex', 'w', encoding='utf8')
        file.write(head_code+'\n')
        n= int(len(dictionary)/rows_num)
        words = [("\\<"+word+"> & "+str(frequancy)+' \\\\ \n') for word, frequancy in dictionary.items()] 
        start=0
        end=rows_num
        new_words = []
        for i in range(n):
            new_words = new_words+ [begin_table+'\n'] +words[start:end] +[end_table+" \n"]
            start=end
            end+=rows_num
        remain_words = len(dictionary) - rows_num*n
        if remain_words > 0:
            new_words +=  [begin_table+" \n"]+ words[-1*remain_words:]+[end_table+" \n"]
        for word in new_words:
            file.write(word)
        file.write(tail_code)
        file.close()
        return True
    except:
        return False



def shape(system):
    """
    	 shape declare a new system for alphabets ,user pass the alphabets "in a list of list"
    	 that want to count it as on shape "inner list" and returns a dictionary has the same value
         for each set of alphabets and diffrent values for the rest of alphabets

        Args:

            param1 ([[char]]): a list of list of alphabets , each inner list have
                              alphabets that with be count  as one shape .
        Returns:
            dictionary: with all alphabets, where each char "key"  have a value
            value will be equals for alphabets that will be count as oe shape
    """

    listOfAlphabet = sorted(list(alphabet))
    alphabetMap = dict()
    indx = 0

    newAlphabet = sorted(list(set(chain(*system))))
    theRestOfAlphabets = sorted(list(set(listOfAlphabet) - set(newAlphabet)))

    for setOfNewAlphabet in system:
        for char in setOfNewAlphabet:
            alphabetMap.update({char: indx})
        indx = indx + 1

    for char in theRestOfAlphabets:
        alphabetMap.update({char: indx})
        indx = indx + 1
    alphabetMap.update({" ": 70})

    return alphabetMap


def convert_text_to_numbers(text,alphabetMap):
    """
         convert_text_to_numbers get a text (surah or ayah) and convert it to list of numbers
         depends on alphabetMap dictionary , user pass the text "list or list of list" that want to count      
         and dictionary that has each chat with it's number that will convert to,and returns a list of numbers

         What it does:
         it convert each letter to a number "corresponding to dictionary given as argument"

         Args:
             param1 ([str] ): a list of strings , each inner list is ayah .
             param2(dict) : a dictionary has each alphabet with it's corresponding number
         Returns:
             List: list of numbers, where each char in the text converted to number

    """
    i=0
    textToNumber=[]
    for char in text:
        textToNumber.insert(i, alphabetMap[char])
        i = i + 1
    return textToNumber


def count_shape(text, system=None):
    """
        count_shape parses the text  and returns a N*P matrix (ndarray),

        the number of rows equals to the number of verses ,
        and the number of columns equals to the number of shapes.

        What it does:
            count the occuerence of each shape in text, depends on the your system ,
            If you don't pass system, then it will count each char as one shape.

            If `A` is a ndarray,
            then A[i,j] is the number of occurrences of alphabet(s)[j] in the
            verse i.

        Args:
            param1 ([str] ): a list of strings , each inner list is ayah .
            param2([[char]]) : it's optional ,
                                -a list of list , each iner list has alphabets that will count as one shape
                                - If you don't pass your system, then it will count each char as one shape
        Returns:
            ndarray: with dimensions (N * P), where
            `N` is the number of verses in chapter and
            `P` the number of elements in system + the number of alphapets as on char [alphabets in system excluded]

    """
    listOfAlphabet = sorted(list(alphabet))
    #print(listOfAlphabet)
    if system == None:
        alphabetMap = dict()

        indx = 0
        for char in listOfAlphabet:
            alphabetMap.update({char: indx})
            indx = indx + 1
        alphabetMap.update({" ": 70})
        p=len(listOfAlphabet)#+1 #the last one for space char

    else:
        alphabetMap=shape(system)

        p=len(listOfAlphabet)-len(list(set(chain(
            *system))))+len(system)#+1 #the last one for space char
    n=len(text)
    A=numpy.zeros((n, p), dtype=numpy.int)#(m-len(list(set(
    # chain(*system)))))+len(system)
    i=0
    j=0
    charCount =[]
    for verse in text:
        verse=convert_text_to_numbers(verse, alphabetMap)
        for k in range(0,p,1) :                   #for key, value in
            # alphabetMap.items():
            charCount.insert(j, verse.count(k))
            j+=1
        A[i, :] =charCount
        i+=1
        charCount=[]
        j=0

    return A


def get_verse_count(surah):
    """
         get_verse_countget get surah as a paramter and return
         how many ayah in it.

         What it does:  count the number of verses in surah

         Args:
             param1 (str ): a strings

         Returns:
             int: the number of verses
    """
    return len(surah)
    

def count_token(text):
    """
         count_token get a text (surah or ayah) and count the
         number of tokens that it has.

         What it does: count the number of tokens in text

         Args:
             param1 (str or [str]): a string or list of strings

         Returns:
            int: the number of tokens
    """
    count=0
    if isinstance(text, list):
        for ayah in text:
            count=count+ayah.count(' ')+1
    else:
           count=text.count(' ')+1
           
    return count



def separate_token_with_dicrites(token):
    """
         gets a token with taskeel, and returns a list contains the token characters with their tashkeel.
        
         Args:
             param1 (str): strig that will separate it. 
        
         Returns:
             [str]: a list contains the token characters with their tashkeel.
    
    """
    token_without_tatweel = strip_tatweel(token)
    print(token_without_tatweel)
    hroof_with_tashkeel = []
    for index,i in enumerate(token):
        if((token[index] in (alphabet or alefat or hamzat)or token[index] is ' ' )):
            k = index
            harf_with_taskeel =token[index]
            while((k+1) != len(token) and (token[k+1] in (tashkeel or harakat or shortharakat or tanwin ))):
                harf_with_taskeel =harf_with_taskeel+""+token[k+1]
                k = k + 1
            index = k
            hroof_with_tashkeel.append(harf_with_taskeel)
    return hroof_with_tashkeel



def frequency_of_character(characters,verse=None,chapterNum=0,verseNum=0 , with_tashkeel=False):
    """
        this function count number of characters occurrence, 
        for specific verse or with chapter or even all Quran , 
        note if you don't pass verse and chapterNum he will get all Quran
    
        Args:
             verse (str): this verse that you need to 
                     count it and default is None.
             chapterNum (int) : chapter number is a number of 'sura' 
                          that will count it , and default is 0
             verseNum (int) : verse number in sura
             chracters (list) : list of characters that you want to count them
             with_tashkeel (boo) : to check if you want to search with tashkeel
    
        Returns:
             {dic} : a dictionary and keys is a characters 
                     and value is count of every chracter.
    """
    #dectionary that have frequency 
    frequency = dict()
    #check if count specific verse
    if verse!=None:
        if not with_tashkeel:
            verse = strip_tashkeel(verse)
        #count frequency of chars
        frequency = hellper_frequency_of_chars_in_verse(verse,characters)
        
    #check if count specific chapter
    elif chapterNum!=0:
        #check if count specific verse in this chapter
        if verseNum!=0:
            #check if verseNum out of range
            if(verseNum<0):
                return dict()
            verse = get_sura(chapterNum,with_tashkeel=with_tashkeel)[verseNum-1]
            #count frequency of chars
            frequency = hellper_frequency_of_chars_in_verse(verse,characters)
        else:
            #count on all chapter
            chapter = " ".join(get_sura(chapterNum,with_tashkeel=with_tashkeel))
            #count frequency of chars
            frequency = hellper_frequency_of_chars_in_verse(chapter,characters)
    else:
        if verseNum!=0:
            #count for specific verse in all Quran 
            Quran = ""
            for i in range(swar_num):
                 Quran = Quran +" "+get_verse(i+1,verseNum,with_tashkeel=with_tashkeel)+" "
            #count frequency of chars
            frequency = hellper_frequency_of_chars_in_verse(Quran,characters)
        else:
            #count for all Quran 
            Quran = ""
            for i in range(swar_num):
                 Quran = Quran +" "+ " ".join(get_sura(i+1,with_tashkeel=with_tashkeel))+" "
            #count frequency of chars
            frequency = hellper_frequency_of_chars_in_verse(Quran,characters)
    return frequency


    

def get_token(tokenNum,verseNum,chapterNum,with_tashkeel=False):
    """
        get token from specific verse form specific chapter
        
        Args:
            tokenNum (int) : position of token
            verseNum (int): number of verse 
            chapterNum (int): number of chapter 
            with_tashkeel (int) : to check if search with taskeel or not

        Returns:
            str :  return verse
    """
    if(chapterNum > swar_num or verseNum<=0 or tokenNum<=0):
        return ""
    try:
        tokens = get_sura(chapterNum,with_tashkeel)[verseNum-1].split()
        if tokenNum > len(tokens):
            return ""
        else:
            return tokens[tokenNum-1]
    except:
        return ""








def search_sequence(sequancesList,verse=None,chapterNum=0,verseNum=0,mode=3):
    """
        take list of sequances and return matched sequance,
        it search in verse ot chapter or All Quran , 
        it return for every match :
            1- matched sequance 
            2- chapter number of occurrence
            3- token number if word and 0 if sentence
        
        Note :
             *if found verse != None it will use it en search .
             
             *if no verse and found chapterNum and verseNum it will
              use this verse and use it to search.
              
             *if no verse and no verseNum and found chapterNum it will
              search in chapter.
             
             *if no verse and no chapterNum and no verseNum it will
              search in All Quran.
        
        it has many modes:
            1- search with decorated sequance (with tashkeel),
               and return matched sequance with decorates (with tashkil).
               
            2- search without decorated sequance (without tashkeel),
               and return matched sequance without decorates (without tashkil).
               
            3- search without decorated sequance (without tashkeel),
               and return matched sequance with decorates (with tashkil).
            
        
        Args:
            chapterNum (int): number of chapter where function search
            verseNum (int): number of verse wher function search
            sequancesList (list): a list of sequances that you want 
                                  to match them
            mode (int): this mode that you need to use and default mode 3

        Returns:
            dict() :  key is sequances and value is a list of matched_sequance 
                      and their positions
    """    
    final_dict = dict()
    #loop on all sequances
    for sequance in sequancesList:
        #check mode 1 (taskeel to tashkeel)
        if mode==1:
             final_dict[sequance] = hellper_pre_search_sequance(
                                    sequance=sequance,
                                    verse=verse,
                                    chapterNum=chapterNum,
                                    verseNum=verseNum,
                                    with_tashkeel=True)
        # chaeck mode 2 (without taskeel to without tashkeel)
        elif mode==2:
            final_dict[sequance] = hellper_pre_search_sequance(
                                   sequance=sequance,
                                   verse=verse,
                                   chapterNum=chapterNum,
                                   verseNum=verseNum,
                                   with_tashkeel=False)
        # chaeck mode 3 (without taskeel to with tashkeel)
        elif mode==3:
            sequance = strip_tashkeel(sequance)
            final_dict[sequance] = hellper_pre_search_sequance(
                                   sequance=sequance,
                                   verse=verse,
                                   chapterNum=chapterNum,
                                   verseNum=verseNum,
                                   with_tashkeel=True,
                                   mode3=True)
    return final_dict        




def search_string_with_tashkeel(string, key):
    """
      Args:
         string: sentence to search by key
         key: taskeel pattern

      Return: (True, text that have that tashkeel pattern)
              (Flase, '')
 
      Assumption:
         Searches tashkeel that is exciplitly included in string.

    """
    # tashkeel pattern
    string_tashkeel_only = get_string_taskeel(string)

    # searching taskeel pattern
    results = []
    for m in re.finditer(key, string_tashkeel_only):

        spacesBeforeStart = \
            count_spaces_before_index(string_tashkeel_only, m.start())
        spacesBeforeEnd = \
            count_spaces_before_index(string_tashkeel_only, m.start())

        begin =  m.start() * 2 - spacesBeforeStart
        end   = m.end() * 2 - spacesBeforeEnd
        one_result = (m.start(), m.end())
        results.append(one_result)

    if results == []:
        return False, []
    else:
        return True, results


def buckwalter_transliteration(string, reverse=False):
   """
     buckwalter_translator get an a Unicode
     tring and transliterate it to Buckwalter encoding or vise verse

     What it does:
         transliterate a Unicode string to buckwalter and vise verse
     Args:
         param1 (str): a string
         param2 (bool): Boolean , it's an optional
                        if it quals to False "False is the defult" ,
                        it transliterate from a Unicode string to buckwalter encoding
                        and vise verse if it equals to True
     Returns:
         str : a string, a Unicode or buckwalter 
    """
   for key, value in buck2uni.items():
       if not reverse:
            string = string.replace(value, key)
       else:
            string = string.replace(key, value)
   return string


def get_tashkeel_binary(ayah):
  '''
     get_tashkeel_pattern is function takes the str or list(ayah or token) and converts to zero and ones

     What it does:
           take token whether ayah or sub ayah and maps it to zero for sukoon and char without diarictics
           and one for char with harakat and tanwin
     Args:
           param1 (str): a string or list

     Returns:
           str : zero and ones for each token
  '''

  marksDictionary = {'ْ': 0, '': 0, 'ُ': 1, 'َ': 1, 'ِ': 1, 'ّ': 1, 'ٌ': 1, 'ً': 1, 'ٍ': 1}
  charWithOutTashkeelOrSukun = ''
  tashkeelPatternList = []  # list of zeros and ones
  marksList = []

  # convert the List o to string without spaces
  ayahModified = ''.join(ayah.strip())
  tashkeelPatternStringWithSpace = ''

  # check is there a tatweel in ayah or not
  if(tatweel in ayahModified):
     ayahModified = strip_tatweel(ayahModified)

  # check whether exist alef_mad in ayah if exist unpack the alef mad
  if (alef_mad in ayahModified):
      ayahModified = unpack_alef_mad(ayahModified)


  # separate tashkeel from the ayah
  ayahOrAyatWithoutTashkeel, marks = separate(ayahModified)

  for mark in marks:
  #the pyarabic returns the char of marks without tashkeel with 'ـ' so if check about this mark if not exist
  #append in list harakat and zero or ones in tashkeel pattern list if yes append the marks and patterns
    if (mark != 'ـ'):
      marksList.append(mark)
      tashkeelPatternList.append(marksDictionary[mark])
    else:
      marksList.append(charWithOutTashkeelOrSukun)
      tashkeelPatternList.append(marksDictionary[charWithOutTashkeelOrSukun])

  # convert list of Tashkeel pattern to String for each token in ayah separate with another token with spce
  for posOfCharInAyah in range(0, len(ayahOrAyatWithoutTashkeel)):
    if ayahOrAyatWithoutTashkeel[posOfCharInAyah] == ' ' and tashkeelPatternList[posOfCharInAyah] == 0:
         tashkeelPatternStringWithSpace += ' '
    else:
         tashkeelPatternStringWithSpace += str(tashkeelPatternList[posOfCharInAyah])
  return tashkeelPatternStringWithSpace, marksList


def unpack_alef_mad(ayahWithAlefMad: str):
  '''
     unpack_alef_mad is function takes the str or list(ayah or ayat) 
     and search about alef mad and unpacks it

     What it does:
         take the Alef mad and converts the alef  mad to alef fataha and alef sukun
     Args:
         param1 (str): a string or list

     Returns:
         str : ayah or token with Unpacked mad
  '''
  ayahWithUnpackAlefMad = ''
  for charOfAyah in ayahWithAlefMad:
     if charOfAyah != 'آ':
         ayahWithUnpackAlefMad += charOfAyah
     else:
         ayahWithUnpackAlefMad += 'أَ'
         ayahWithUnpackAlefMad += 'أْ'
  return ayahWithUnpackAlefMad




def check_all_alphabet(system):
    '''
     check_alphabet get a list of alphabets or system(list of lists of alphabets)
     and return the rest of arabic alphabets [alphabets in system excluded]
     -in case sytem equals all arabic alphabets, it will return empty list.

     What it does:
         return the rest of arabic alphabets that not included in system.

     Args:
         param1 ([char] ): a list or list of lists of characters.

     Returns:
         list: include all other arabic alphabet.
    '''

    listOfAlphabet = list(alphabet)
    if isinstance(system, list):
        system=list(chain(*system))
    theRestOfAlphabets = sorted(list(set(listOfAlphabet) - set(system)))
    return theRestOfAlphabets


def check_system(system, indx=None):
    '''
     check_sytem get a system (list of lists ) and index (it's
     optional) and return full sorted system or a specific index in it.

     -sortion will follow this approach : system in the first with the same
     order , then all remain alphabets sorted alphabetically .

     What it does:
         build a full sorted system and return it or a specific index in it.

     Args:
         param1 ([[char]] ):  list of lists of characters.
         int: it's optinal , it will return this index in full sorted system.

     Returns:
         list: full sorted system or a spesefic index.
    '''
    if indx==None:
        return (system + [[char] for char in check_all_alphabet(system)])
    else:
        return (system + [[char] for char in check_all_alphabet(system)])[indx]



def search_with_pattern(pattern,sentence=None,verseNum=None,chapterNum=None,threshold=1):
    '''
       this function use to search in 0's,1's pattern and
       return matched words from sentence pattern 
       dependent on the ratio to adopt threshold.
       
       Args:
           pattern (str): 0's,1's pattern that you need to search.
           sentence (str): Arabic string with tashkeel where 
                           function will search.
           verseNum (int): number of specific verse where
                           will search.
           chapterNum (int): number of specific chapter 
                             where will search.
           threshold (float): threshold of similarity , if 1 it will
                              get the similar exactly, and if not ,it will 
                              get dependant on threshold number.
        
       Cases: 
           1- if pass sentece only or with another args 
              it will search in sentece only.
           2- if not passed sentence and passed verseNum and chapterNum,
              it will search in this verseNum that exist in chapterNum only.
           3- if not passed sentence,verseNum and passed chapterNum only,
              it will search in this specific chapter only
    
       Return:
           [list] : it will return list that have matched word, or 
                    matched senteces and return empty list if not found.
    
       Note : it's takes time dependent on your threshold and size of chapter,
              so it's not support to search on All-Quran becouse 
              it take very long time more than 11 min.
    '''
    if threshold > 1 or threshold < 0:
        sys.exit('Threshold should be 0 <= Threshold <= 1')
    pattern = pattern.replace(' ','')
    if len(pattern)<=0:
        sys.exit('pattern don\'t passed')
    
    #check if sentece exist
    if sentence != None:
        #convert sentence to 0/1
        sentence_pattern,taskieel = get_tashkeel_binary(sentence)
        return hellper_search_with_pattern(pattern=pattern,
                                           sentence_pattern=sentence_pattern,
                                           sentence=sentence,
                                           ratio=threshold)
    else:
        #check if search in specific chapter
        if chapterNum != None:
            #check if search in specific verese
            if verseNum != None:
                sentence = get_verse(chapterNum=chapterNum,
                                     verseNum=verseNum,
                                     with_tashkeel=True)
            #search in all chapter
            else:
                sentence = " ".join(get_sura(chapterNum,True))
        #search in all Quran
        else:
            sys.exit('please send sentece or verseNum and chapterNum to search.')
        
        #convert sentence to 0/1
        sentence_pattern,taskieel = get_tashkeel_binary(sentence)
        sentence_pattern_without_spaces = sentence_pattern.replace(" ","")
        #check if no pattern exist
        if pattern not in sentence_pattern_without_spaces:
            return []
        else:
            return hellper_search_with_pattern(pattern=pattern,
                                               sentence_pattern=sentence_pattern,
                                               sentence=sentence,
                                               ratio=threshold)
