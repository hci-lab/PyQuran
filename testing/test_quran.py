"""unittest module for quran.py
"""
import unittest

# Adding another searching path
from sys import path
path.append('../tools/')
path.append('../core/')

from quran import *

class Testing_quran(unittest.TestCase):

    def test_get_sura(self):
        self.assertEqual(len(get_sura(1)), 7)
        self.assertEqual(len(get_sura(2)), 286)
        self.assertEqual(len(get_sura(49)), 18)
        self.assertEqual(len(get_sura(76)), 31)

        self.assertEqual(len(get_sura(1, True)), 7)
        self.assertEqual(len(get_sura(2, True)), 286)
        self.assertEqual(len(get_sura(49, True)), 18)
        self.assertEqual(len(get_sura(76, True)), 31)

    def test_fetch_aya(self):
        aya = 'يختص برحمته من يشاء والله ذو الفضل العظيم'
        self.assertEqual(fetch_aya(3, 74), aya)

        aya = 'الم'
        self.assertEqual(fetch_aya(29, 1), aya)


        self.assertEqual(len(fetch_aya(28, 88)), 82)

        aya = 'الر تلك ءايت الكتب الحكيم'
        self.assertEqual(fetch_aya(10, 1), aya)

        aya = 'واتبع ما يوحى إليك واصبر حتى يحكم الله وهو خير الحكمين'
        self.assertEqual(fetch_aya(10, 109), aya)

        self.assertEqual(len(fetch_aya(6, 165)), 105)

        aya = 'الحمد لله رب العلمين'
        self.assertEqual(fetch_aya(1, 2), aya)




if __name__ == '__main__':
    unittest.main()
