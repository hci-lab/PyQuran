PyQuran
=======

PyQuran is a python package, that provides tools for *Quranic Analysis*:

## Features
- fetch Chapeters and Verses.
- search Quran by text tokens and by diacritics patterns.
- buckwalter transliteration, back and forth
- Multiple **alphabetical systems**, *for more details see the [PyQuran Wiki](https://github.com/TahaMagdy/PyQuran/wiki)*



## Install
Pyquran can be installed from PyPI:

    pip install pyquran
or conda:

    conda install pyquran

## Dependencies
- [numpy](http://www.numpy.org/)
- [pyarabic](https://github.com/linuxscout/pyarabic)

## Quran Arabic Corpus

We use **[tanzil](http://tanzil.net/docs/download) Quran Corpus**, (*Uthmanic Version*).
* Text format is `UTF-8`
* Filter Operation *Explain the substituation, add examples and the replaced/removed chars.

## Contributing
Would you like  to contribute to PyQuran development?
Great! Please read more details
at [CONTRIBUTING.md](CONTRIBUTING.md).

See also [How to contribute to PyQuran](fileName.md).

## Citing
not_completed_ (need to disscuss it with the prof.)
Cite _PyQuran_ as the following _BibTeX_ entry.
```latex
@MISC {PyQuran2018,
author             = "Waleed A. Yousef and Umar Mohamed and Ali Osama and Abdullah Ramzy and Taha Magdy and Ali H. Abdelmonim  and Mostafa Alaa",
title              = "PyQuran",
howpublished       = "https://github.com/TahaMagdy/PyQuran",
month              = "feb",
year               = "2018"
}
```


## Communication
ـnot_completed_


## Licence 
not_completed_ (need to disscuss it with the prof.)


## NOTE:
If you are going to run on `Emacs` shell. It *MUST* be configured to use `UTF-8`;
<br /> else you see this
```python
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```
to avoid *emacs configuration* headache, use a terminal that supports `UTF-8` to run the code =]
