### count_rasm


```python
count_rasm(text, system=None)
```


counts the occerences of each letter (As `system` defines) in sura.


__Args__

 
- __text__: [str], a list of strings , each inner list is ayah .
 
- __system__: Optional, [[char]], revise [Alphabetical Systems](#alphabetical-systems),
if `system` is not passed, the normal alphabet is applied.


__Returns__

(N * P) ndarray (Matrix A): N is the number of verses, P is the alphabet (as defined in `system`).

`A[i][j]` is the number of the letter `j` in the verse `i`.


__Example__

```python
newSystem = [[q.beh, q.teh, q.theh], [q.jeem, q.hah, q.khah]]
q.count_rasm(q.quran.get_sura(110), newSystem)

>>>[[1 2 1 0 0 0 1 0 4 0 0 1 1 0 0 0 1 0 0 0 0 0 1 0 0 3 0 1 1 1 0 0]
[1 2 0 0 2 0 0 0 5 0 2 0 1 0 1 0 0 0 0 0 0 0 2 0 0 4 0 3 1 3 1 3]
[6 2 0 0 0 0 1 0 4 0 1 0 2 0 2 0 0 0 0 0 0 1 2 0 2 0 1 2 2 2 0 0]]
```

----

### search_string_with_tashkeel


```python
search_string_with_tashkeel(string, key)
```



  
__Args__

  
- __string__: str, sentence to search by key.
  
- __key__: str, taskeel pattern.


  
__Assumption__

 Searches tashkeel that is exciplitly included in string.

  
__Returns__

  
- __find__: list of pairs where x and y are the start and end index of the matched.
  
- __nod-found__: []

  
__Example__

```python
string = 'صِفْ ذَاْ ثَنَاْ كَمْ جَاْدَ شَخْصٌ'
q.search_string_with_tashkeel(string, 'َْ')

>>> [(3, 5), (7, 9), (10, 12), (13, 15), (17, 19)]
```


----

### frequency_of_character


```python
frequency_of_character(characters, verse=None, chapterNum=0, verseNum=0, with_tashkeel=False)
```


counts the number of characters in a specific verse or  sura or even the entrire Quran ,


__Note__

 If verse and chapterNum is not passed, the entire Quran is targeted 


__Args__

  
- __verse__: str, this verse that you need to count it and default is None.
 chapterNum, int, chapter number is a number of 'sura' that will count it , and default is 0.
  
- __verseNum__: int, verse number in sura.
  
- __chracters__: [], list of characters that you want to count them.
  
- __with_tashkeel__: Bool, to check if you want to search with tashkeel.


__Returns__

 {dic} : {str : int} a dictionary and keys is a characters
	 and value is count of every chracter.


__Example__

```python
q.frequency_of_character(['أ',"ب","تُ"],verseNum=2,with_tashkeel=False)
#that will count the vers number **2** in all swar
>>> {'أ': 101, 'ب': 133, 'تُ': 0}

q.frequency_of_character(['أ',"ب","تُ"],chapterNum=1,verseNum=2,with_tashkeel=False)
#that will count the vers number **2** in chapter **1**
>>> {'أ': 0, 'ب': 1, 'تُ': 0}

q.frequency_of_character(['أ',"ب","تُ"],chapterNum=1,verseNum=2,with_tashkeel=False)
#that will count in **all Quran**
>>> {'أ': 8900, 'ب': 11491, 'تُ': 2149}

```

----

### frequency_sura_level


```python
frequency_sura_level(suraNumber)
```


Computes the frequency dictionary for a sura


__Args__

 
- __suraNumber__: 1 <= Int <= 114.

 
- __Return__:
 
- __[aya_frequency_dictionary]__: the key of  `aya_frequency_dictionary` is a
unique word in aya and the corresponding value is its frequency.
A list of frequency dictionaries for each verse of Sura.



__Note__

* frequency dictionary is a python dict, which carries word frequencies
  for an aya.
* Its key is (str) word, its value is (int) word frequency


__Example__


```python
q.frequency_sura_level(suraNumber=1)

>>> [{بسم': 1, 'الله': 1, 'الرحمن': 1, 'الرحيم': 1'},
{الحمد': 1, 'لله': 1, 'رب': 1, 'العلمين': 1'},
{الرحمن': 1, 'الرحيم': 1'},
{ملك': 1, 'يوم': 1, 'الدين': 1'},
{إياك': 1, 'نعبد': 1, 'وإياك': 1, 'نستعين': 1'},
{اهدنا': 1, 'الصرط': 1, 'المستقيم': 1'},
{عليهم': 2',
 صرط': 1',
 الذين': 1',
 أنعمت': 1',
 غير': 1',
 المغضوب': 1',
 ولا': 1',
 الضالين': 1'}]
```

----

### frequency_quran_level


```python
frequency_quran_level()
```


Compute the words frequences of the Quran.


__Returns__

 
- __[sura_level_frequency_dict]__: Revise the output of frequency_sura_level.




----

### sort_dictionary_by_similarity


```python
sort_dictionary_by_similarity(frequency_dictionary, threshold=0.8)
```


this function using to cluster words using similarity
and sort every bunch of word  by most common and sort bunches
descending in same time


__Args__

 
- __frequency_dictionary__: dict, frequency dictionary to be sorted.

__Returns__

dict : {str: int} sorted dictionary


__Example__

```python
frequency_dic = q.generate_frequency_dictionary(114)
q.sort_dictionary_by_similarity(frequency_dic)
# this dictionary is sorted using similarity 0.8
>>> {'أعوذ': 1, 'إذا': 2, 'العقد': 1, 'الفلق': 1, 'النفثت': 1, 'برب': 1, 'حاسد': 1, 'حسد': 1, 'خلق': 1, 'شر': 4, 'غاسق': 1, 'فى': 1, 'قل': 1, 'ما': 1, 'من': 1, 'وقب': 1, 'ومن': 3}
```

----

### check_sura_with_frequency


```python
check_sura_with_frequency(sura_num, freq_dec)
```


this function check if frequency dictionary of specific sura is
compatible with original sura in shapes count


__Args__

suraNumber (int): sura number


__Returns__

 
- __Boolean__: True :- if compatible
	 Flase :- if not

__Example__

```python
frequency_dic = q.generate_frequency_dictionary(114)
q.check_sura_with_frequency(114, frequency_dic)
>>> True
```

----

### search_sequence


```python
search_sequence(sequancesList, verse=None, chapterNum=0, verseNum=0, mode=3)
```


take list of sequances and return matched sequance, it search in verse ot
chapter or All Quran ,

   it return for every match :
   1 - matched sequance
   2 - chapter number of occurrence
   3 - token number if word and 0 if sentence

Note :
 - if found verse != None it will use it en search .

 - if no verse and found chapterNum and verseNum it will
 - use this verse and use it to search.

 - if no verse and no verseNum and found chapterNum it will
 - search in chapter.

 - if no verse and no chapterNum and no verseNum it will
  search in All Quran.

it has many modes:

- search with decorated sequance (with tashkeel),
  and return matched sequance with decorates (with tashkil).

- search without decorated sequance (without tashkeel),
  and return matched sequance without decorates (without tashkil).

- search without decorated sequance (without tashkeel),
   and return matched sequance with decorates (with tashkil).



__Args__

 
- __chapterNum__: int, number of chapter where function search.
 
- __verseNum__: int, number of verse wher function search.
 
- __sequancesList__: [], a list of sequances that you want to match them.
 
- __mode__: int, this mode that you need to use and default mode 3.


__Returns__

 
- __dict__:  key is sequances and value is a list of matched_sequance and their positions.


__Example__

```python
# search in chapter = 1 only using mode 3 (default)
q.search_sequence(sequancesList=['ملك يوم الدين'],chapterNum=1)
#it will return
#{'sequance-1' : [ (matched_sequance , position , vers_num , chapter_num) , (....) ],
# 'sequance-2' : [ (matched_sequance , position , vers_num , chapter_num) , (....) ] }
# Note : position == 0 if sequance is a sentence and == word position if sequance is a word
>>> {'ملك يوم الدين': [('مَلِكِ يَوْمِ الدِّينِ', 0, 4, 1)]}

# search in all Quran using mode 3 (default)
q.search_sequence(sequancesList=['ملك يوم'])
>>> {'ملك يوم': [('مَلِكِ يَوْمِ', 0, 4, 1),  ('الْمُلْكُ يَوْمَ', 0, 73, 6),  ('الْمُلْكُ يَوْمَئِذٍ', 0, 56, 22),  ('الْمُلْكُ يَوْمَئِذٍ', 0, 26, 25)]}
```

