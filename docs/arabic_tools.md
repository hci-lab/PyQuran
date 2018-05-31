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


**Construct a user-defined system**:
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
Returns the alphabet including treated-as-one letters. If you pass the index as
the second optional arguement, it returns the letter of the that index only, not the
hole alphabet.

**Arguments**

- **system**:  a list of letters, where each letter to be treated as one letter
  are in one sublist. see [Alphabetical Systems](#alphabetical-systems)
- **index**: (int) is a index of a letter in the new system.


**Example**

This prints each letter as one element in a new alphabet list, as you can see the
two letters *alef* and *beh* are considered one letter.
```python
q.check_system([['alef', 'beh']])
Out: 
[['ء'],
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
--------








### buckwalter_transliteration
Back and forth bauckwalter-arabic transliteration.

**NOTE**: Revise [Buckwalter](https://en.wikipedia.org/wiki/Buckwalter_transliteration)

```python
q.buckwalter_transliteration('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
Out: <in~aA >aEoTayonaka Alokawovara
```



### separate_token_with_diacritics

```python
separate_token_with_diacritics(sentence)
```
Grouping each letter with its diacritics. 

**Argument**

- **sentence**: (str)

**Example**

```python
q.separate_token_with_dicrites('إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ')
Out: ['إِ', 'نَّ', 'ا', ' ', 'أَ', 'عْ', 'طَ', 'يْ', 'نَ', 'كَ', ' ', 'ا', 'لْ', 'كَ', 'وْ', 'ثَ', 'رَ']
```




### unpack_alef_mad
**unpack_alef_mad**
```python
unpack_alef_mad(sentance)
```
Factors alef_mad in a sentance into alef_hamza and alef and returns the sentance.

**Argument**

- **sentance**: (str)



**Example**

```python
q.unpack_alef_mad('آ')
Out: 'أْأَ'
```
