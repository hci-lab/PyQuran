"""unittest module for searchHelper.py
"""
import unittest
import os
from sys import path

# The current path of the current module.
path_current_module = os.path.dirname(os.path.abspath(__file__))
tools_modules = '../tools/'
core_modules = '../core/'

tools_path = os.path.join(path_current_module, tools_modules)
core_path  = os.path.join(path_current_module, core_modules)

path.append(tools_path)
path.append(core_path)

from quran import get_verse
from searchHelper import *
from pyquran import get_tashkeel_binary

class Testing_searchHelper(unittest.TestCase):

    def test_count_spaces_before_index(self):
        self.assertEqual(count_spaces_before_index('', 0), 0)
        self.assertEqual(count_spaces_before_index('01 34 6 8', 8), 3)
        self.assertEqual(count_spaces_before_index(' ', 1), 1)


    def test_get_string_taskeel(self):
        x = 'ﺐِﺴﻣ ﺎﻠﻠﻫِ ﺎﻟﺮّﺤﻤﻧ ﺎﻟﺮَﺤﻴﻣ'
        self.assertEqual(len(get_string_taskeel(x)), 7)


    def test_hellper_get_sequance_positions(self):
       self.assertEqual(hellper_get_sequance_positions("abcd abdsacd abdscd abcd abdsacd abdscd",'abcd abdsacd'),[1,4])
       self.assertEqual(hellper_get_sequance_positions("بسم الله الرحمن الرحيم",'بسم الله'),[1])
       self.assertEqual(hellper_get_sequance_positions('بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ','الرَّحْمَنِ'),[2])

    def test_hellper_search_function(self):
        ver_wo_taskeel = get_verse(1,1,with_tashkeel=False)
        ver_w_taskeel = get_verse(1,1,with_tashkeel=True)
        self.assertEqual(hellper_search_function(verse=ver_w_taskeel,
                                                 sequance="بِسْمِ",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=True),
                                                 [])
        
        self.assertEqual(hellper_search_function(verse=ver_w_taskeel,
                                                 sequance="بِسْمِ",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=False),
                                                 [('بِسْمِ', 1)])

        self.assertEqual(hellper_search_function(verse=ver_w_taskeel,
                                                 sequance="بسم",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=False),
                                                 [])
        
        self.assertEqual(hellper_search_function(verse=ver_w_taskeel,
                                                 sequance="بسم",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=True),
                                                 [('بِسْمِ', 1)])

        self.assertEqual(hellper_search_function(verse=ver_wo_taskeel,
                                                 sequance="بِسْمِ",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=False),
                                                 [])
        
        self.assertEqual(hellper_search_function(verse=ver_wo_taskeel,
                                                 sequance="بِسْمِ",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=True),
                                                 [])

        self.assertEqual(hellper_search_function(verse=ver_wo_taskeel,
                                                 sequance="بسم",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=False),
                                                 [('بسم', 1)]
)
        self.assertEqual(hellper_search_function(verse=ver_wo_taskeel,
                                                 sequance="بسم",
                                                 verseNum=0,
                                                 chapterNum=0,
                                                 mode3=True),
                                                 [('بسم', 1)])

        self.assertEqual(hellper_search_function(verse=ver_w_taskeel,
                                                 sequance="بسم",
                                                 verseNum=1,
                                                 chapterNum=1,
                                                 mode3=True),
                                                 [('بِسْمِ', 1, 1, 1)])

        
    def test_hellper_frequency_of_chars_in_verse(self):
        ver_w_taskeel = get_verse(1,1,with_tashkeel=True)
        self.assertEqual(hellper_frequency_of_chars_in_verse(ver_w_taskeel,['ر',"رّ","ة",'َ']),{'ة': 0, 'ر': 2, 'رّ': 2, 'َ': 4})


    def test_hamming_distance(self):
        self.assertEqual(hamming_distance("abcd",'absc'),2)
        self.assertEqual(hamming_distance("مرحبا كيف حالك",'مورحبا كيف حالك'),13)

    def test_get_word_num(self):
        self.assertEqual(get_word_num(15,"hellow how are you"),3)
        self.assertEqual(get_word_num(7,"hellow how are you"),1)

    def  test_hellper_search_with_pattern(self):
        aya = get_verse(1,1,with_tashkeel=True)
        pattern = get_tashkeel_binary(aya)
        result = hellper_search_with_pattern('101',pattern[0],aya)
        self.assertEqual(result,['بِسْمِ', 'الرَّحْمَنِ', 'الرَّحِيمِ'])

        result = hellper_search_with_pattern('101',pattern[0],aya,ratio=0.5)
        self.assertEqual(result,['بِسْمِ',
                                 'بِسْمِ اللَّهِ',
                                 'اللَّهِ',
                                 'اللَّهِ الرَّحْمَنِ',
                                 'الرَّحْمَنِ',
                                 'الرَّحْمَنِ الرَّحِيمِ',
                                 'الرَّحِيمِ'])

        result = hellper_search_with_pattern('1011',pattern[0],aya)
        self.assertEqual(result,['الرَّحْمَنِ'])

        result = hellper_search_with_pattern('10111',pattern[0],aya)
        self.assertEqual(result,[])

        
if __name__ == '__main__':
    unittest.main()
