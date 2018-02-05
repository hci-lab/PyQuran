#!/usr/local/bin/python3
"""Taha's testing module
    * _test suffix is added to all functions here.

"""

from arabic import *
import pyquran
import re
import searchHelper

'''
print(pyquran.get_sura(113))
print(pyquran.get_sura(113, True))
'''

string = 'a^b*c&d a^b*c&d'

def count_spaces_before_index_test(string, index):
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
'''
print(count_spaces_before_index('01 34 6 8', 100))
'''


def get_string_taskeel_test(string):
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
'''
x = 'بِسم اللهِ الرّحمن الرَحيم'
print(get_string_taskeel(x))
'''



def search_string_with_tashkeel_test(string, key):
    """
    string: sentence to search by key
    key: taskeel pattern

    return: (True, text that have that tashkeel pattern)
            (Flase, '')

    Assumption:
        Searches tashkeel that is exciplitly included in string.
    ToDo:
        1 get tashkeel pattern with spaces
        
    """
    # tashkeel pattern
    string_tashkeel_only = searchHelper.get_string_taskeel(string)
    print(string_tashkeel_only)
    print(string_tashkeel_only)
    print(string_tashkeel_only)

    # searching taskeel pattern
    results = []
    for m in re.finditer(key, string_tashkeel_only):

        spacesBeforeStart = searchHelper.\
            count_spaces_before_index(string_tashkeel_only, m.start())
        spacesBeforeEnd = searchHelper.\
            count_spaces_before_index(string_tashkeel_only, m.start())

        begin =  m.start() * 2 - spacesBeforeStart 
        end   = m.end() * 2 - spacesBeforeEnd 
        one_result = (m.start(), m.end())
        results.append(one_result)

    if results == []:
        return False, []
    else:
        return True, results
        
sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
results = search_string_with_tashkeel_test(sentence, fatha + sukun)  
print(results)


def tasheel_to_names(pattern):
    pass

'''
x = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
x = get_string_taskeel(x)
print(count_spaces_before_index(x, 18))
'''
