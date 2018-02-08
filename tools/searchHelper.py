"""searchHelper: contains helper functions for searching.
"""

from arabic import *
import re
from pyarabic.araby import strip_tashkeel, strip_tatweel
import quran


def count_spaces_before_index(string, index):
    """counts spaces before a char in string.

    Args: 
        param1 (str): string
        param2 (int): char index inside string
    Returns:
         int: number of spaces before string[index]

    """
    count = 0
    for i in range(index):
        if string[i] == ' ':
            count += 1

    return count


def get_string_taskeel(string):
    """get list of tashkeel without letters

    Args: 
        param1 (str): string
        param2 (int): char index inside string
    Returns:
        list[char]: a list of diacritics found in `straing`

    """
    x = ''
    for char in string:
        if char in tashkeel or char == ' ':
            x += char
    return x



def hellper_get_sequance_positions(verse,sequance):
    '''
        this function takes verse and sequence and returns 
        the position of match word,
        and if sequence exists in verse more that one, it 
        return list of first matched the word. 
    '''
    verse = strip_tashkeel(verse)
    sequance = strip_tashkeel(sequance)
    sequance = sequance.split()
    verse = verse.split()
    positions = []
    for n,v in enumerate(verse):
        if v not in sequance:
            continue
        for en,se in enumerate(sequance):
            if se != verse[n]:
                break
            if en == len(sequance)-1:
                positions.append(n)
            n+=1
    return positions



def hellper_search_function(verse,sequance,verseNum,chapterNum,mode3):
    
    #split verse  to tokens
    tokens = re.split(r' ',verse)
    
    if mode3:
        verse = strip_tashkeel(verse)
    tashkeel_ = "|".join([fatha,fathatan,damma,dammatan
                          ,kasra,kasratan,shadda,sukun])
    pattern = r"((\w|["+tashkeel_+"]*)*"+str(sequance)+"(\w|["+tashkeel_+"]*)*)"
    
    #get match_sequance
    matches = re.findall(pattern,verse)
    matches = [j.strip() for i in matches for j in i if j !='']
    #check if found or not
    if len(matches)!=0:
        try:
            new_tokens = verse.split()
            positions = dict()
            #get position of occuerance
            lst = []
            if len(sequance.split())>1:
                for tok in matches:
                    positions[tok] = (0,hellper_get_sequance_positions(
                                      verse,tok))
            else:
                for tok in matches:
                    if verse.count(tok) > 1:
                        ls = [i for i,x in enumerate(new_tokens) if x == tok]
                        positions[tok] = (0,ls)
                    else:
                        positions[tok] = (0,[new_tokens.index(tok)])
                        
            if chapterNum!=0 and len(sequance.split())==1:
                for token in matches:
                    loc,ls = positions[token]
                    index = int(ls[loc])
                    positions[token] = (loc+1,ls)
                    #check if exist the same token many time
                    lst.append((tokens[index],
                                index+1,
                                verseNum,
                                chapterNum))
                #if matched sequance token 
                return lst   
        except:
            pass
            
        if len(sequance.split())==1:
                #if matched sequance token
                for token in matches:
                    loc,ls = positions[token]
                    index = int(ls[loc])
                    positions[token] = (loc+1,ls)
                    #check if exist the same token many time
                    lst.append((tokens[index],
                                    index+1))
                #if matched sequance token 
                return lst
        else:
            #check if mode3 False
            if not mode3:
                if chapterNum!=0:
                    #if match sequance sentence
                    return [(token,0,verseNum,chapterNum) for token in matches]
                else:
                    #if match sequance sentence
                    return [(token,0) for token in matches]
            else:
                lst = []                
                #if match sequance sentence
                for token in matches:
                    new_token = []
                    loc,ls = positions[token]
                    index = int(ls[loc])
                    positions[token] = (loc+1,ls)
                    new_token = " ".join([str(tokens[index-
                                          len(sequance.split())+i*1+1]) 
                                          for i in range(len(token.split()))])
                    if chapterNum!=0:
                        lst.append((new_token,0,verseNum,chapterNum))
                    else:
                        lst.append((new_token,0))
                return lst 
    return []






def hellper_pre_search_sequance(sequance,verse=None,chapterNum=0,
                                verseNum=0,with_tashkeel=False,mode3=False):
    """
        search about sequance in verse or chapter or Quran 
        and return matched seqance and his position if sequance
        was token or sub-token ,and 0 if sequance was sentence.
        
        -cases:
          * if found verse as string it will search in verse that entered
          * if no chapterNum and no verseNum and  no verse it will search
            in All Quran.

          * if no verseNumber and no verse and found chapterNum it will
            search in chapter.

          * if found chapterNum and verseNum and no verse it will search
            in verse.
          
        Args:
            verse (str): it's a verse where function search
            sequances (str): a sequance that you want to match it
            chapterNum (int) : number of chapter 
            verseNum (int) : number of verse
            with_tashkeel (int) : to check if search with taskeel or not
            mode3 (bool) : if true it will us mode 3 to search
            
        Returns:
            list of tuble :  (matched_sequance ,
                              his_position ,
                              verse number ,
                              chapter number )

            Note: position will 0 if matched_sequance was part of sentence,
                  and will number if  matched_sequance was token or sub-token
    """
    if verseNum<0 or chapterNum <0 :
        return []
    #remove extra spaces
    sequance = re.sub(r" +"," ",sequance)
    sequance = sequance.strip()
    
    #strip tashkeel if with_tashkeel flage is false
    if not with_tashkeel:
        sequance = strip_tashkeel(sequance)
    
    #search in verse that enterd 
    if verse != None:
        return hellper_search_function(verse,sequance,verseNum,chapterNum,mode3)
    else:
        #chech if specific chapter  
        if chapterNum!=0:
            #check if specific verse
            if verseNum!=0:
                verse = quran.get_verse(chapterNum,verseNum,with_tashkeel)
                return hellper_search_function(verse,sequance,
                                               verseNum,
                                               chapterNum,
                                               mode3)
            else:
                #search in Chapter
                verses = quran.get_sura(chapterNum,with_tashkeel)
                return sum([hellper_search_function(v,sequance,
                                                    num+1,chapterNum,
                                                    mode3) 
                            for num,v in enumerate(verses)], [])
        else:
            #search in all Quran
            final_list = []
            for i in range(swar_num):
                verses = quran.get_sura(i+1,with_tashkeel)
                final_list += sum([hellper_search_function(v,sequance,
                                                           num+1,i+1,
                                                           mode3) 
                                   for num,v in enumerate(verses)], [])
            return final_list
    

def hellper_frequency_of_chars_in_verse(verse,charaters):
    """
        this function count number of characters occurrence in verse
            
        Args:
            verse (str): this verse that you need to 
                         count it and default is None.
            chracter (list) : list of characters that you want to count them 
    
        Returns:
            {dic} : a dictionary and keys is a characters and value is count of 
                    every chracter.
    """
    #dectionary that have frequency 
    frequency = dict()
    #count frequency of chars
    for char in charaters:
        frequency[char] = verse.count(char)
    return frequency
    
