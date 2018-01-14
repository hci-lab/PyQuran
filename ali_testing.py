#import sys
from xml.etree import ElementTree
from pyarabic import araby
from arabic import *
from itertools import chain
from collections import Counter, defaultdict

xml_file_name = 'QuranCorpus/quran-simple-clean.xml'
quran_tree_ = ElementTree.parse(xml_file_name)

"""Test Cases"""
class Erros:
    erros_dict={
        'INVALID_CHAPTER_NUMBER':"Chapter numbers should be between 1 and 114 inclusive.",
        'INVALID_VERSE_NUMBER':"The verse number is out of range.",
        'INVALID_SURA_NUMBER':"The sura number is out of range.",
        'INVALID_SURA_NAME':"The sura name is not valid.",
        'INVALID_VERSE_NUMBER':"The verse number is out of range.",
        'INVALID_COLUMN_NAME':"The specific column could not be found.",
        }

    def getErrorCount(self):
        """Gets the total number of error messages.
        Args:
        Returns:
          	int: a positive value indicating the number of erros.
        """
        return len(Erros.erros_dict)

#==============================================================
def separate_token_with_dicrites(token):
    """gets a token(string) with taskeel, and returns a list of strings,
    each string in the list represents each character in the token with its own tashkeel.
    Args:
        token (str): string represents a word or aya or sura
    Returns:
        [str]: a list contains the token characters with their tashkeel.
    """
    token_without_tatweel = araby.strip_tatweel(token)
    print(token_without_tatweel)
    hroof_with_tashkeel = []
    for index,i in enumerate(token):
        if((token[index] in (alphabet or alefat or hamzat) )):
            k = index
            harf_with_taskeel =token[index]
            while((k+1) != len(token) and (token[k+1] in (tashkeel or harakat or shortharakat or tanwin ))):
                harf_with_taskeel =harf_with_taskeel+""+token[k+1]
                k = k + 1
            index = k
            hroof_with_tashkeel.append(harf_with_taskeel)
    return hroof_with_tashkeel

def get_sura_number(suraName):
    """It takes sura name as string, and returns the an ordered number(integer) of the sura
    Args:
        suraName (str) : string represents the sura name.
    Returns:
        int: the sura number which name is suraName.
    Usage Note:
        Do not forget that the index of the returned list starts at zero.
        So if the order Sura number is x, then it's at (x-1) in the list.
    """
    suras_list = quran_tree_.findall('sura')
    suraNumber = None
    for index in range (1,115):
        if suras_list[index-1].attrib['name'] == suraName:
            suraNumber = index
    return suraNumber

def get_sura_name(suraNumber=None):
    """It takes and ordered number of a sura, and returns the sura name as string or
	returns a list contains all suras' names if you don't pass any parameter (the entire Quran is targeted).
    Args:
        suraNumber (int): it's optional
    Returns:
        str: the sura name which number is suraNumber
        OR
        [srt]: list of all suras' names (if the suraNumber parameter is None)
    Usage Note:
        Do not forget that the index of the returned list starts at zero.
        So if the order Sura number is x, then it's at (x-1) in the list.
    """
    # get all suras
    suras_list = quran_tree_.findall('sura')
    if suraNumber is None :
        suraName = [(suras_list[i].attrib['name']) for i in range(0,114)]
    else:
        # get suraName
        suraName = suras_list[suraNumber-1].attrib['name']
    # return suraName
    return  suraName


def main():
    """
    Testing Function : separate_token_with_dicrites(token)
    Hints:
        1) if the received parameter is not valid, the returned list will be empty.
        2) if the received parameter contains Arabic alphabets and another alphabets,
        the returned list will have only the Arabic alphabets.
    """
    #token = "dasasslقل ما أسألكم عليه من أجر"
    #hroof_with_tashkeel_list =  separate_token_with_dicrites(token)
    #print(hroof_with_tashkeel_list)

    """
    Testing Function : def get_sura_number(suraName):
    Hints: if the received parameter(suraName) is not valid, the returned value(suraNumber) will be None. 
    """
    """
	suraNumber = get_sura_number("dsf")
    if suraNumber is not None :
        print(suraNumber)
    else:
        print(Errors.erros_dict["INVALID_SURA_NAME"])
    """

	"""
    Testing Function : def get_sura_name(suraNumber):
    Hints: if the received parameter(suraName) is not valid, the returned value(suraNumber) will be None. 
    """
    """
	suraName = get_sura_name(160)
    if suraName is not None :
        print(suraName)
    else:
        print(Errors.erros_dict["INVALID_SURA_NUMBER"])
    """

	

if __name__ == '__main__':
   main()
