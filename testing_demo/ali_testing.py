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

x = 'الحمد لله رب  العالمين'
print(separate_token_with_dicrites(x))



