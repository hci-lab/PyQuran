"""unittest module for pyquran.py
"""
import unittest

# Adding another searching path
from sys import path
path.append('../tools/')
path.append('../core/')

from arabic import *
from pyquran import *

class Testing_pyquran(unittest.TestCase):

    def test_search_string_with_tashkeel(self):
        sentence = 'ﺺِﻓْ ﺫَﺍْ ﺚَﻧَﺍْ ﻚَﻣْ ﺝَﺍْﺩَ ﺶَﺨْﺻٌ'
        x = search_string_with_tashkeel(sentence, fatha + sukun)
        y = (True, [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)])
        self.assertEqual(x, y)


    def test_get_tashkeel_binary(self):
        binaryPatternY = '0010101'
        subAyah = 'الْأَحْيَاءُ'
        binaryPatternX =  get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
        binaryPatternY = '1010 101011 001011'
        subAyah = 'إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ'
        binaryPatternX =  get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
        binaryPatternY = '101 00011 0001011 0001101'
        subAyah = 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ'
        binaryPatternX =  get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
        binaryPatternY = '11011 1011 10 10 00011101 110 10 00101 00111 0010101 001101 001101'
        subAyah = ' يُسَبِّحُ لِلَّهِ مَا فِي السَّمَوَاتِ وَمَا فِي الْأَرْضِ الْمَلِكِ الْقُدُّوسِ الْعَزِيزِ الْحَكِيمِ'
        binaryPatternX =  get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
if __name__ == '__main__':
    unittest.main()
