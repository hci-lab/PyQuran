# Retrieving Quran
PyQuran is a set of functions and variables.


```python
import pyquran as q
```


### get_sura
```python
get_sura(sura_number, with_tashkeel=False)
```
Returns a list of verses, where verses are nothing but strings.

**Arguments**

- **sura_number**:   (int)the ordered number of sura in The Mushaf, starting from 1.
- **with_tashkeel**: (bool) to return verses with diacritics to not.


**Example**

```python
q.get_sura(108, True)
Out: ['إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ', 'فَصَلِّ لِرَبِّكَ وَانْحَرْ', 'إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ']
```
---------

### fetch_aya
```python
q.fetch_aya(sura_number, aya_number)
```
Returns a verse.

**Arguments**

- **sura_number**: (int) the ordered number of sura in The Mus'haf.
- **aya_number**:  (int) the ordered number of aya in The Mus'haf.


**Example**

```python
q.fetch_aya(1, 2)
Out: 'الحمد لله رب العلمين'
```

--------
### get_sura_name
```python
q.get_sura_name(suraNumber=None)
```
Returns the Arabic name of a Sura.

**Arguments**

- **suraNumber**:   (int) the ordered number of sura in The Mushaf, starting from 1.


**Example**

```python
q.get_sura_name(2)
Out: 'البقرة'
```
--------


### get_sura_number
```python
q.get_sura_number(suraName)
```
Returns the Arabic name of a Sura.

**Arguments**

- **suraName**:  (str) The Arabic Sura name.


**Example**

```python
pq.get_sura_number('الملك')
>>> 67
```
--------

