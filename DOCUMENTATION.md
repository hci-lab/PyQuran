# Documentation

* [Features](#features)
* [Imporatan information](#imporatan-information)
* [Usage](#usage)
* [Functions](#functions)
    * [Access functions](#access-functions)
        * [get_sura](#get_sura)
        * [get_verse](#get_verse)
        * [get_token](#get_token)
        * [get_sura_number](#get_sura_number)
        * [get_sura_name](#get_sura_name)
        * [get_verse_count](#get_verse_count)
    * [Manipulate functions](#manipulate-functions)
        * [separate_token_with_diacritics](#separate_token_with_diacritics)
        * [get_tashkeel_binary](#get_tashkeel_binary)
        * [unpack_alef_mad](#unpack_alef_mad)
        * [shape](#shape)
        * [check_system](#check_system)
        * [check_all_alphabet](#check_all_alphabet)
        * [buckwalter_transliteration](#buckwalter_transliteration)
        * [extract_tashkeel](#extract_tashkeel)
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





# Imporatan information

* Note all verses/chapters/tokens start with **1** not **0**

#### AlphaSystem : 
it's collection of Alphabits that you can apply it on Quran as you need, where you can treat many characters as one character, like:
```python
system = [['أ','آ','إ'],['ت','ب']]
```
here we treat **['أ','آ','إ']** as one character and **['ت','ب']** as another one and the **res characters** every one treat as one, this system applied to all functions in **PyQuran** in Counting,Search,Filltering ...etc. 

the default system used in library treat every character as one , you will find some of **pre-defined** parts of system that you can use it to define your system , import **systems** to use them.

* pre-defined:
    * withoutDotSystem (treat all characters has dot as one)
    * hamazatSystem (treat all characters has hamza as one)

```python
from pyquran import systems
system = [['ت','ب'], systems.hamazatSystem]
```



# Usage

```python
   import PyQuran as pq
```



# Functions


## Access functions:

#### get_sura
**get_sura(chapter_num,with_tashkeil)**
- takes **chapter_num** it's the number of surah and returns **list of chapter verses** and the **with_tashkeil (optional)** is the diacritics option and if **_True_** return chapter with diacritics and if **False** return without and defualt _false_ .

```python
  sura = pq.get_sura(108,True)
  print(sura)

  >>> ['إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ', 'فَصَلِّ لِرَبِّكَ وَانْحَرْ', 'إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ']
```

#### get_verse
**get_verse(chapter_num,verse_num,with_tashkeel)** 
- takes the **chapter_num** , **verse_num** and and it return **verse content** and **with_tashkeil (optional)** is the diacritics option and if **_True_** return verses with diacritics and if **False** return without and defualt _false_.

```python
  ayahText=pq.get_verse(110,1,True)
  print(ayahText)

  >>> إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ
```

#### get_token
**get_token(token_num , verse_num , chapter_num , with_tashkeel)** 
- takes the **token_num** (position Of Token) , **verse_num** , **chapter_num** and it return **token**  and **with_tashkeil (optional)** is the diacritics option and if **_True_** return token with diacritics and if **False** return without and defualt _false_ .


```python
  tokenText = pq.get_token(4,1,114,True)
  print(tokenText)

  >>> النَّاسِ
```

#### get_sura_number
**get_sura_number(chapter_name)**
- takes the name of chapter and return it's number.

```python
  suraNumber = pq.get_sura_number('الملك')
  print(suraNumber)

  >>> 67
```

#### get_sura_name
**get_sura_name(chapter_num)** 
- takes the number of chapter and return it's.

```python
  suraName = pq.get_sura_name(67)
  print(suraName)

  >>> الملك
```

#### get_verse_count
**get_verse_count(chapter)**
- takes **chapter** and return the number of verses.

```python
  numberOfAyat = pd.get_verse_count(pq.get_sura(110,True))
  print(numberOfAyat)

  >>> 3
```


## Manipulate functions:

#### separate_token_with_diacritics

**separate_token_with_diacritics(sentence)**
- takes **sentence** and separate it to characters with there diacritics.

```python
  wordSeparated = pq.separate_token_with_dicrites('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
  print(wordSeparated)

  >>> ['إِ', 'نَّ', 'ا', ' ', 'أَ', 'عْ', 'طَ', 'يْ', 'نَ', 'كَ', ' ', 'ا', 'لْ', 'كَ', 'وْ', 'ثَ', 'رَ']
```

#### get_tashkeel_binary
**get_tashkeel_binary(verse)**
- takes the verses content or chapters with diacritics and it returns tuple of the mapping of **chracters with diacritics** to **0's,1's** and **harakah** represented as **1** and **sukun** represented as **0** and return list of diacritics too.

```python
  pattern = pq.get_tashkeel_binary('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
  print(pattern)

  >>> ('1010 101011 001011', ['ِ', 'ْ', 'َ', '', '', 'َ', 'ْ', 'َ', 'ْ', 'َ', 'َ', '', '', 'ْ', 'َ', 'ْ', 'َ', 'َ'])

```

#### unpack_alef_mad
**unpack_alef_mad(ayahWithAlefMad)**
- takes **ayahWithAlefMad** (sentence that has Alef-Mad) and it returns the sentence after replace **Alef-mad** to **Alef-hamza-above + fatha** and **alef-hamza-above + sukun**.

```python
  unpackAlefMad = pq.unpack_alef_mad('آ')
  print(unpackAlefMad)

  >>> 'أْأَ'
```

#### shape
**shape(system)**
- takes **system** (a new system for alphabets) ,system is "**a list of lists**" that want to treat every "**inner list**" as one character and returns a dictionary has the same value for each set of alphabets and diffirent values for the rest of alphabets , you can see to more details [here](#imporatan-information).

```python
  newSystem = [[pq.beh, pq.teh], [pq.jeem, pq.hah, pq.khah]]
  updatedSystem = pq.shape(newSystem)
  print(updatedSystem)

  >>> {'ب': 0, 'ت': 0, 'ث': 0, 'ج': 1, 'ح': 1, 'خ': 1, 'ء': 2, 'آ': 3, 'أ': 4, 'ؤ': 5, 'إ': 6, 'ئ': 7, 'ا': 8, 'ة': 9, 'د': 10, 'ذ': 11, 'ر': 12, 'ز': 13, 'س': 14, 'ش': 15, 'ص': 16, 'ض': 17, 'ط': 18, 'ظ': 19, 'ع': 20, 'غ': 21, 'ف': 22, 'ق': 23, 'ك': 24, 'ل': 25, 'م': 26, 'ن': 27, 'ه': 28, 'و': 29, 'ى': 30, 'ي': 31, ' ': 70}
```


#### check_all_alphabet
**check_all_alphabet(system)**
- takes **system** and return the rest of default alphabet chracters that doesn't include **system**.

```python
  system = [[pq.beh, pq.teh], [pq.jeem, pq.hah, pq.khah]]
  rest = pq.check_all_alphabet(system)
  print(rest)

  >>> ['ء', 'آ', 'أ', 'ؤ', 'إ', 'ئ', 'ا', 'ة', 'ث', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ى', 'ي']
```


#### check_system
**def check_system(system, indx=None)**
- takes **system** and return main system after apply new system and takes too **index (optional)** that return specific collection from main system.  

```python
  # without index
  system = [[pq.beh, pq.teh], [pq.jeem, pq.hah, pq.khah]]
  rest = pq.check_system(system)
  print(rest)

  >>> [['ب', 'ت'], ['ج', 'ح', 'خ'], ['ء'], ['آ'], ['أ'], ['ؤ'], ['إ'], ['ئ'], ['ا'], ['ة'], ['ث'], ['د'], ['ذ'], ['ر'], ['ز'], ['س'], ['ش'], ['ص'], ['ض'], ['ط'], ['ظ'], ['ع'], ['غ'], ['ف'], ['ق'], ['ك'], ['ل'], ['م'], ['ن'], ['ه'], ['و'], ['ى'], ['ي']]

  
  # with index
  system = [[pq.beh, pq.teh], [pq.jeem, pq.hah, pq.khah]]
  rest = pq.check_system(system,index=1)
  print(rest)
  
  >>> ['ج', 'ح', 'خ']
 ```


#### buckwalter_transliteration
**buckwalter_transliteration(sentence, reverse)**
- takes an **sentence** and **reverse (optional)** the trnslate option if **True** convert **sentence** from Arabic to BuckWalter and if **False (default)** convert **sentence** from BuckWalter to Arabic.

##### note**:the encoding with **diacritics** is  different from **without diacritics**.

```python
  buckwalterEncode = pq.buckwalter_transliteration('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
  print(buckwalterEncode)

  >>> <in~aA >aEoTayonaka Alokawovara
```


#### extract_tashkeel
**extract_tashkeel(sentence)**
- takes an **sentence** and return the tashleel only without charaters.
**Comming soooooon =D .....Taha Magedy Note**




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
  results = search_string_with_tashkeel(sentence,tashkeel_pattern)
  print(results)

  >>> [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)]
```


#### search_with_pattern 
**search_with_pattern(pattern,sentence=None,verseNum=None,chapterNum=None,threshold=0,op=False)**
** comming soon =D ** 


