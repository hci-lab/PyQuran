# PyQuran: The Python package for Quranic Analysis


PyQuran is a package which provides tools for *Quranic Analysis*.


It is still a small package which needs a lot of your effort. We believe that it
is a seed of a fundamental general package for
computations on `Quran` with Python, even at the most basic level which simply retrieving Quran text.

*Before Islam*, Arabic letters  were without  dots—
[*rasm*](https://en.wikipedia.org/wiki/Rasm), which resulted in ambiguty, two or three
letters had the same rasm/form/shape/look. 

Muslims have decided to remove this ambiguity by adding
dots above or below each letter of the ones which share the same rasm. Now each letter has a unique form. By the way,
originally, `Quran` was written without dots on the letters.


To enable you to use both modern system or other, we introduce *alphabetical systems*,
It is a dynamic construction of letters—
[Alphabetical Systems](arabic_tools/#alphabetical-systems).





## Current Features
- fetch chapters and verses.
- search Quran by text tokens and by diacritics patterns.
- buckwalter transliteration, back and forth
- Multiple **alphabetical systems**, *for more details see the [PyQuran Wiki](https://github.com/TahaMagdy/PyQuran/wiki)*



## Install
- From _PyPI_: `$ pip3 install pyquran`
- From Source: `$ python3 setup.py install`


## Dependencies
- [numpy](http://www.numpy.org/)
- [pyarabic](https://github.com/linuxscout/pyarabic)

## Quran Corpus 
We use [tanzil](http://tanzil.net/docs/download) Quran Corpus (*Uthmani Text*), it is in `UTF-8` encoding. You
can find all unique characters of Uthmanic Corpus
[here](https://hci-lab.github.io/PyQuran-Private/Filtering-Special-Recitation-Symbols/#recitation-symbols).

There are *special recitation symbols* مصطلحات الضبط in the *Uthmani Text*, they are a guide for the reciter
to know the right positions to pause and the rules of tajweed.
We provide an interface to filter those symbols, *only the fly while fetching from the corpus*,
we **DO NOT** change the corpus, NEVER.

[For the full details about filtering *special recitation symbols* مصطلحات
الضبط.](https://hci-lab.github.io/PyQuran-Private/Filtering-Special-Recitation-Symbols/#recitation-symbols)

## Contributing
To contribute and maintain *PyQuran*, Please read  [CONTRIBUTING.md](https://hci-lab.github.io/PyQuran-Private/CONTRIBUTING).

## Citing
```
@MISC {PyQuran2018,
author = "Waleed A. Yousef and 
          Taha M. Madbouly and
          Omar M. Ibrahime and
          Ali H. El-Kassas and
          Ali O. Hassan and
          Abdallah R. Albohy",
title = "PyQuran: The Python package for Quranic Analysis",
howpublished = "https://hci-lab.github.io/PyQuran-Private",
year = "2018"}
```


## Communication
[Author Page](https://hci-lab.github.io/PyQuran-Private/authors)

