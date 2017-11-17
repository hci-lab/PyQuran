import pyarabic.araby as arabic
import pandas as pd

def retrieveStringCharFrequency(inputString,disctAlphabets):  
    dict_obj = disctAlphabets.copy() #to update into the new dictionary not the old one
    for key,val in collections.Counter(araby.normalize_hamza(inputString)).items():
        if key in dict_obj:
            dict_obj[key] = val
    return dict_obj


def parseSurah(quranDF,surahIdx,alphabetsList):
    """
    The function parses the Sura and new pandaDataframe of a number of verses and each row output contains 
    verse number, text, dictionary of (letters,freq)
    
    Args:
        quranDF (dataframe): pandaDataframe of (AyahIdx,AyahText)
        surahIdx (int): number of the surah 
        alphabetsList List[str]: list of list of alphabets that contains m unicodes representing m characters; 
    the default is the 29 characters where hamza is the 29th letter
        
    Returns:
        pandasDF: new pandas dataframe with new column AyahLetterFreq 

    Raises:
        AttributeError: 
        ValueError: If `quranDF` is empty .
        ValueError: If `surahIdx` is not exists .
        ValueError: If `alphabetsList` is empty.
    Todo:
    * To implement the AttributeError handling exceptions
    
    Examples:
        >>> #alphabets=['ي','و','ه','ن','م','ل','ك','ق','ف','غ','ع','ظ','ط','ض','ص','ش','س','ز','ر','ذ','د','خ','ح','ج','ث','ت','ب','ا','ء']
        >>> alphabets=['ا','ل']
        >>> QuranDf = parseQuranTxtFile('quran-simple-clean.txt','|','#')
        >>> parsedSurah = parseSurah(QuranDf,1,alphabets)

        >>> parsedSurah #return all verses with ayahtext and freq
        >>> parsedSurah.iloc[2] # return the Ayah index 2
        >>> parsedSurah.iloc[2].loc["AyahLetterFreq"].get('ل') # return the frequency of the letter ل into ayah 2
    """
    disctAlphabets =  dict((el,0) for el in alphabetsList)
    filterQuranDF = quranDF.loc[surahIdx]
    filterQuranDF["AyahLetterFreq"] = filterQuranDF['AyahText'].apply(retrieveStringCharFrequency,args=(disctAlphabets,))
    return filterQuranDF