```python
X
```
X

**Arguments**

- **X**:  X


**Example**

```python
X
```
--------







-------------------
# Thbeed

* [Features](#features)
* [Imporatan information](#imporatan-information)
* [Usage](#usage)
* [Functions](#functions)
    * [Access functions](#access-functions)
        [x] DONE
    * [Manipulate functions](#manipulate-functions)
        [x] DONE
    * [Analysis functions](#analysis-functions)
        * [count_shape](#count_shape)
        * [count_token](#count_token)
        * [frequency_of_character](#frequency_of_character) 
        * [generate_frequancy_dictionary](#generate_frequancy_dictionary)
        * [sort_dictionary_by_similarity](#sort_dictionary_by_similarity)
        * [check_sura_with_frequency](#check_sura_with_frequency)
        * [generate_latex_table](#generate_latex_table)
    * [Search functions](#search-functions)
        * [search_sequence](#search_sequence)
        * [search_string_with_tashkeel](#search_string_with_tashkeel)
        * [search_with_pattern](#search_with_pattern)



# Features

* Access Holy-Quran :
    - get **Chapter** with/without diacritics.
    - get **Verse** with/without diacritics.
    - get **Token** (word).
    - get **Chapter name** , **Chapter number**.
    - get **Verses number** in verse.
* Manipulate with Holy-Quran :
    - Separate to **letters** with/without diacritics.
    - Apply your **System** on Quran.
    - get **Binary representation** of Holy-Quran as 0's , 1's.
    - Extract **Taskill** from sentence. 
    - Dealing with linguistic rules like :
        - Transfer Alef-mad **"آ"** to "أَأْ" 
    - Convert the **unicode of arabic** text to **buckwalter encoding** and vice versa
    - Convert Quran to **buckwalter reprsentation** and vice versa. 
* Analysis Holy-Quran:
    - get **Frequency Matrix** of letters dependent on Applied _alphabet system_.
    - get **Frequency dictionary** of tokens.
    - sort **Frequency dictionary** using similarity threshold.
* Search in Holy-Quran using :
    - **Text** and ther is a variety options.
    - **diacritics pattern**. 
    - **binary representation pattern** using threshold.








# Functions
## Manipulate functions:



## Analysis functions:

#### count_shape 
**count_shape(text, system=None)**
- takes **text** (chapter/verse), **system (optional)** it's the shape of character as example [[bah,gem]] and return a **n*p matrix** where **n** number of verses and **p** number of collections in system and if not pass system it will apply the defualt.  

```python
  newSystem=[[beh, teh, theh], [jeem, hah, khah]]
  alphabetAsOneShape =pq.count_shape(get_sura(110), newSystem)
  print(alphabetAsOneShape)

  >>> [[1 2 1 0 0 0 1 0 4 0 0 1 1 0 0 0 1 0 0 0 0 0 1 0 0 3 0 1 1 1 0 0]
       [1 2 0 0 2 0 0 0 5 0 2 0 1 0 1 0 0 0 0 0 0 0 2 0 0 4 0 3 1 3 1 3]
       [6 2 0 0 0 0 1 0 4 0 1 0 2 0 2 0 0 0 0 0 0 1 2 0 2 0 1 2 2 2 0 0]]
```

#### count_token
**count_token(text)** 
- takes **text** (chapter/verse) and returns the number of tokens.
###### ***note***: the harf ('و') is not calculated as token alone

```python
  numberOfToken=pq.count_token(tools.get_sura(110))
  print(numberOfToken)

  >>> 19
```


#### frequency_of_character 
**frequency_of_character(characters,verse=None,chapterNum=0,verseNum=0,with_tashkeel=False)**
- takes **characters** that you need to count , return dictionary that havecounts characters occurrence for verses or with chapter or even all quran and the dictionary contains the key char and values is an occurrence of character .
- optional opptions: 
    - **verse** (str): if passed, it will applied to this string only 
    - **chapterNum** (int) : if passed only, it will applied to this chapter only.
    - **verseNum** (int) :
        - if passed only, it will applied to **verseNum** for **all Chapters**.
        - if passed with **chapterNum**, it will applied to verseNum for **chapterNum**.
    - **with_tashkeel** (bool):
        - if **True** applied to Quran **with** Tashkieel.
        - if **False** applied to Quran **without** Tashkieel.
- Note : if don't pass any  **optional opptions** it will applied to all **Quran**.

```python
  frequencyOfChar =tools.frequency_of_character(['أ','ب'],'قل أعوذ برب الناس',114,1)
  print(frequencyOfChar)

  >>> {أ:1,ب:2}
```


#### generate_frequancy_dictionary
**generate_frequency_dictionary(suraNumber=None)** 
- takes **suraNumber (optional)** the number of chapter and it returns the dictionary of  words contains the **word** as key and its **frequency** as value and if not pass **suraNumber** it will applied to **all-Quran**.

```python
  dictionaryFrequency = pq.generate_frequency_dictionary(114)
  print(dictionaryFrequency)

  >>> {'الناس': 4, 'من': 2, 'قل': 1, 'أعوذ': 1, 'برب': 1, 'ملك': 1, 'إله': 1, 'شر': 1, 'الوسواس': 1, 'الخناس': 1, 'الذى': 1, 'يوسوس': 1, 'فى': 1, 'صدور': 1, 'الجنة': 1, 'والناس': 1}
```


#### sort_dictionary_by_similarity
**sort_dictionary_by_similarity(frequency_dictionary,threshold=0.8)**
- using to **cluster words  by using similarity** and sort every bunch of word  by most common and sort bunches descending in the same time takes the frequency dictionary generated using [generate_frequency_dictionary](#generate_frequency_dictionary) function. This function takes dictionary of frequencies and **threshold (optional)** to specify **the degree of similarity** 
 
```python
  sortedDictionary = pq.sort_dictionary_by_similarity(dictionaryFrequency)
  print(sortedDictionary)

  >>> {'الناس': 4, 'الخناس': 1, 'والناس': 1, 'من': 2, 'قل': 1, 'أعوذ': 1, 'برب': 1, 'ملك': 1, 'إله': 1, 'شر': 1, 'الوسواس': 1, 'الذى': 1, 'يوسوس': 1, 'فى': 1, 'صدور': 1, 'الجنة': 1}
```

#### check_sura_with_frequency
**check_sura_with_frequency(sura_num,freq_dec)**
- function checks if frequency dictionary of **specific chapter** is compatible with **original chapter** in quran, it takes **sura_num** (chapter number) and **freq_dec** (frequency dictionary) and return **True** if compatible and **False** in not.

```python
  dictionaryFrequency = pq.generate_frequency_dictionary(111)
  matched = pq.check_sura_with_frequency(110,dictionaryFrequency)
  print(matched)

  >>> False
```

#### generate_latex_table
**generate_latex_table(dictionary,filename,location=".")**
- generates latex code of table of frequency it takes dictionary frequency ,it takes **dictionary** (frequency dictionary) , **filename** and **location** (location to save) , the default location is same directory by symbol '.', then it returns **True** if the operation of generation completed successfully **False** if something wrong 

```python
  latexTable = pq.generate_latex_table(dictionaryFrequency,'any_file_name')
  print(latexTable)

  >>> True
```

 
## Search functions

#### search_sequence
**search_sequence(sequancesList,verse=None,chapterNum=0,verseNum=0,mode=3)**
- take list of sequances and return matched sequance, it search in verse ot chapter or All Quran,
    - it return for every match :
         - matched sequance 
         - chapter number of occurrence
         - token number if word and 0 if sentence
        
    - Note :
         - if found verse != None it will use it en search .    
         - if no verse and found chapterNum and verseNum it will use this verse and use it to search.
         - if no verse and no verseNum and found chapterNum it will search in chapter.
         - if no verse and no chapterNum and no verseNum it will search in All Quran.
        
    - it has many modes:
        1. search with decorated sequance (with tashkeel), and return matched sequance with decorates (with tashkil).
        2. search without decorated sequance (without tashkeel), and return matched sequance without decorates (without tashkil).
        3. search without decorated sequance (without tashkeel), and return matched sequance with decorates (with tashkil).
            
        
    - optional opptions: 
        - **verse** (str): if passed, it will applied to this string only 
        - **chapterNum** (int) : if passed only, it will applied to this chapter only.
        - **verseNum** (int) :
            - if passed only, it will applied to **verseNum** for **all Chapters**.
            - if passed with **chapterNum**, it will applied to verseNum for **chapterNum**.
        - **with_tashkeel** (bool):
            - if **True** applied to Quran **with** Tashkieel.
            - if **False** applied to Quran **without** Tashkieel.
            - mode (int): this mode that you need to use and default mode 3
            
    - Note : if don't pass any  **optional opptions** it will applied to all **Quran**.
    - Returns: dict() : key is sequances and value is a list of matched_sequance and their positions

```python
  matchedKeyword = pq.search_sequence(['قل أعوذ برب'])
  print(matchedKeyword)

  >>> {'قل أعوذ برب': [('قُلْ أَعُوذُ بِرَبِّ', 0, 1, 113), ('قُلْ أَعُوذُ بِرَبِّ', 0, 1, 114)]}

```

#### search_string_with_tashkeel
**search_string_with_tashkeel(sentence,tashkeel_pattern)**
- takes an **sentence** and **tashkeel_pattern** (composed of 0's , 1's) and it returns the locations that matched the pattern of diacrictics start index **inclusive** and end index **exculsive** and return empty list if not found.

```python

  sentence = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
  tashkeel_pattern = ar.fatha + ar.sukun
  results = pq.search_string_with_tashkeel(sentence,tashkeel_pattern)
  print(results)

  >>> [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)]
```


#### search_with_pattern 
**search_with_pattern(pattern,sentence=None,verseNum=None,chapterNum=None,threshold=1)**
- this function use to search in 0's,1's pattern and return matched words from sentence pattern dependent on the    threshold, it takes a **patter** that you need to looking for , and **sentence (optional)** (sentence where will   search), **chapterNum (opetional)** and **verseNum (opetional)** and return list of matched words and sentences. 

    - Cases: 
        1. if pass sentece only or with another args 
           it will search in sentece only.
        2. if not passed sentence and passed verseNum and chapterNum,
           it will search in this verseNum that exist in chapterNum only.
        3. if not passed sentence,verseNum and passed chapterNum only,
           it will search in this specific chapter only
    
      * Note : it's takes time dependent on your threshold and size of chapter, so it's not support to search on All-Quran becouse it take very long time more than 11 min.

```python

  result = pq.search_with_pattern(pattern="01111",chapterNum=1,threshold=0.9)
  print(result)
  
  >>>['الرَّحِيمِ مَلِكِ', 'نَعْبُدُ وَإِيَّاكَ', 'الْمُسْتَقِيمَ صِرَطَ']
```

