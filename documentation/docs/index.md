# PyQuran: The Python package for Quranic Analysis


PyQuran is a package which provides tools for Quranic Analysis and Arabic texts.


It is still a small package which needs a lot of your effort. We believe that it
is a seed of a fundamental general package for
computations on Quran with Python, even at the most basic level which is simply
retrieving Quran text.

*Before Islam*, Arabic letters  were without  dots—
[*rasm*](https://en.wikipedia.org/wiki/Rasm), which resulted in ambiguty, two or three
letters had the same rasm or form.

Muslims have decided to remove this ambiguity by adding
dots above or below each letter of the ones which share the same rasm. Now each letter has a unique form. By the way,
originally, Quran was written using letters without dots.


To enable researchers to use modern alphabet, old rasm or other, we introduce *alphabetical systems*,
It is a dynamic construction of letters— Alphabetical Systems.




## Quran Corpus
We use [tanzil](http://tanzil.net/docs/download) Quran Corpus (*Uthmani Text*), it is in `UTF-8` encoding. You
can find all unique characters of Uthmanic Corpus
[here](https://hci-lab.github.io/PyQuran-Private/Filtering-Special-Recitation-Symbols/#recitation-symbols).

There are *special recitation symbols* مصطلحات الضبط in the *Uthmani Text*, they are a guide for the reciter
to know the right positions to pause and the rules of tajweed.
We provide an interface to filter those symbols, *on the fly while fetching from the corpus*,
we **DO NOT** change the corpus, NEVER.

[For the full details about filtering *special recitation symbols* مصطلحات
الضبط.](https://hci-lab.github.io/PyQuran-Private/Filtering-Special-Recitation-Symbols/#recitation-symbols)





## Current Features
- [Quran Retrieving.](https://hci-lab.github.io/PyQuran-Private/quran_tools/)
- Advanced Searching, by
  [Text](https://hci-lab.github.io/PyQuran-Private/analysis_tools/#search_sequence)
and [Diacritics](https://hci-lab.github.io/PyQuran-Private/analysis_tools/#search_string_with_tashkeel) Patterns.
- [Buckwalter Transliteration](https://hci-lab.github.io/PyQuran-Private/arabic_tools/#buckwalter_transliteration), back and forth.
- Multiple [Alphabetical Systems](https://hci-lab.github.io/PyQuran-Private/arabic_tools/#alphabetical-systems).
- Words Frequency Table المعجم الترددى للألفاظ .


## PyQuran needs and Upcoming Features.
- Words Frequency Table filtered according to words meaning.
- Morphology analysis of words to their roots.
- Arabic tools for representing Arabic text for AI algorithms and neural
  networks, for more serious Arabic text processing and understanding. Those
  tools should take meaning, diacritics, roots and other morphology aspects in
  account.
- Some PyQuran in-house tools and architecture enhancement will be on GitHub
  Issues for you contributors to make PyQuran professional and easy to use.



## Contributing
To contribute and maintain PyQuran, Please read  [CONTRIBUTING](https://hci-lab.github.io/PyQuran-Private/CONTRIBUTING) section.



## Dependencies
- [numpy](http://www.numpy.org/)
- [pyarabic](https://github.com/linuxscout/pyarabic)


## Install
- From PyPI: `$ pip3 install pyquran`

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
