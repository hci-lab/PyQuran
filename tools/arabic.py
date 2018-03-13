"""This module contains Arabic tools for text analysis
"""

# Umar; remove this to quran and correct the spelling to `suar_num`
swar_num = 114

# letters.
hamza            = u'\u0621'
hamza_above      = u'\u0654' # 
alef_mad         = u'\u0622'
alef_hamza_above = u'\u0623'
waw_hamza        = u'\u0624'
alef_hamza_below = u'\u0625'
yeh_hamza        = u'\u0626'
alef             = u'\u0627'
beh              = u'\u0628'
teh_marbuta      = u'\u0629'
teh              = u'\u062a'
theh             = u'\u062b'
jeem             = u'\u062c'
hah              = u'\u062d'
khah             = u'\u062e'
dal              = u'\u062f'
thal             = u'\u0630'
reh              = u'\u0631'
zain             = u'\u0632'
seen             = u'\u0633'
sheen            = u'\u0634'
sad              = u'\u0635'
dad              = u'\u0636'
tah              = u'\u0637'
zah              = u'\u0638'
ain              = u'\u0639'
ghain            = u'\u063a'
feh              = u'\u0641'
qaf              = u'\u0642'
kaf              = u'\u0643'
lam              = u'\u0644'
meem             = u'\u0645'
noon             = u'\u0646'
heh              = u'\u0647'
waw              = u'\u0648'
alef_maksura     = u'\u0649'
yeh              = u'\u064a'
madda_above      = u'\u0653'
hamza_above      = u'\u0654'
hamza_below      = u'\u0655'
alef_wasl        = u'\u0671'

tatweel          = u'\u0640'

# diacritics
fathatan         = u'\u064b'
dammatan         = u'\u064c'
kasratan         = u'\u064d'
fatha            = u'\u064e'
damma            = u'\u064f'
kasra            = u'\u0650'
shadda           = u'\u0651'
sukun            = u'\u0652'

# small letters
small_alef       = u"\u0670"
small_waw        = u"\u06e5"
small_yeh        = u"\u06e6"
#ligatures
lam_alef                     = u'\ufefb'
lam_alef_hamza_above         = u'\ufef7'
lam_alef_hamza_below         = u'\ufef9'
lam_alef_mad_above           = u'\ufef5'
simple_lam_alef              = u'\u0644\u0627'
simple_lam_alef_hamza_above  = u'\u0644\u0623'
simple_lam_alef_hamza_below  = u'\u0644\u0625'
simple_lam_alef_mad_above  = u'\u0644\u0622'

# Lists
alphabet = [
        hamza,
        hamza_above,
        alef_mad,   
        alef_hamza_above,  
        waw_hamza,  
        alef_hamza_below,
        yeh_hamza, 
        alef, 
        beh,
        teh_marbuta,
        teh,
        theh,
        jeem,  
        hah,  
        khah, 
        dal,
        thal,
        reh,  
        zain,  
        seen, 
        sheen,  
        sad,  
        dad,  
        tah, 
        zah, 
        ain,
        ghain,  
        feh,  
        qaf,  
        kaf, 
        lam,  
        meem,  
        noon,  
        heh,  
        waw,  
        alef_maksura, 
        yeh
        ]

tashkeel  = [fathatan, dammatan,  kasratan, fatha, damma, kasra, sukun, shadda]
harakat   = [fathatan, dammatan,  kasratan, fatha, damma, kasra, sukun]
shortharakat  = [ fatha,   damma,   kasra,  sukun]
shortharakatWithShadda  = [ fatha,   damma,   kasra,  sukun, shadda]

tanwin  = [fathatan,   dammatan,    kasratan]

not_def_haraka = tatweel
lamAlefLike = [
            lam_alef, 
            lam_alef_hamza_above, 
            lam_alef_hamza_below, 
            lam_alef_mad_above, 
            ]
hamzat = [
            hamza, 
            waw_hamza, 
            yeh_hamza, 
            hamza_above, 
            hamza_below, 
            alef_hamza_below, 
            alef_hamza_above, 
            ]
alefat = [
            alef, 
            alef_mad, 
            alef_hamza_above, 
            alef_hamza_below, 
            alef_wasl, 
            alef_maksura, 
            small_alef, 
        ]
# wihtout dots. Groups
behLike  = [beh, teh, theh, noon]
jeemLike = [hah, khah, jeem]
dalLike  = [dal, thal]
rehLike  = [reh, zain]
seenLike = [seen, sheen]
sadLike  = [sad, dad]
tahLike  = [tah, zah]
ainLike  = [ain, ghain]
fehLike  = [feh, qaf]


weak   = [ alef,  waw,  yeh,  alef_maksura]
yehlike =  [ yeh,   yeh_hamza,   alef_maksura,    small_yeh  ]

wawLike   = [ waw,   waw_hamza,   small_waw ]
tehLike   = [ teh,   teh_marbuta ]

small   = [ small_alef,  small_waw,  small_yeh]
moon_letters = [hamza    , 
        alef_mad         , 
        alef_hamza_above , 
        alef_hamza_below , 
        alef             , 
        beh              , 
        jeem             , 
        hah              , 
        khah             , 
        ain              , 
        ghain            , 
        feh              , 
        qaf              , 
        kaf              , 
        meem             , 
        heh              , 
        waw              , 
        yeh
    ]
sun_letters = [
        teh              , 
        theh             , 
        dal              , 
        thal             , 
        reh              , 
        zain             , 
        seen             , 
        sheen            , 
        sad              , 
        dad              , 
        tah              , 
        zah              , 
        lam              , 
        noon             , 
    ]


# Systems
class Systems:
    '''A container of systems.
    '''
    def __init__(self):
        # 
        self.withoutDots = [behLike,
        jeemLike,
        dalLike,
        rehLike,
        seenLike,
        sadLike,
        tahLike,
        ainLike,
        fehLike]

        # 
        self.hamazat = [hamzat]

        # 
        self.default = alphabet
# END CLASS


# Exporting object
systems = Systems()




"""
    * Some alphabet building tools
"""
def alphabet_excluding(excludedLetters):
    """returns the alphabet excluding the given letters.

    Args:
        excludedLetters (list['char']): letters to be excluded from the alphabet

    Returns:
        str: alphabet excluding the given excludedLetters

    Calling:
        print(alphabet_excluding([alef, beh, qaf, teh]))
        
    """
    return [x for x in alphabet if x not in excludedLetters]


def treat_as_the_same(listOfLetter, letter, text):
    """convert any letter in the `listOfLetter` to `letter` in the given text

    Args:
        listOfLetter (['chars'] or str) 
        letter (char)
        text (str)

    Returns:
        str: a text after changing all the `listOfLetter` to that char `letter`
    
    Example:
        print(treat_as_the_same([alef_hamza_above], alef, line))
        print(treat_as_the_same([ain], qaf, line))
        
        
    """
    pass
