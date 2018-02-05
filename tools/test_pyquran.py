"""unittest module for pyquran.py
"""
import unittest
import pyquran as pq

class Testing_pyquran(unittest.TestCase):


    def test_get_tashkeel_binary(self):
        self.assertEqual('0010101',pq.get_tashkeel_binary('الْأَحْيَاءُ')[0])
        self.assertEqual('1010 101011 001011',pq.get_tashkeel_binary('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')[0])
        self.assertEqual('101 00011 0001011 0001101',pq.get_tashkeel_binary('بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ')[0])
        self.assertEqual('11011 1011 10 10 00011101 110 10 00101 00111 0010101 001101 001101',pq.get_tashkeel_binary('يُسَبِّحُ لِلَّهِ مَا فِي السَّمَوَاتِ وَمَا فِي الْأَرْضِ الْمَلِكِ الْقُدُّوسِ الْعَزِيزِ الْحَكِيمِ')[0])
if __name__ == '__main__':
    unittest.main()
