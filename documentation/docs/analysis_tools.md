### count_shape


```python
count_shape(text, system=None)
```



count_shape parses the text  and returns a N*P matrix (ndarray),

the number of rows equals to the number of verses ,
and the number of columns equals to the number of shapes.

What it does:
count the occuerence of each shape in text, depends on the your system ,
If you don't pass system, then it will count each char as one shape.

If `A` is a ndarray,
then A[i,j] is the number of occurrences of alphabet(s)[j] in the
verse i.

 
- __Args__:
param1 ([str] ): a list of strings , each inner list is ayah .
param2([[char]]) : it's optional ,
		-a list of list , each iner list has alphabets that will count as one shape
		- If you don't pass your system, then it will count each char as one shape
 
- __Returns__:
 
- __ndarray__: with dimensions (N * P), where
`N` is the number of verses in chapter and
`P` the number of elements in system + the number of alphapets as on char [alphabets in system excluded]


----

### count_token


```python
count_token(text)
```



 count_token get a text (surah or ayah) and count the
 number of tokens that it has.

 What it does: count the number of tokens in text

  
- __Args__:
 param1 (str or [str]): a string or list of strings

  
- __Returns__:
 
- __int__: the number of tokens

----

### frequency_of_character


```python
frequency_of_character(characters, verse=None, chapterNum=0, verseNum=0, with_tashkeel=False)
```



this function count number of characters occurrence,
for specific verse or with chapter or even all Quran ,
note if you don't pass verse and chapterNum he will get all Quran

 
- __Args__:
 verse (str): this verse that you need to
	 count it and default is None.
 chapterNum (int) : chapter number is a number of 'sura'
		  that will count it , and default is 0
 verseNum (int) : verse number in sura
 chracters (list) : list of characters that you want to count them
 with_tashkeel (boo) : to check if you want to search with tashkeel

 
- __Returns__:
 {dic} : a dictionary and keys is a characters
	 and value is count of every chracter.

----

### generate_frequency_dictionary


```python
generate_frequency_dictionary(suraNumber=None)
```


It takes and ordered number of a sura, and returns the dictionary:
   * key is the word.  value is its frequency in the Sura.
   - If you don't pass any parameter, then the entire Quran is targeted.
   - This function have to work on the Quran with تشكيل, because it's an..
 important factor.

 
- __Args__:
suraNumber (int): it's optional

 
- __Returns__:
 
- __dict__: {str: int}

----

### sort_dictionary_by_similarity


```python
sort_dictionary_by_similarity(frequency_dictionary, threshold=0.8)
```


this function using to cluster words using similarity
   and sort every bunch of word  by most common and sort bunches
   descending in same time


- __Args__:
  frequency_dictionary (dict): frequency dictionary that need to sort

- __Returns__:
  dict : sorted dictionary

----

### check_sura_with_frequency


```python
check_sura_with_frequency(sura_num, freq_dec)
```


this function check if frequency dictionary of specific sura is
compatible with original sura in shapes count

 
- __Args__:
suraNumber (int): sura number

 
- __Returns__:
 
- __Boolean__: True :- if compatible
	 Flase :- if not

----

### search_sequence


```python
search_sequence(sequancesList, verse=None, chapterNum=0, verseNum=0, mode=3)
```



take list of sequances and return matched sequance,
it search in verse ot chapter or All Quran ,
it return for every match :
1- matched sequance
2- chapter number of occurrence
3- token number if word and 0 if sentence

Note :
 *if found verse != None it will use it en search .

 *if no verse and found chapterNum and verseNum it will
  use this verse and use it to search.

 *if no verse and no verseNum and found chapterNum it will
  search in chapter.

 *if no verse and no chapterNum and no verseNum it will
  search in All Quran.

it has many modes:
1- search with decorated sequance (with tashkeel),
   and return matched sequance with decorates (with tashkil).

2- search without decorated sequance (without tashkeel),
   and return matched sequance without decorates (without tashkil).

3- search without decorated sequance (without tashkeel),
   and return matched sequance with decorates (with tashkil).


 
- __Args__:
chapterNum (int): number of chapter where function search
verseNum (int): number of verse wher function search
sequancesList (list): a list of sequances that you want
		  to match them
mode (int): this mode that you need to use and default mode 3

 
- __Returns__:
dict() :  key is sequances and value is a list of matched_sequance
	  and their positions

----

### search_string_with_tashkeel


```python
search_string_with_tashkeel(string, key)
```



   
- __Args__:
  
- __string__: sentence to search by key
  
- __key__: taskeel pattern

   
- __Return__: (True, text that have that tashkeel pattern)
  (Flase, '')

   
- __Assumption__:
 Searches tashkeel that is exciplitly included in string.


----

### search_with_pattern


```python
search_with_pattern(pattern, sentence=None, verseNum=None, chapterNum=None, threshold=1)
```



   this function use to search in 0's,1's pattern and
   return matched words from sentence pattern
   dependent on the ratio to adopt threshold.


- __Args__:
   pattern (str): 0's,1's pattern that you need to search.
   sentence (str): Arabic string with tashkeel where
		   function will search.
   verseNum (int): number of specific verse where
		   will search.
   chapterNum (int): number of specific chapter
		 where will search.
   threshold (float): threshold of similarity , if 1 it will
		  get the similar exactly, and if not ,it will
		  get dependant on threshold number.


- __Cases__:
   1- if pass sentece only or with another args
  it will search in sentece only.
   2- if not passed sentence and passed verseNum and chapterNum,
  it will search in this verseNum that exist in chapterNum only.
   3- if not passed sentence,verseNum and passed chapterNum only,
  it will search in this specific chapter only


- __Return__:
   [list] : it will return list that have matched word, or
	matched senteces and return empty list if not found.

   Note : it's takes time dependent on your threshold and size of chapter,
  so it's not support to search on All-Quran becouse
  it take very long time more than 11 min.

