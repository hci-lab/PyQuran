def parseQuranTxtFile(txtFilePath,separatorTxt,copyRightsStratingChar):
    """Parse input txt file Quran with three column delimeters
        1- Read the input txt
        2- Rename pandas columns to be ["SurahIdx", "AyahIdx","AyahText"]
        3- Remove the copy rights sections with start with #
        4- Set the dataframe index to be ["SurahIdx", "AyahIdx"]
  
      Args:
        txtFilePath (str): input path to the quran-simple-clean.txt
        Separator (str): Separator char
        copyRightsStratingChar (str): copyRights parts starting chars Ex: #

    Returns:
        pandasDF: cleaned indexed pandas dataframe.

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `Separator` is multi char.
        ValueError: If `txtFilePath` is not exists .
    Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension
    Examples:
        >>> QuranDf = parseQuranTxtFile('quran-simple-clean.txt','|','#')
        >>> ayahText = QuranDf.loc[1].loc[1] #filter for surah
        >>> ayahText            
            AyahText    بسم الله الرحمن الرحيم
            Name: 1, dtype: object
    


    """
    QuranDf = pd.read_csv(xmlFilePath, sep=separatorTxt,names = ["SurahIdx", "AyahIdx","AyahText"])

    #to remove the copyrights rows
    QuranDf = QuranDf[~QuranDf.SurahIdx.str.startswith(copyRightsStratingChar)]

    #to add set types for dataframe for fast processing
    QuranDf['SurahIdx'] = QuranDf.SurahIdx.astype(int)
    QuranDf['AyahIdx'] = QuranDf.AyahIdx.astype(int)

    #set SurahIdx as index for filteration perspective
    QuranDf.set_index(['SurahIdx','AyahIdx'],inplace=True)
    return QuranDf