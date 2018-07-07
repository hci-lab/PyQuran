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
check_system(system, index=None)
```


 Returns the alphabet including treated-as-one letters. If you pass the index as the second optional arguement, it returns the letter of the that index only, not the hole alphabet.


 
__Args__

 
- __system__: [[char]], a list of letters, where each letter to be treated as
one letter are in one sub-list,  see  [Alphabetical Systems](#alphabetical-systems).
 
- __index__: Optional integer, is a index of a letter in the new system.

 
__Returns__

  
- __list__: full sorted system or a specific index.


__Example__

```python
q.check_system([['alef', 'beh']])

>>> [['ء'],
['آ'],
['أ', 'ب'],
['ؤ'],
['إ'],
['ئ'],
['ا'],
['ة'],
['ت'],
['ث'],
['ج'],
['ح'],
['خ'],
['د'],
['ذ'],
['ر'],
['ز'],
['س'],
['ش'],
['ص'],
['ض'],
['ط'],
['ظ'],
['ع'],
['غ'],
['ف'],
['ق'],
['ك'],
['ل'],
['م'],
['ن'],
['ه'],
['و'],
['ى'],
['ي']]
```
The previous example prints each letter as one element in a new alphabet list,
as you can see the two letters alef and beh are considered one letter.

----

### shape


```python
shape(system)
```


shape declare a new system for alphabets ,user pass the alphabets "in a list of list"
   that want to count it as on shape "inner list" and returns a dictionary has the same value
   for each set of alphabets and diffrent values for the rest of alphabets


__Args__


param1 ([[char]]): a list of list of alphabets , each inner list have
		  alphabets that with be count  as one shape .

__Returns__

 
- __dictionary__: with all alphabets, where each char "key"  have a value
value will be equals for alphabets that will be count as oe shape

----

### factor_alef_mad


```python
factor_alef_mad(sentance)
```


It returns the `sentance` having alef_mad factored into alef_hamza and alef_wasel.

 
__Args__

  
- __sentance__: str, a string or list.

 
__Returns__

  
- __str__: sentance having the alef_mad factored

 
__Example__

```python
q.unpack_alef_mad('آ')

>>> 'أْأَ'
```
  
----

### grouping_letter_diacritics


```python
grouping_letter_diacritics(sentance)
```


Grouping each letter with its diacritics.


__Args__

 
- __sentance__: str


__Returns__

 
- __[str]__: a list of _x_, where _x_ is the letter accompanied with its
diacritics.


__Example__

```python
q.separate_token_with_dicrites('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')

>>> ['إِ', 'نَّ', 'ا', ' ', 'أَ', 'عْ', 'طَ', 'يْ', 'نَ', 'كَ', ' ', 'ا', 'لْ', 'كَ', 'وْ', 'ثَ', 'رَ']
```

----

### alphabet_excluding


```python
alphabet_excluding(excludedLetters)
```


returns the alphabet excluding `excludedLetters`.


__Args__

 
- __excludedLetters__: list[Char], letters to be excluded from the alphabet.


__Returns__

 
- __str__: alphabet excluding  `excludedLetters`.


__Example__

```python
 q.alphabet_excluding([q.alef, q.beh, q.qaf, q.teh, q.dal, q.yeh, q.alef_mad])
 >>>
 ['ء',
 'ٔ',
 'أ',
 'ؤ',
 'إ',
 'ئ',
 'ة',
 'ث',
 'ج',
 'ح',
 'خ',
 'ذ',
 'ر',
 'ز',
 'س',
 'ش',
 'ص',
 'ض',
 'ط',
 'ظ',
 'ع',
 'غ',
 'ف',
 'ك',
 'ل',
 'م',
 'ن',
 'ه',
 'و',
 'ى']
```

----

### strip_tashkeel


```python
strip_tashkeel(string)
```


convert any letter in the `listOfLetter` to `letter` in the given text


__Args__

 
- __string__: str, to drop tashkeel from.



__Example__

```python
x = q.quran.get_verse(12, 2, with_tashkeel=True)
x
>>> 'إِنَّا أَنزَلْنَهُ قُرْءَنًا عَرَبِيًّا لَّعَلَّكُمْ تَعْقِلُونَ'

q.strip_tashkeel(x)
>>> 'إنا أنزلنه قرءنا عربيا لعلكم تعقلون'
```



----

### buckwalter_transliteration


```python
buckwalter_transliteration(string, reverse=False)
```


Back and forth Arabic-Bauckwalter transliteration.
  Revise [Buckwalter](https://en.wikipedia.org/wiki/Buckwalter_transliteration)

 
__Args__

  
- __string__: to be transliterated.
  
- __reverse__: Optional boolean. `False` transliterates from Arabic to
 Bauckwalter, `True` transliterates from Bauckwalter to Arabic.

 
__Returns__

  
- __str__: transliterated string.




__Example__

```python
q.buckwalter_transliteration('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')

>>> <in~aA >aEoTayonaka Alokawovara
```

