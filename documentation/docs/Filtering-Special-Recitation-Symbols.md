# Quran Corpus
We use the *Uthmani Text* of Quran from [tanzil](http://tanzil.net/docs/download).<br>
This is the its hashing ```MD5 (quran-uthmani.xml) = 6aae945d556a1b28cfe682c0ea5ab518```.

# Recitation Symbols

Quran is  written in Arabic Alphabet, but the *Quran scholars* have put
some marks to help reciters and readers in pronouncing and give them some guidance like the kind of 
some letters and pause marks.

Those are the unique characters in the corpus.<br>
((Table Unicode | Symbol  | Kind {letter/mark}))


# Filtering Recitation Symbols
While fetching from corpus, we run the following method to remove all
the recitation marks **they are NOT letters**.

The only thing we replace, is the Alef wasl: ٱ, we add Alef: ا instead, because alef wasl and alef are the same
one letter in Arabic, but alef wasl has a mark above it to indicate that it is not pronounced
as a glottal stop in case of continuing, [Read more about Alef Wasl](https://en.wikipedia.org/wiki/Hamza#Hamzat_wa%E1%B9%A3l).


This filtering is done in run time. We **do not** change the corpus at all.

**[source](https://github.com/hci-lab/PyQuran-Private/blob/master/tools/filtering.py#L107:#L134)**

> Also feel free to report any bugs or lingual errors, you are most welcome, just
> open  an [issue](https://github.com/hci-lab/PyQuran/issues).

