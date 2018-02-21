"""unittest module for pyquran.py
"""
import unittest
import numpy as np
# Adding another searching path
from sys import path
path.append('../tools/')
path.append('../core/')

from arabic import *
import quran
import pyquran 


class Testing_pyquran(unittest.TestCase):

    def test_search_string_with_tashkeel(self):
        sentence = 'ﺺِﻓْ ﺫَﺍْ ﺚَﻧَﺍْ ﻚَﻣْ ﺝَﺍْﺩَ ﺶَﺨْﺻٌ'
        x = pyquran.search_string_with_tashkeel(sentence, fatha + sukun)
        y = (True, [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)])
        self.assertEqual(x, y)


    def test_get_tashkeel_binary(self):
        binaryPatternY = '0010101'
        subAyah = 'الْأَحْيَاءُ'
        binaryPatternX =  pyquran.get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
        binaryPatternY = '1010 101011 001011'
        subAyah = 'إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ'
        binaryPatternX =  pyquran.get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
        binaryPatternY = '101 00011 0001011 0001101'
        subAyah = 'بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ'
        binaryPatternX =  pyquran.get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)
        binaryPatternY = '11011 1011 10 10 00011101 110 10 00101 00111 0010101 001101 001101'
        subAyah = ' يُسَبِّحُ لِلَّهِ مَا فِي السَّمَوَاتِ وَمَا فِي الْأَرْضِ الْمَلِكِ الْقُدُّوسِ الْعَزِيزِ الْحَكِيمِ'
        binaryPatternX =  pyquran.get_tashkeel_binary(subAyah)[0]
        self.assertEqual(binaryPatternX,binaryPatternY)

        
    def test_get_frequency(self):    
        ver_w_taskeel = quran.get_verse(1,1,with_tashkeel=True)
        fre_dec = {'الرَّحِيمِ': 1, 'الرَّحْمَنِ': 1, 'اللَّهِ': 1, 'بِسْمِ': 1}
        self.assertEqual(pyquran.get_frequency(ver_w_taskeel),fre_dec)
        fre_dec={'أُنزِلَ': 2,
                 'إِلَيْكَ': 1,
                 'بِمَا': 1,
                 'قَبْلِكَ': 1,
                 'مِن': 1,
                 'هُمْ': 1,
                 'وَالَّذِينَ': 1,
                 'وَبِالْءَاخِرَةِ': 1,
                 'وَمَا': 1,
                 'يُؤْمِنُونَ': 1,
                 'يُوقِنُونَ': 1}

        freq = pyquran.get_frequency(quran.get_verse(2,4,with_tashkeel=True))
                             
        self.assertEqual(freq,fre_dec)


    def test_generate_frequency_dictionary(self):
        fre_dec = {'أحد': 2,
                   'الصمد': 1,
                   'الله': 2,
                   'قل': 1,
                   'كفوا': 1,
                   'لم': 1,
                   'له': 1,
                   'هو': 1,
                   'ولم': 2,
                   'يكن': 1,
                   'يلد': 1,
                   'يولد': 1}
        sura = pyquran.generate_frequency_dictionary(suraNumber=112)
        self.assertEqual(sura,fre_dec)


    def test_check_sura_with_frequency(self):
        freq = pyquran.generate_frequency_dictionary(suraNumber=2)
        self.assertEqual(pyquran.check_sura_with_frequency(2,freq),True)

        freq = pyquran.generate_frequency_dictionary(suraNumber=95)
        self.assertEqual(pyquran.check_sura_with_frequency(95,freq),True)

    def test_sort_dictionary_by_similarity(self):

        freq = pyquran.generate_frequency_dictionary(suraNumber=113)
        fre_dec = {'أعوذ': 1,
                   'إذا': 2,
                   'العقد': 1,
                   'الفلق': 1,
                   'النفثت': 1,
                   'برب': 1,
                   'حاسد': 1,
                   'حسد': 1,
                   'خلق': 1,
                   'شر': 4,
                   'غاسق': 1,
                   'فى': 1,
                   'قل': 1,
                   'ما': 1,
                   'من': 1,
                   'وقب': 1,
                   'ومن': 3}
        
        self.assertEqual(pyquran.sort_dictionary_by_similarity(freq),fre_dec)

        freq = pyquran.generate_frequency_dictionary(suraNumber=112)
        fre_dec={'الله': 2, 'ولم': 2, 'قل': 1, 'هو': 1, 'الصمد': 1, 'لم': 1, 'يلد': 1, 'يولد': 1, 'له': 1, 'كفوا': 1, 'أحد': 2, 'يكن': 1}
        self.assertEqual(pyquran.sort_dictionary_by_similarity(freq,threshold=0.2),fre_dec)

        
        fre_dec={'ولم': 2, 'الصمد': 1, 'لم': 1, 'يولد': 1, 'الله': 2, 'له': 1, 'أحد': 2, 'قل': 1, 'هو': 1, 'يلد': 1, 'يكن': 1, 'كفوا': 1}
        self.assertEqual(pyquran.sort_dictionary_by_similarity(freq,threshold=0.45),fre_dec)


    def test_frequency_of_character(self):
        ver_w_taskeel = quran.get_verse(1,1,with_tashkeel=True)
        self.assertEqual(pyquran.frequency_of_character(['ا','ض',"بً"],with_tashkeel=False),{'ا': 38667, 'ض': 1686, 'بً': 0})
        self.assertEqual(pyquran.frequency_of_character(['ا','ض',"بً"],with_tashkeel=True),{'ا': 38667, 'ض': 1686, 'بً': 218})
        self.assertEqual(pyquran.frequency_of_character(['ا','ض',"بً"],verseNum=1,with_tashkeel=True),{'ا': 426, 'ض': 18, 'بً': 2})
        self.assertEqual(pyquran.frequency_of_character(['ا','ض',"بً"],verseNum=4,chapterNum=12,with_tashkeel=True),{'ا': 4, 'ض': 0, 'بً': 1})
        self.assertEqual(pyquran.frequency_of_character(['ا','ض',"بً"],verse=ver_w_taskeel),{'ا': 3, 'ض': 0, 'بً': 0})


    def test_get_token(self):
        self.assertEqual(pyquran.get_token(4,1,1),'الرحيم')
        self.assertEqual(pyquran.get_token(5,1,1),'')
        self.assertEqual(pyquran.get_token(20,0,5),'')
        self.assertEqual(pyquran.get_token(20,0,-5),'')
        self.assertEqual(pyquran.get_token(95,1,5),'')
        self.assertEqual(pyquran.get_token(4,1,1,with_tashkeel=True),'الرَّحِيمِ')


    def test_search_sequence(self):

        result=pyquran.search_sequence(['بِسْمِ اللَّهِ','الرحمن'],verseNum=1,chapterNum=1)
        real={'الرحمن': [('الرَّحْمَنِ', 3, 1, 1)],
              'بسم الله': [('بِسْمِ اللَّهِ', 0, 1, 1)]}
        self.assertEqual(result,real)

        result=pyquran.search_sequence(['بِسْمِ اللَّهِ','الرحمن'],verseNum=1,chapterNum=1,mode=1)
        real={'الرحمن': [], 'بِسْمِ اللَّهِ': [('بِسْمِ اللَّهِ', 0, 1, 1)]}
        self.assertEqual(result,real)


    def test_search_with_pattern(self):
        result = pyquran.search_with_pattern(pattern="01101011000101",chapterNum=2)
        real=['ءَامِنُوا كَمَا ءَامَنَ النَّاسُ', 'وَلَتَجِدَنَّهُمْ أَحْرَصَ النَّاسِ', 'بِالْمَعْرُوفِ حَقًّا عَلَى الْمُتَّقِينَ', 'بِالْمَعْرُوفِ حَقًّا عَلَى الْمُحْسِنِينَ', 'لِلتَّقْوَى وَلَا تَنسَوُا الْفَضْلَ']
        self.assertEqual(result,real)

        result=pyquran.search_with_pattern(pattern="0110101100111010101",chapterNum=2)
        self.assertEqual(result,[])

        result = pyquran.search_with_pattern(pattern="01111",chapterNum=1)
        real = ['الرَّحِيمِ مَلِكِ', 'نَعْبُدُ وَإِيَّاكَ', 'الْمُسْتَقِيمَ صِرَطَ']
        self.assertEqual(result,real)

        try:
            pyquran.search_with_pattern(pattern="01111")
            result=True
        except:
            result=False
        self.assertEqual(result,False)
            

        result=pyquran.search_with_pattern(pattern="01111",chapterNum=1,threshold=0.9)
        real=['الرَّحِيمِ مَلِكِ', 'نَعْبُدُ وَإِيَّاكَ', 'الْمُسْتَقِيمَ صِرَطَ']
        self.assertEqual(result,real)


    def test_count_shape(self):
       # test case 1: small surah with system
       system = [[beh, teh, theh], [jeem, hah, khah]]
       returnedNParray = count_shape(get_sura(110), system)
       expectedFROW = [1, 2, 1, 0, 0, 0, 1, 0, 4, 0, 0, 1, 1,
                       0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 3,
                       0, 1, 1, 1, 0, 0]
       self.assertEqual(returnedNParray.shape, (3, 32))
       self.assertEqual(list(returnedNParray[0]), expectedFROW)

       # test case 2: big surah with system
       system = [[beh, teh, theh], [jeem, hah, khah]]
       returnedNParray = count_shape(get_sura(2), system)
       self.assertEqual(returnedNParray.shape, (286, 32))

      # test case 3: without system
       returnedNParray = count_shape(get_sura(110))
       expectedFROW = [1, 0, 0, 0, 1, 0, 4, 0, 0, 1, 0, 1, 1,
                       0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                       1, 0, 0, 3, 0, 1, 1, 1, 0, 0]
       self.assertEqual(returnedNParray.shape, (3, 36))
       self.assertEqual(list(returnedNParray[0]), expectedFROW)


    def test_buckwalter_transliteration(self):
           # test case 1:"from arabic without tashkeel to buckwalter "
           self.assertEqual(buckwalter_transliteration("مرحبا"), "mrHbA")

           # test case 2:"from arabic with tashkeel to buckwalter "
           arabicText = "يُولَدُ جَمِيعُ ٱلنّاسِ أَحْرَارًا مُتَسَاوِينَ فِي ٱلْكَرَامَةِ وَٱلْحُقُوقِ. وَقَدْ وُهِبُوا عَقْلًا وَضَمِيرًا وَعَلَيْهِمْ أَنْ يُعَامِلَ بَعْضُهُمْ بَعْضًا بِرُوحِ ٱلْإِخَاءِ"
           expectedTransliteration = "yuwladu jamiyEu {ln~Asi >aHoraArFA mutasaAwiyna fiy {lokaraAmapi wa{loHuquwqi. waqado wuhibuwA EaqolFA waDamiyrFA waEalayohimo >ano yuEaAmila baEoDuhumo baEoDFA biruwHi {lo<ixaA'i"
           self.assertEqual(buckwalter_transliteration(arabicText),
                            expectedTransliteration)

           # test case 3:"from buckwalter to arabic"
           bulkwalter = "mutasaAwiyna fiy {lokaraAmapi wa{loHuquwqi."
           expectedTransliteration = "مُتَسَاوِينَ فِي ٱلْكَرَامَةِ وَٱلْحُقُوقِ."
           self.assertEqual(buckwalter_transliteration(bulkwalter, True),
                            expectedTransliteration)

    def test_get_verse_count(self):
        # count elfatha with basmala
        self.assertEqual(get_verse_count(get_sura(1)), 7)

        self.assertEqual(get_verse_count(get_sura(9)), 129)

    def test_count_token(self):
        # count sura's tokens
        self.assertEqual(count_token(get_sura(112)), 15)
        # count ayah's tokens
        self.assertEqual(count_token(get_sura(112)[0]), 4)


if __name__ == '__main__':
    unittest.main()
