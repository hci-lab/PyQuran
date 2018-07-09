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


## Alphabetical Systems (Definitions)
[**Rasm**](https://en.wikipedia.org/wiki/Rasm): is any set of letters which are
writtern in the same form, namely; they are indistinguishable in wirtting by
they are distinguished from the context. For example, the letters  ت ث ن ى,
they can be written with only one rasm ىـ, without dots.

**Alphabetical System**: is a set of rasm; dynamically constructed by 
specifying the letters that you will treat them as one rasm. By the way,  the
default Arabic alphabet is a special case of the **Alphabetical System** where
each letter is as one rasm.


**Predefined systems** are stored in `systems` object.

1. **Default**: each letter is treated as a unique rasm.
2. **Without Dots**: by removing the dots some letters will be
    indistinguishable; those letters are treated as one rasm.
    The following example shows the (Without Dots) system as a list of lists;
    where the sublist contains the letters which share the same rasm.
3. **Hamazat**: consider each any letter accompanied by hamaz ء as one rasm.

**NOTE**: You may go further and construct your system by speicying what 
letters you want to treat as one rasm, then you can do some statistical
analysis like, count, variance, average, ...

Example:
```python
q.systems.withoutDots
Out: 
[['ب', 'ت', 'ث', 'ن'], # Rasm 1
 ['ح', 'خ', 'ج'], # Rasm 2
 ['د', 'ذ'], # Rasm 3
 ['ر', 'ز'], # Rasm 4
 ['س', 'ش'], # Rasm 5
 ['ص', 'ض'], # Rasm 6
 ['ط', 'ظ'], # Rasm 7
 ['ع', 'غ'], # Rasm 8
 ['ف', 'ق']] # Rasm 9
```


### Constructing a user-defined system:
```python
system = [[alef_hamza_above, alef],
          [beh, teh]]
```
The previous piece of code means "Treat *alef_hamza_above* and *alef*
as the same one latter, also treat *beh* and *teh* as one letter as well".

The rest of letters can be dynamically constructed using `check_system()`

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

