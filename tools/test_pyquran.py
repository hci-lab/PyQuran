"""unittest module for pyquran.py
"""
import unittest
from arabic import *
from pyquran import *

class Testing_pyquran(unittest.TestCase):

    def test_search_string_with_tashkeel(self):
        sentence = 'ﺺِﻓْ ﺫَﺍْ ﺚَﻧَﺍْ ﻚَﻣْ ﺝَﺍْﺩَ ﺶَﺨْﺻٌ'
        x = search_string_with_tashkeel(sentence, fatha + sukun)
        y = (True, [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)])
        self.assertEqual(x, y)



if __name__ == '__main__':
    unittest.main()
