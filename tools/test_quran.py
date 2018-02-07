"""unittest module for quran.py
"""
import unittest


import quran

class Testing_quran(unittest.TestCase):

    def test_get_sura(self):
        self.assertEqual(len(quran.get_sura(1)), 7)
        self.assertEqual(len(quran.get_sura(2)), 286)
        self.assertEqual(len(quran.get_sura(49)), 18)
        self.assertEqual(len(quran.get_sura(76)), 31)

        self.assertEqual(len(quran.get_sura(1, True)), 7)
        self.assertEqual(len(quran.get_sura(2, True)), 286)
        self.assertEqual(len(quran.get_sura(49, True)), 18)
        self.assertEqual(len(quran.get_sura(76, True)), 31)


if __name__ == '__main__':
    unittest.main()
