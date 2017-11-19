## Tanzil (Quran text النص القراني الرقميّ)

[tanzil](http://tanzil.net/docs/download) has a number of *Quran texts* based on scriptting الإملاء
* Text format is `UTF-8`


## Fetch_Quran file
It parses *XML* file.<br />
change the `xml_file_name` variable to the xml quran text file name.

# Quran Texts
1. `quran-uthmani.xml`: is  similar to **Madina Mushaf**.
2. `quran-simple-clean.xml`: without *diacritics*. 
<br /> 

### Diffrences between *Quran texts*:<br />
 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ is `quran-uthmani`<br /> 
 الرحمن الرحيم is `quran-simple`

## NOTE:
If you are going to run on `Emacs` shell. It *MUST* be configured to use 'UTF-8';
<br /> else you see this
```python
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```
to avoid *emacs configuration* headache, use a terminal that supports `UTF-8` to run the code =]
