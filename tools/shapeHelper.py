'''shapeHelper: contains helper functions shape.
'''


from arabic import *
from itertools import chain

def searcher(system, ch):
    for i in range(0, len(system), 1):
        if ch in system[i]:
            return i 


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


def check_repetation(system):
    diff = len(list(chain(*system)))-len(list(set(chain(*system))))
    if diff > 0:
        return True
    else:
        return False