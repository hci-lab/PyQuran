

* [FAQ](https://github.com/TahaMagdy/PyQuran/wiki/FAQ) — answers to frequently asked questions


## Documentation
This is suitable for the *PyQuran* users.


##  Development 
This section is for *PyQuran* maintainers.

- ## Project Structure
*PyQuran* is organized as the following:
- **core**: contains main functions/modules.
- **tools**: contains helper functions/modules.
- **testing**: contains unit tests for each module.
- **QuranCorpus**: contains Quran corpus and corpus hashes.


```
.
│   README.md
│   setup.py
|   __init__.py
|       ...
|
└───core
│   │   pyquran.py
│   │      ...   
|
└───tools
|   │   filtering.py
|   |      ...
│   
└───testing
|   │   test_filtering.py
|   |      ...
│   
└───QuranCorpus
    │   quran-uthmani.xml
    |      ...
```
