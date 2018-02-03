# PyQuran

* [Features](#features)
* [Usage](#usage)
* [Functions](#functions)
    * [Access functions](#access-functions)
    * [Manipulate functions](#manipulate-functions)
    * [Analysis functions](#analysis-functions)
    * [Search functions](#search-functions)
    * [Other functions](#access-functions)
    



# Features

* Access Holy-Quran :
    - get **Chapter** with/without diacritics.
    - get **Verse** with/without diacritics.
    - get **Token** (word).
    - get **Chapter name** , **Chapter number**.
    - get **Verses number** in verse.
* Manipulate with Holy-Quran :
    - Separate to **Tokens** with/without diacritics.
    - Separate to **letters** with/without diacritics.
    - Apply your **System** on Quran.
    - get **Binary representation** of Holy-Quran as 0's , 1's.
    - Extract **Taskill** from sentence. 
    - Dealing with linguistic rules like :
        - Transfer Alef-mad **"آ"** to "أَأْ" 
    - Convert the **unicode of arabic** text to **buckwalter encoding** and vice versa
* Analysis Holy-Quran:
    - get **Frequency Matrix** of letters dependent on Applied _alphabet system_.
    - get **Frequency dictionary** of tokens.
    - sort **Frequency dictionary** using similarity threshold.
* Search in Holy-Quran using :
    - **Text** and ther is a variety options.
    - **diacritics pattern**. 
    - **binary representation pattern** using threshold.



# Usage

```python
   import PyQuran as pq
```


# Functions

## Access functions:

##### get-sura : 
**get_sura(suran_num,with_tashkeil)**
- takes **sura_num** it's the number of surah  and returns sura verses and **with_tashkeil** is the diacritics option and if **_True_** return verses with diacritics and if **False** return without and defualt _false_. 

```python
  sura = pq.get_sura(108,True)
  print(sura)

  >>> ['إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ', 'فَصَلِّ لِرَبِّكَ وَانْحَرْ', 'إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ']
```

**get_sura_number** function takes the name of chapter and it returns the number of chapter
<br>
```python
  suraNumber = pq.get_sura_number('الملك')
  print(suraNumber)

  >>> 67
```
**get_sura_name** function takes the number of chapter and it returns the name of chapter
<br>
```python
  suraName = pq.get_sura_name(67)
  print(suraName)

  >>> الملك
```

**get_verse** function takes the surah and ayah number and the option of diacritics its default is **False** to activate it pass **True** then it returns the text of ayah
<br>
```python
  ayahText=pq.get_verse(110,1,True)
  print(ayahText)

  >>> إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ

```

**get_token** function takes the **token number(position Of Token)** , **verse number** and **chapter number** the option of diacritics its default is **False** to activate it pass **True** then it returns the token
<br>

```python
  tokenText = pq.get_token(4,1,114,True)
  print(tokenText)

  >>> النَّاسِ
```




## Count functions:

 **count_shape** function takes the shape of character as example [[bah,gem]] and <br> counts it in verse or chapter or all quran: Example:
<br>
```python
  newSystem=[[beh, teh, theh], [jeem, hah, khah]]
  alphabetAsOneShape =pq.count_shape(get_sura(110), newSystem)
  print(alphabetAsOneShape)

  >>> [[1 2 1 0 0 0 1 0 4 0 0 1 1 0 0 0 1 0 0 0 0 0 1 0 0 3 0 1 1 1 0 0]
       [1 2 0 0 2 0 0 0 5 0 2 0 1 0 1 0 0 0 0 0 0 0 2 0 0 4 0 3 1 3 1 3]
       [6 2 0 0 0 0 1 0 4 0 1 0 2 0 2 0 0 0 0 0 0 1 2 0 2 0 1 2 2 2 0 0]]
```

**count_token** function takes text (ayah or surah) and returns the number of token in ayah or surah: Example:
<br>
***note***: the harf ('و') is not calculated as token alone
<br>
```python
  numberOfToken=pq.count_token(tools.get_sura(110))
  print(numberOfToken)

  >>> 19
```
**get_verse_count** function takes surah and calculates the number of ayat in surah: Example:

```python
  numberOfAyat = tools.get_verse_count(pq.get_sura(110,True))
  print(numberOfAyat)

  >>> 3
```


**frequency_of_character** function counts characters occurrence for verses or with chapter or even all quran and returns the dictionary contains the key char and values is an occurrence of character
<br>

```python
  frequencyOfChar =tools.frequency_of_character(['أ','ب'],'قل أعوذ برب الناس',114,1)
  print(frequencyOfChar)

  >>> {أ:1,ب:2}
```

## Search functions
**search_sequence** function takes list of sequences and returns (matched sequences,Token_no,verse_number,chapter number) it searches in verse , chapter or All Quran
<br>
```python
  matchedKeyword = pq.search_sequence(['قل أعوذ برب'])
  print(matchedKeyword)

  >>> {'قل أعوذ برب': [('قُلْ أَعُوذُ بِرَبِّ', 0, 1, 113), ('قُلْ أَعُوذُ بِرَبِّ', 0, 1, 114)]}

```

**search_string_with_tashkeel** function takes an Ayah and Pattern **composed of (0,1)** and it returns **True** if the text has tashkeel pattern**False** if the diacritics pattern doesn't match the text and it returns the locations that matched the pattern of diacrictics start index **inclusive** and end index **exculsive**
<br>
```python

  sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
  tashkeel_pattern = ar.fatha + ar.sukun
  results = search_string_with_tashkeel(sentence,
  tashkeel_pattern)
  print(results)

  >>> (True, [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)])
```

## Additional functions
***

**buckwalter_arabic_transliteration** function takes an **unicode  string** and the option of reverse has default value **False** to convert **unicode string** to **bukwalter encoding**.and it has value **True** to **buckwalter encoding** to **unicode of arabic**
<br>
**note**:the encoding with **diacritics** is  different from **without diacritics**
<br>

```python
  buckwalterEncode = pq.buckwalter_arabic_transliteration('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
  print(buckwalterEncode)

  >>> <in~aA >aEoTayonaka Alokawovara
```

**unpack_alef_mad** function takes the alef_mad and it returns alef with hamza and alef with sukun
<br>
```python
  unpackAlefMad = pq.unpack_alef_mad('آ')
  print(unpackAlefMad)

  >>> 'أْأَ'
```

**get_tashkeel_binary** function which takes the verses or chapters with diacritics and it returns the mapping of **marks of diacritics** to **(0,1)** **harakah** represents **1** and **sukun** represents **0** with list of diacritics
<br>
```python
  pattern = pq.get_tashkeel_binary('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
  print(pattern)

  >>> ('1010 101011 001011', ['ِ', 'ْ', 'َ', '', '', 'َ', 'ْ', 'َ', 'ْ', 'َ', 'َ', '', '', 'ْ', 'َ', 'ْ', 'َ', 'َ'])

```

**generate_frequancy_dictionary** function takes the number of chapter and it returns the dictionary of words contains the **word** and its **frequency** the key of dictionary is word and the value  is frequency of word
<br>
```python
  dictionaryFrequency = pq.generate_frequency_dictionary(114)
  print(dictionaryFrequency)

  >>> {'الناس': 4, 'من': 2, 'قل': 1, 'أعوذ': 1, 'برب': 1, 'ملك': 1, 'إله': 1, 'شر': 1, 'الوسواس': 1, 'الخناس': 1, 'الذى': 1, 'يوسوس': 1, 'فى': 1, 'صدور': 1, 'الجنة': 1, 'والناس': 1}
```

**separate_token_with_diacritics** function takes the verses or chapters and it separate the verses or chapters to each character with diacritics
<br>
```python
  wordSeparated = pq.separate_token_with_dicrites('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
  print(wordSeparated)

  >>> ['إِ', 'نَّ', 'ا', ' ', 'أَ', 'عْ', 'طَ', 'يْ', 'نَ', 'كَ', ' ', 'ا', 'لْ', 'كَ', 'وْ', 'ثَ', 'رَ']
```
**sort_dictionary_by_similarity** function using to **cluster words  by using similarity** and sort every bunch of word  by most common and sort bunches descending in the same time takes the frequency dictionary generated by using **generate_frequency_dictionary** function. This function takes dictionary frequency and **threshold** to specify **the degree of similarity** 
 <br>
```python
  sortedDictionary = pq.sort_dictionary_by_similarity(dictionaryFrequency)
  print(sortedDictionary)

  >>> {'الناس': 4, 'الخناس': 1, 'والناس': 1, 'من': 2, 'قل': 1, 'أعوذ': 1, 'برب': 1, 'ملك': 1, 'إله': 1, 'شر': 1, 'الوسواس': 1, 'الذى': 1, 'يوسوس': 1, 'فى': 1, 'صدور': 1, 'الجنة': 1}
```

**shape** function takes **a new system for alphabets** ,passing the alphabets "**in a list of list**" that want to count it as on shape "**inner list**" and returns a dictionary has the same value for each set of alphabets and diffirent values for the rest of alphabets
<br>
```python
  newSystem = [[pq.beh, pq.teh], [pq.jeem, pq.hah, pq.khah]]
  shape = pq.shape(newSystem)
  print(sortedDictionary)

  >>> {'ب': 0, 'ت': 0, 'ث': 0, 'ج': 1, 'ح': 1, 'خ': 1, 'ء': 2, 'آ': 3, 'أ': 4, 'ؤ': 5, 'إ': 6, 'ئ': 7, 'ا': 8, 'ة': 9, 'د': 10, 'ذ': 11, 'ر': 12, 'ز': 13, 'س': 14, 'ش': 15, 'ص': 16, 'ض': 17, 'ط': 18, 'ظ': 19, 'ع': 20, 'غ': 21, 'ف': 22, 'ق': 23, 'ك': 24, 'ل': 25, 'م': 26, 'ن': 27, 'ه': 28, 'و': 29, 'ى': 30, 'ي': 31, ' ': 70}
```

**check_sura_with_frequency** function checks if frequency dictionary of **specific chapter** is compatible with **original chapter** in quran
<br>
```python
  dictionaryFrequency = pq.generate_frequency_dictionary(111)
  matched = pq.check_sura_with_frequency(110,dictionaryFrequency)
  print(matched)

  >>> False
```

**generate_latex_table** generates latex code of table of frequency 
it takes dictionary frequency , file name and location : location to save , the default location is same directory by symbol '.'then it returns **True** if the operation of generation completed successfully **False** if something wrong 
<br>
```python
  latexTable = pq.generate_latex_table(dictionaryFrequency,'any_file_name')
  print(latexTable)

  >>> True
```
