## Importing PyQuran
```python
import pyquran as q
```

- Quran retrieving tools are in `q.quran`. 

### get_sura


```python
get_sura(sura_number, with_tashkeel=False, basmalah=False)
```


returns a sura as a list of verses.


__Args__

 
- __sura_number__: 1 <= Integer <= 114, the ordered number of sura in Mushaf.
 
- __with_tashkeel__: Boolean, if true return sura with tashkeel else return
	   without.
 
- __basmalah__: Boolean, adding basmalah as aya.

__Returns__

  
- __[str]__: a list of sura's ayat.


__Note__

Index statrts at zero.
So if the order number of an aya is x, then it's at (x-1) in the returned
list.


__Example__

```python
   q.quran.get_sura(108, with_tashkeel=True)

   >>> ['إِنَّا أَعْطَيْنَكَ الْكَوْثَرَ', 'فَصَلِّ لِرَبِّكَ وَانْحَرْ', 'إِنَّ شَانِئَكَ هُوَ الْأَبْتَرُ']
```

----

### get_verse


```python
get_verse(sura_number, verse_number, with_tashkeel=False)
```



get specific verse form specific chapter


__Args__

 
- __sura_number__: 1 <= Integer <= 114, the ordered number of sura in Mushaf.
 
- __verse_number__: Integer > 0,  number of verse.
 
- __with_tashkeel__: Boolean, if true return sura with tashkeel else return
		   without.


__Returns__

 
- __str__:  a verse.


__Example__

```python
q.quran.get_verse(sura_number=1, verse_number=2)

>>> 'الحمد لله رب العلمين'
```

----

### get_sura_number


```python
get_sura_number(sura_name)
```




__Args__

sura_name (str) : string represents the sura name.

__Returns__

 
- __int__: the sura number which name is sura_name.

__Note__

Do not forget that the index of the returned list starts at zero.
So if the order Sura number is x, then it's at (x-1) in the list.


__Example__

```python
pq.quran.get_sura_number('الملك')

>>> 67
```

----

### get_sura_name


```python
get_sura_name(sura_number=None)
```


Returns the name of `sura_number`. If `sura_number=None` a list of all
sura's names is retunred.


__Args__

 
- __sura_number__: Optional, 1 <= Integer <= 114, the ordered number of sura in Mushaf.


__Returns__

 
- __str__: the sura name which number is sura_number.
 
- __[srt]__: list of all suras' names (if the sura_number parameter is None).


__Example__

```python
q.quran.get_sura_name(2)

>>> 'البقرة'
```

