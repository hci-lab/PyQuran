PyQuran
=======

PyQuran is a python package, that provides tools for *Quranic Analysis*.


It is still a small package which needs a lot of your effort. But, we think it is a seed of a fundamental general package for
computations on `Quran` with Python, even at the most basic level which simply retrieving Quran text.

*Before Islam*, Arabic letters  were without  dots—
[*rasm*](https://en.wikipedia.org/wiki/Rasm), which resulted in ambiguty, two or three
letters had the same rasm/form/shape/look. 

Muslims have decided to remove this ambiguity by adding
dots above or below each letter of the ones which share the same rasm. Now each letter has a unique form. By the way,
originally, `Quran` was written without dots on the letters.


To enable you to use both modern system for other, we introduce *alphabetical systems*,
It is a dynamic construction of letters.—
[Alphabetical Systems](https://github.com/TahaMagdy/PyQuran/wiki/Alphabetical-Systems).


## Table of Contents
- [Current Features](#current-features)
- [Install](#install)
- [Dependencies](#dependencies)
- [Quran Corpus](#quran-corpus)
- [Contributing](#contributing)
- [Citing](#citing)
- [Communication](#communication)
- [Licence](#licence)



## Current Features
- fetch chapters and verses.
- search Quran by text tokens and by diacritics patterns.
- buckwalter transliteration, back and forth
- Multiple **alphabetical systems**, *for more details see the [PyQuran Wiki](https://github.com/TahaMagdy/PyQuran/wiki)*



## Install
- From _PyPI_: `$ pip install pyquran`
- From Source: `$ python3 setup.py install`


## Dependencies
- [numpy](http://www.numpy.org/)
- [pyarabic](https://github.com/linuxscout/pyarabic)

## Quran Corpus 
We use [tanzil](http://tanzil.net/docs/download) Quran Corpus (*Uthmani Text*), it is in `UTF-8` encoding. You
can find all unique characters of Uthmanic Corpus
[here](https://github.com/TahaMagdy/PyQuran/wiki/Filtering-Special-Recitation-Symbols).

There are *special recitation symbols* مصطلحات الضبط in the *Uthmani Text*, they are a guide for the reciter
to know the right positions to pause and the rules of tajweed.
We provide an interface to filter those symbols, *only the fly while fetching from the corpus*,
we **DO NOT** change the corpus, NEVER.

[For the full details about filtering *special recitation symbols* مصطلحات الضبط.](https://github.com/TahaMagdy/PyQuran/wiki)

## Contributing
To contribute and maintain *PyQuran*, Please read  [CONTRIBUTING.md](CONTRIBUTING.md).

See also [How to contribute to PyQuran](what_can_you_do_to_help_pyquran.md).

## Citing
not_completed_ (need to disscuss it with the prof.)
Cite _PyQuran_ as the following _BibTeX_ entry.
```ruby
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
not_completed_ (need to discuss it with the prof.)
