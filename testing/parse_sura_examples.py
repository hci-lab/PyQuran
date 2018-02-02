from tools import parse_sura

"""
NOTE: 
    * the function returns ndarray, but I print it for testing.
    * DO NOT write Arabic char like this ['د', 'ك']
        becuase the editor will filp them, 
        dal is the first letternnot the letter kaf.
"""

dal = 'د'
meem = 'م'
alifWithoutHamza = 'ا'
baa2 = 'ب'
kaf = 'ك'


# Surat Al-Ekhlaas
# the first column is the letter dal
# the second column is the letter h'aa2 
parse_sura(112, [dal, meem])


# Surat Al-Masad
parse_sura(111, [meem, alifWithoutHamza, baa2])


# Surat Al-Baiina
parse_sura(98, [kaf])
