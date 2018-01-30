"""This modules contains functions to retrieve from quran.
"""
from xml.etree import ElementTree
from pyarabic.araby import strip_tashkeel
from uthmanic import *

# Parsing xml
xml_file_name = '../QuranCorpus/quran-uthmani.xml'
quran_tree = ElementTree.parse(xml_file_name)





def get_sura(sura_number, with_tashkeel=False):
    """gets an sura by returning a list of ayat al-sura.

    Args: 
        param1 (int): the ordered number of sura in The Mushaf.
        param2 (bool): if true return sura with tashkeel else return without
    Returns:
         [str]: a list of `ayat al-sura.`

    Usage Note:
        Do not forget that the index of the reunred list starts at zero.
        So if the order aya number is x, then it's at (x-1) in the list.

    Working_State: OK.

    TESTING: 
            1  Handle out of range inputs.
            2  Handle non integer inputs.

    """
    
    sura_number -= 1
    sura = []
    suras_list = quran_tree.findall('sura')
    ayat = suras_list[sura_number]

    for aya in ayat:
        sura.append(aya.attrib['text'])

    uthmanic_free_sura = []
    for aya in sura:
        uthmanic_free_sura.append(uthmanic_filter(aya))

    if not with_tashkeel:
       return list(map(strip_tashkeel, uthmanic_free_sura)) 
    else:
       return uthmanic_free_sura




def fetch_aya(sura_number, aya_number):
    """

    Args:
        param1 (int): the ordered number of sura in The Mus'haf.
        param2 (int): the ordered number of aya in The Mus'haf.

    Returns:
        str: an aya as a string

    """
    aya_number -= 1
    sura = get_sura(sura_number)
    return sura[aya_number]

def retrieve_qruan_as_one_strint():
    pass

