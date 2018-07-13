"""This modules contains functions to retrieve from quran.
"""
from xml.etree import ElementTree
import arabic as ar
import filtering
import error
import os

# Relative path to this modul's location in PyQuran.
corpus_xml_relative_path= '../QuranCorpus/quran-uthmani.xml'

# The current path of the current module.
current_path  = os.path.dirname(os.path.abspath(__file__))
# Joining this module's path with the relative path of the corpus
corpus_path = os.path.join(current_path, corpus_xml_relative_path)




# Parsing xml
quran_tree = ElementTree.parse(corpus_path)





def get_sura(sura_number, with_tashkeel=False, basmalah=False):
    """returns a sura as a list of verses.

    Args:
        sura_number: 1 <= Integer <= 114, the ordered number of sura in Mushaf.
        with_tashkeel: Boolean, if true return sura with tashkeel else return
                       without.
        basmalah: Boolean, adding basmalah as aya.
    Returns:
         [str]: a list of sura's ayat.

    Note:
        Index statrts at zero.
        So if the order number of an aya is x, then it's at (x-1) in the returned
        list.

    Example:
    ```python
       q.quran.get_sura(108, with_tashkeel=True)\n
       >>> ['إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ', 'فَصَلِّ لِرَبِّكَ وَانْحَرْ', 'إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ']
    ```
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

    if basmalah and sura_number != 1 -1 and sura_number != 9 -1:
        #suras_list[0][0].attrib['text']
        bismilah = [suras_list[0][0].attrib['text']]
        sura = bismilah + sura

    uthmanic_free_sura = []
    for aya in sura:
        uthmanic_free_sura.append(filtering.recitation_symbols_filter(aya))

    if not with_tashkeel:
       return list(map(ar.strip_tashkeel, uthmanic_free_sura)) 
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

    message = "Sura number must be an integer between 1 to 114, inclusive."
    error.is_int(sura_number, message)

    message = "Aya number is a positive integer."
    error.is_int(sura_number, message)


    aya_number -= 1
    sura = get_sura(sura_number)
    if aya_number > len(sura) - 1:
        raise ValueError('Aya number most not exceed the number of ayat in sura.')
    return sura[aya_number]



def retrieve_qruan_as_one_string():
    quran_string = ''
    for i in range (1, 115):
        for aya in get_sura(i, with_tashkeel=True):
                quran_string += aya + ' '
    return quran_string

def get_sura_number(sura_name):
    """
    Args:
        sura_name (str) : string represents the sura name.
    Returns:
        int: the sura number which name is sura_name.
    Note:
        Do not forget that the index of the returned list starts at zero.
        So if the order Sura number is x, then it's at (x-1) in the list.

    Example:
    ```python
    q.quran.get_sura_number('الملك')\n
    >>> 67
    ```
    """
    suras_list = quran_tree.findall('sura')
    suraNumber = None
    for index in range (1, 115):
        if suras_list[index-1].attrib['name'] == sura_name:
            suraNumber = index
    return suraNumber

def get_sura_name(sura_number=None):
    """Returns the name of `sura_number`. If `sura_number=None` a list of all
    sura's names is retunred.

    Args:
        sura_number: Optional, 1 <= Integer <= 114, the ordered number of sura in Mushaf.

    Returns:
        str: the sura name which number is sura_number.
        [srt]: list of all suras' names (if the sura_number parameter is None).

    Example:
    ```python
    q.quran.get_sura_name(2)\n
    >>> 'البقرة'
    ```
    """
    # get all suras
    suras_list = quran_tree.findall('sura')
    if sura_number is None :
        suraName = [(suras_list[i].attrib['name']) for i in range(0,114)]
    else:
        # get suraName
        suraName = suras_list[sura_number-1].attrib['name']
    # return suraName
    return  suraName



# Redandant: 
# 
def get_verse(sura_number, verse_number, with_tashkeel=False):
    """
        get specific verse form specific chapter
        
        Args:
            sura_number: 1 <= Integer <= 114, the ordered number of sura in Mushaf.
            verse_number: Integer > 0,  number of verse.
            with_tashkeel: Boolean, if true return sura with tashkeel else return
                           without.

        Returns:
            str:  a verse.

        Example:
        ```python
        q.quran.get_verse(sura_number=1, verse_number=2)\n
        >>> 'الحمد لله رب العلمين'
        ```
    """
    if(sura_number > ar.swar_num or verse_number<=0):
        return ""
    try:
        return get_sura(sura_number,with_tashkeel)[verse_number-1]
    except:
        return ""
