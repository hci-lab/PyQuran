"""This modules contains functions to retrieve from quran.
"""
from xml.etree import ElementTree
from pyarabic.araby import strip_tashkeel
from arabic import swar_num
from filtering import *
import error

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
    
    message = "Sura number must be an integer between 1 to 114, inclusive."
    error.is_int(sura_number, message)

    message = "The second parameter must be bool, it an optional False by default"
    error.is_bool(with_tashkeel, message)
       
    
    sura_number -= 1
    sura = []
    suras_list = quran_tree.findall('sura')
    ayat = suras_list[sura_number]

    for aya in ayat:
        sura.append(aya.attrib['text'])

    uthmanic_free_sura = []
    for aya in sura:
        uthmanic_free_sura.append(recitation_symbols_filter(aya))

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

def get_sura_number(suraName):
    """It takes sura name as string, and returns the an ordered number(integer) of the sura
    Args:
        suraName (str) : string represents the sura name.
    Returns:
        int: the sura number which name is suraName.
    Usage Note:
        Do not forget that the index of the returned list starts at zero.
        So if the order Sura number is x, then it's at (x-1) in the list.
    """
    suras_list = quran_tree.findall('sura')
    suraNumber = None
    for index in range (1,115):
        if suras_list[index-1].attrib['name'] == suraName:
            suraNumber = index
    return suraNumber

def get_sura_name(suraNumber=None):
    """It takes and ordered number of a sura, and returns the sura name as string or
	returns a list contains all suras' names if you don't pass any parameter (the entire Quran is targeted).
    Args:
        suraNumber (int): it's optional
    Returns:
        str: the sura name which number is suraNumber
        OR
        [srt]: list of all suras' names (if the suraNumber parameter is None)
    Usage Note:
        Do not forget that the index of the returned list starts at zero.
        So if the order Sura number is x, then it's at (x-1) in the list.
    """
    # get all suras
    suras_list = quran_tree.findall('sura')
    if suraNumber is None :
        suraName = [(suras_list[i].attrib['name']) for i in range(0,114)]
    else:
        # get suraName
        suraName = suras_list[suraNumber-1].attrib['name']
    # return suraName
    return  suraName



# Redandant: 
# 
def get_verse(chapterNum,verseNum,with_tashkeel=False):
    """
        get specific verse form specific chapter
        
        Args:
            chapterNum (int): number of chapter 
            verseNum (int): number of verse 
            with_tashkeel (int) : to check if search with taskeel or not

        Returns:
            str :  return verse
    """
    if(chapterNum > swar_num or verseNum<=0):
        return ""
    try:
        return get_sura(chapterNum,with_tashkeel)[verseNum-1]
    except:
        return ""
