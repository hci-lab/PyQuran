PyQuran
=======
PyQuran is a python library providing functionality working on character and word level designed to make analysis on the holy Quran, chapters, verses, and tokens faster and easier.


## Main Features

## Install
Pyquran can be installed from PyPI:
    pip install pyquran
or conda:
    conda install pyquran

## Dependencies
[Python](https://www.python.org/) (>= 3.4)  
[Numpy](http://www.numpy.org/) (>= 1.7.1)  
[Pyarabic](https://github.com/linuxscout/pyarabic)

## Quran Arabic Corpus

We use **[tanzil](http://tanzil.net/docs/download) Quran Corpus**, (*Uthmanic Version*).
* Text format is `UTF-8`
* Filter Operation [Explain -- ????]

## Contributing
Would you like  to contribute to PyQuran development?
Great! Please read more details
at [CONTRIBUTING.md](CONTRIBUTING.md).

See also [How to contribute to PyQuran](fileName.md).


## Citing
If you use PyQuran in your research, please use the following BibTeX entry.

    @MISC {PyQuran2018,
    author             = "Waleed A. Yousef and Umar Mohamed and Ali Osama and Abdullah Ramzy and Taha Magdy and Ali H. Abdelmonim  and Mostafa Alaa",
    title              = "PyQuran",
    howpublished       = "https://github.com/TahaMagdy/PyQuran",
    month              = "feb",
    year               = "2018"
    }


## Communication
* GitHub issues: feature requests, bug reports,  install issues, thoughts, etc.  
* [Gitter channel](https://gitter.im/TahaMagdy/PyQuran): general chat, online discussions, collaboration etc.   
* [Stack Overflow](https://stackoverflow.com/questions/tagged/pyquran):For usage questions, You can ask on Stack Overflow or on [our mailing list](https://groups.google.com/forum/?fromgroups#!forum/blabla)

## NOTE:
If you are going to run on `Emacs` shell. It *MUST* be configured to use `UTF-8`;
<br /> else you see this
```python
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
```
to avoid *emacs configuration* headache, use a terminal that supports `UTF-8` to run the code =]

## License
[Apache License 2.0](https://github.com/TahaMagdy/PyQuran/blob/master/LICENSE)
