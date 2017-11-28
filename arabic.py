"""This module contains Arabic tools for text analysis
"""

# constans.
comma            = u'\u060c'
semicolon        = u'\u061b'
question         = u'\u061f'
hamza            = u'\u0621'
alef_mad       = u'\u0622'
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
zero             = u'\u0660'
one              = u'\u0661'
two              = u'\u0662'
three            = u'\u0663'
four             = u'\u0664'
five             = u'\u0665'
six              = u'\u0666'
seven            = u'\u0667'
eight            = u'\u0668'
nine             = u'\u0669'
percent          = u'\u066a'
decimal          = u'\u066b'
thousands        = u'\u066c'
star             = u'\u066d'
mini_alef        = u'\u0670'
alef_wasla       = u'\u0671'
full_stop        = u'\u06d4'
byte_order_mark  = u'\ufeff'


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
lam_alef_mad_above         = u'\ufef5'
simple_lam_alef              = u'\u0644\u0627'
simple_lam_alef_hamza_above  = u'\u0644\u0623'
simple_lam_alef_hamza_below  = u'\u0644\u0625'
simple_lam_alef_mad_above  = u'\u0644\u0622'

# Lists
alphabet = u''.join([
        alef, 
        beh,
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
        yeh, 
        hamza,   
        alef_mad,  
        alef_hamza_above,  
        waw_hamza,  
        alef_hamza_below,
        yeh_hamza, 
        alef_maksura,  
        teh_marbuta
        ])

tashkeel  = (fathatan,  dammatan,  kasratan, 
            fatha, damma, kasra, 
            sukun, 
            shadda)
harakat  = (  fathatan,    dammatan,    kasratan, 
            fatha,   damma,   kasra, 
            sukun
            )
shortharakat  = ( fatha,   damma,   kasra,  sukun)

tanwin  = (fathatan,   dammatan,    kasratan)

not_def_haraka = tatweel
liguatures = (
            lam_alef, 
            lam_alef_hamza_above, 
            lam_alef_hamza_below, 
            lam_alef_mad_above, 
            )
hamzat = (
            hamza, 
            waw_hamza, 
            yeh_hamza, 
            hamza_above, 
            hamza_below, 
            alef_hamza_below, 
            alef_hamza_above, 
            )
alefat = (
            alef, 
            alef_mad, 
            alef_hamza_above, 
            alef_hamza_below, 
            alef_wasla, 
            alef_maksura, 
            small_alef, 

        )
weak   = ( alef,  waw,  yeh,  alef_maksura)
yehlike =  ( yeh,   yeh_hamza,   alef_maksura,    small_yeh  )

wawlike   = ( waw,   waw_hamza,   small_waw )
tehlike   = ( teh,   teh_marbuta )

small   = ( small_alef,  small_waw,  small_yeh)
moon_letters = (hamza    , 
        alef_mad       , 
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
    )
sun_letters = (
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
    )
alphabetic_order = {
                alef             : 1, 
                beh              : 2, 
                teh              : 3, 
                teh_marbuta      : 3, 
                theh             : 4, 
                jeem             : 5, 
                hah              : 6, 
                khah             : 7, 
                dal              : 8, 
                thal             : 9, 
                reh              : 10, 
                zain             : 11, 
                seen             : 12, 
                sheen            : 13, 
                sad              : 14, 
                dad              : 15, 
                tah              : 16, 
                zah              : 17, 
                ain              : 18, 
                ghain            : 19, 
                feh              : 20, 
                qaf              : 21, 
                kaf              : 22, 
                lam              : 23, 
                meem             : 24, 
                noon             : 25, 
                heh              : 26, 
                waw              : 27, 
                yeh              : 28, 
                hamza            : 29, 
                alef_mad         : 29, 
                alef_hamza_above : 29, 
                waw_hamza        : 29, 
                alef_hamza_below : 29, 
                yeh_hamza        : 29, 
                }


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
    filtered_alphabet = ''
    return [x for x in alphabet if x not in excludedLetters]

