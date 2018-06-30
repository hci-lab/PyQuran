## Alphabets
We use [PyArabic](https://pypi.python.org/pypi/PyArabic/0.6.2) constants which
represents letters, instead of writting Arabic in the code.

```python
hamza            = u'\u0621'
alef_mad         = u'\u0622'
alef_hamza_above = u'\u0623'
waw_hamza        = u'\u0624'
alef_hamza_below = u'\u0625'
yeh_hamza        = u'\u0626'
alef             = u'\u0627'
beh              = u'\u0628'
teh_marbuta      = u'\u0629'
teh              = u'\u062a'
theh             = u'\u062b'
jeem             = u'\u062c'
hah              = u'\u062d'
khah             = u'\u062e'
dal              = u'\u062f'
thal             = u'\u0630'
reh              = u'\u0631'
zain             = u'\u0632'
seen             = u'\u0633'
sheen            = u'\u0634'
sad              = u'\u0635'
dad              = u'\u0636'
tah              = u'\u0637'
zah              = u'\u0638'
ain              = u'\u0639'
ghain            = u'\u063a'
feh              = u'\u0641'
qaf              = u'\u0642'
kaf              = u'\u0643'
lam              = u'\u0644'
meem             = u'\u0645'
noon             = u'\u0646'
heh              = u'\u0647'
waw              = u'\u0648'
alef_maksura     = u'\u0649'
yeh              = u'\u064a'
madda_above      = u'\u0653'
hamza_above      = u'\u0654'
hamza_below      = u'\u0655'
alef_wasl        = u'\u0671'
```


## Alphabetical Systems
We define **alphabetical system** as a dynamic construction of letters in which
you can treat a group of letters one letter. The default alphabet is a special
case of the Alphabetical System where each letter is treated as one letter.

**Predefined systems** are stored in `systems` object.

1. default.
2. without dots system.
3. hamazat.

Example:
```python
q.systems.withoutDots
Out: 
[['ب', 'ت', 'ث', 'ن'],
 ['ح', 'خ', 'ج'],
 ['د', 'ذ'],
 ['ر', 'ز'],
 ['س', 'ش'],
 ['ص', 'ض'],
 ['ط', 'ظ'],
 ['ع', 'غ'],
 ['ف', 'ق']]
```


**Constructing a user-defined system**:
```python
system = [[alef_hamza_above, alef],[beh, teh]]
```
The previous line of code means "Treat *alef_hamza_above* and *alef*
as the same one latter, also treat *beh* and *teh* as one letter as well"

And then, a system can be applied to some text analysis functions like counting,
filtering, etc.




### check_system


```python
check_system(system, indx=None)
```



 check_sytem get a system (list of lists ) and index (it's
 optional) and return full sorted system or a specific index in it.

 -sortion will follow this approach : system in the first with the same
 order , then all remain alphabets sorted alphabetically .

 What it does:
 build a full sorted system and return it or a specific index in it.

  
- __Args__:
 param1 ([[char]] ):  list of lists of characters.
  
- __int__: it's optinal , it will return this index in full sorted system.

  
- __Returns__:
  
- __list__: full sorted system or a spesefic index.

----

### shape


```python
shape(system)
```



	 shape declare a new system for alphabets ,user pass the alphabets "in a list of list"
	 that want to count it as on shape "inner list" and returns a dictionary has the same value
 for each set of alphabets and diffrent values for the rest of alphabets

 
- __Args__:

param1 ([[char]]): a list of list of alphabets , each inner list have
		  alphabets that with be count  as one shape .
 
- __Returns__:
 
- __dictionary__: with all alphabets, where each char "key"  have a value
value will be equals for alphabets that will be count as oe shape

----

### unpack_alef_mad


```python
unpack_alef_mad(ayahWithAlefMad)
```


 unpack_alef_mad is function takes the str or list(ayah or ayat)
 and search about alef mad and unpacks it

 What it does:
 take the Alef mad and converts the alef  mad to alef fataha and alef sukun
  
- __Args__:
 param1 (str): a string or list

  
- __Returns__:
 str : ayah or token with Unpacked mad
  
----

### separate_token_with_dicrites


```python
separate_token_with_dicrites(token)
```



 gets a token with taskeel, and returns a list contains the token characters with their tashkeel.

  
- __Args__:
 param1 (str): strig that will separate it.

  
- __Returns__:
  
- __[str]__: a list contains the token characters with their tashkeel.


----

### alphabet_excluding


```python
alphabet_excluding(excludedLetters)
```


returns the alphabet excluding the given letters.

 
- __Args__:
excludedLetters (list['char']): letters to be excluded from the alphabet

 
- __Returns__:
 
- __str__: alphabet excluding the given excludedLetters

 
- __Calling__:
print(alphabet_excluding([alef, beh, qaf, teh]))


----

### strip_tashkeel


```python
strip_tashkeel(string)
```


convert any letter in the `listOfLetter` to `letter` in the given text

 
- __Args__:
string (str): to drop tashkeel from.


 
- __Example__:



----

### get_tashkeel_binary


```python
get_tashkeel_binary(ayah)
```



 get_tashkeel_pattern is function takes the str or list(ayah or token) and converts to zero and ones

 What it does:
   take token whether ayah or sub ayah and maps it to zero for sukoon and char without diarictics
   and one for char with harakat and tanwin
  
- __Args__:
   param1 (str): a string or list

  
- __Returns__:
   str : zero and ones for each token
  
----

### check_all_alphabet


```python
check_all_alphabet(system)
```



 check_alphabet get a list of alphabets or system(list of lists of alphabets)
 and return the rest of arabic alphabets [alphabets in system excluded]
 -in case sytem equals all arabic alphabets, it will return empty list.

 What it does:
 return the rest of arabic alphabets that not included in system.

  
- __Args__:
 param1 ([char] ): a list or list of lists of characters.

  
- __Returns__:
  
- __list__: include all other arabic alphabet.

----

### buckwalter_transliteration


```python
buckwalter_transliteration(string, reverse=False)
```



 buckwalter_translator get an a Unicode
 tring and transliterate it to Buckwalter encoding or vise verse

 What it does:
 transliterate a Unicode string to buckwalter and vise verse
  
- __Args__:
 param1 (str): a string
 param2 (bool): Boolean , it's an optional
		if it quals to False "False is the defult" ,
		it transliterate from a Unicode string to buckwalter encoding
		and vise verse if it equals to True
  
- __Returns__:
 str : a string, a Unicode or buckwalter

