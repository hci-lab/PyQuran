from xml.etree import ElementTree
import numpy
from collections import Counter
import operator
from audioop import reverse
from itertools import chain
import functools
from collections import Counter, defaultdict
from arabic import *



xml_file_name = 'QuranCorpus/quran-simple-clean.xml'
quran_tree = ElementTree.parse(xml_file_name)


def get_sura(sura_number):
    """gets an sura by returning a list of ayat al-sura.

    Args:
        param1 (int): the ordered number of sura in The Mushaf.

    Returns:
         [str]: a list of ayat al-sura.

    Usage Note:
        Do not forget that the index of the reunred list starts at zero.
        So if the order aya number is x, then it's at (x-1) in the list.

    """
    sura_number -= 1
    sura = []
    suras_list = quran_tree.findall('sura')
    ayat = suras_list[sura_number]
    for aya in ayat:
        sura.append(aya.attrib['text'])
    return sura

def shape(system):
    """
    	 shape declare a new system for alphabets ,user pass the alphabets "in a list of list"
    	 that want to count it as on shape "inner list" and returns a dictionary has the same value
         for each set of alphabets and diffrent values for the rest of alphabets

        Args:

            param1 ([[char]]): a list of list of alphabets , each inner list have
                              alphabets that with be count  as one shape .
        Returns:
            dictionary: with all alphabets, where each char "key"  have a value
            value will be equals for alphabets that will be count as oe shape


    """
    listOfAlphabet = sorted(list(alphabet))
    print(listOfAlphabet)

    alphabetMap = dict()

    indx = 0
    '''
        for char in listOfAlphabet:
            alphabetMap.update({char: indx})
            indx = indx + 1
        alphabetMap.update({" ": 70})
    print("--------alphabetMap-------")
    '''




    newAlphabet=sorted(list(set(chain(*system))))
    print(newAlphabet)

    theRestOfAlphabets=sorted(list(set(listOfAlphabet)-set(newAlphabet)))
    print(theRestOfAlphabets)

    for setOfNewAlphabet in system:
        for char in setOfNewAlphabet:
            alphabetMap.update({char:indx})
        indx=indx+1
    print(alphabetMap)

    for char in theRestOfAlphabets:
        alphabetMap.update({char:indx})
        indx=indx+1

    alphabetMap.update({" ": 70})


    print("------------End Shape Fun----------------------")

    print(alphabetMap)
    return alphabetMap

def convert_text_to_numbers(text,alphabetMap):
    """
        	 convert_text_to_numbers get a text (surah or ayah) and convert it to list of numbers
        	 depends on alphabetMap dictionary , user pass the text "list or list of list" that want to count it
        	 and dictionary that has each chat with it's number that will convert to,and returns a list of numbers





            What it does:
                it convert each letter to a number "corresponding to dictionary given as argument"


            Args:

                param1 ([str] ): a list of strings , each inner list is ayah .
                param2(dict) : a dictionary has each alphabet with it's corresponding number
            Returns:
                List: list of numbers, where each char in the text converted to number


            """
    #sorted(text)
    i=0
    textToNumber=[]
    for char in text:
        textToNumber.insert(i, alphabetMap[char])
        i = i + 1

    #print(textToNumber)
    #print("------------------end of text to num--------------")
    return textToNumber


def count_shape(text, system=None):
    listOfAlphabet = sorted(list(alphabet))
    print(listOfAlphabet)
    if system == None:
        alphabetMap = dict()

        indx = 0
        for char in listOfAlphabet:
            alphabetMap.update({char: indx})
            indx = indx + 1
        alphabetMap.update({" ": 70})
        print("--------alphabetMap-------")
        print(alphabetMap)
    else:
        alphabetMap=shape(system)

    p=len(listOfAlphabet)-len(list(set(chain(
        *system))))+len(system)#+1 #the last one for space char
    A=numpy.zeros((len(text), p+1), dtype=numpy.int)#(m-len(list(set(
    # chain(*system)))))+len(system)
    i=0
    j=0
    lastVal=-1
    verses=[[]]
    charCount =[]
    #alphabetMap.popitem()
    #A[i, :] = Counter(convert_text_to_numbers(verse, alphabetMap))
    for verse in text:
        verse=convert_text_to_numbers(verse, alphabetMap)
        for val in alphabetMap.values() :                   #for key, value in
            # alphabetMap.items():
            print(val)

            if lastVal<val :
                charCount.insert(j, verse.count(val))
                lastVal=val
                j += 1
        #for key,char in (Counter(convert_text_to_numbers(verse,
                                                    #  alphabetMap))).items():
            #charCount.insert(j, char)
        #print(charCount)
        print("------------------------------")
        A[i, :]= charCount#[:-1]
        #verses.insert(i, charCount[:-1])
        i+=1
        charCount= []
        j=0
        val=0
        lastVal=0
    C=numpy.asarray(verses)
    print(C)

    return C

def coun_shape(text, system=None):
    """
        count_shape parses the text  and returns a N*P matrix (ndarray),

        the number of rows equals to the number of verses ,
        and the number of columns equals to the number of shapes.

        What it does:
            count the occuerence of each shape in text, depends on the your system ,
            If you don't pass system, then it will count each char as one shape.

            If `A` is a ndarray,
            then A[i,j] is the number of occurrences of alphabet(s)[j] in the
            verse i.

        Args:
            param1 ([str] ): a list of strings , each inner list is ayah .
            param2([[char]]) : it's optional ,
                                -a list of list , each iner list has alphabets that will count as one shape
                                - If you don't pass your system, then it will count each char as one shape
        Returns:
            ndarray: with dimensions (N * P), where
            `N` is the number of verses in chapter and
            `P` the number of elements in system + the number of alphapets as on char [alphabets in system excluded]


    """
    listOfAlphabet = sorted(list(alphabet))
    print(listOfAlphabet)
    if system == None:
        alphabetMap = dict()

        indx = 0
        for char in listOfAlphabet:
            alphabetMap.update({char: indx})
            indx = indx + 1
        alphabetMap.update({" ": 70})

    else:
        alphabetMap=shape(system)

    p=len(listOfAlphabet)-len(list(set(chain(
        *system))))+len(system)#+1 #the last one for space char
    n=len(text)
    A=numpy.zeros((n, p), dtype=numpy.int)#(m-len(list(set(
    # chain(*system)))))+len(system)
    i=0
    j=0
    charCount =[]
    for verse in text:
        verse=convert_text_to_numbers(verse, alphabetMap)
        for k in range(0,p,1) :                   #for key, value in
            # alphabetMap.items():
            charCount.insert(j, verse.count(k))
            j+=1
        A[i, :] =charCount
        i+=1
        charCount=[]
        j=0

    return A


def main():
    #print(buckwalter_transliteration(get_sura(9)[0], False))
    #print(buckwalter_arabic_transliteration(get_sura(9)[0], False))

    print("------------------------------------------------------")
    #print(buckwalter_transliteration("brA'p mn Allh wrswlh <lY Al*yn EAhdtm
    # mn Alm$rkyn", True))
    #print(buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn
    # EAhdtm mn Alm$rkyn", True))
    #print(buckwalter_arabic_transliteration("brA'p mn Allh wrswlh <lY Al*yn "
    #                                 #       "EAhdtm mn Alm$rkyn", True))
    print("------------------------------------------------------")
    print(get_sura(110))
    print( coun_shape(get_sura(110), [[beh], [dal,thal], [teh, noon]]))
    #newSystem=[[teh,beh,teh,noon],[dal,thal],[jeem,hah,khah],[sad,dad,tah,zah],[ain,ghain]]
    #newSystem=[['r']]
    #print (shape(newSystem))
    ''' 
    alphabetAsOneShape, alphabetCount, A =count_shape(get_sura(110),[[beh,teh, theh], [jeem, hah, khah]])
    print(A)
    print("------------------------------------------------------")
    printf = functools.partial(print, end=" ")
    for key in alphabetAsOneShape:  # .encode("utf-8")
        for val in alphabetAsOneShape[key]:
            printf(val)
        print(" : " + str(alphabetCount[key]))
    '''









if __name__ == '__main__':
    main()




























