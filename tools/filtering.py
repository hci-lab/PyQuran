'''Contains Uthmanic symbols and related functions.
    reference: en.wikipedia.org/wiki/Arabic_script_in_Unicode
'''

import arabic
import error
import re

hamza_above     = '\u0654' # u'\u0654'
small_high_meem = '\u06e2'
small_low_meem  = '\u06ed'
small_high_seen = '\u06dc'
small_low_seen  = '\u06e3'
small_alef      = '\u0670'
small_waw       = '\u06e5'
small_yeh       = '\u06e6'
small_high_noon = '\u06e8'
mad_lazim_mark  = '\u0653'
tatweel         = '\u0640'
alef_wasl_with_saad_above   = '\u0671'
empty_centre_high_stop      = '\u06eb'
small_high_rounded_zero     = '\u06df'
empty_center_low_stop       = '\u06ea'
small_high_upright_rectangular_zero  = '\u06e0'
rounded_high_stop_with_filled_centre = '\u06ec'


recitationSymbols = [ 
    alef_wasl_with_saad_above, # Replace with alef
    hamza_above, # Remain
    small_high_meem, # Remove
    small_low_meem, # Remove
    small_high_seen, # Remove
    small_low_seen, # Remove
    small_alef, # Remove
    small_waw, # Remove
    small_yeh, # Remove
    small_high_noon, # Remove
    mad_lazim_mark, # Remove
    tatweel, # Remove
    empty_centre_high_stop, # Remove
    small_high_rounded_zero, # Remove
    empty_center_low_stop, # Remove
    small_high_upright_rectangular_zero, # Remove
    rounded_high_stop_with_filled_centre # Remove
]

'my_user_name'
'''
# Cannot fide hamza_above
import tools
import arabic
x = tools.search_sequence([hamza_above])
print(x)


quran = open('QuranCorpus/quran-uthmani.txt', 'r')
quran = quran.read()
#print(quran)
print(len(quran))
print(hamza_above in quran)
import re
p = re.compile(quran)
print(p.search(hamza_above))
print(p.findall(hamza_above))
'''

"""
    problems;
        * 'ء' is removed from AlNsaa 92  u'\u0621'
        * hamza_above     = '\u0654' # u'\u0654'
        * 1:126 الأخر what is this hamza?! is it أ or alef + hamza above?

    In [1]: u'\u0621'
    Out[1]: 'ء'

    In [2]: '\u0654'
    Out[2]: 'ٔ'
"""

def get_patterns():
    patterns = []
    for x in [small_yeh, small_waw] :
        for y in arabic.shortharakat:
            patterns.append(x + y)

    return patterns + [small_yeh, small_waw]

patterns_list = get_patterns()

remove_no_tashkeel_after = [
        small_high_meem, # Remove
        small_low_meem, # Remove
        small_high_seen, # Remove
        small_low_seen, # Remove
        small_alef, # Remove
        small_high_noon, # Remove
        mad_lazim_mark, # Remove
        tatweel, # Remove
        empty_centre_high_stop, # Remove
        small_high_rounded_zero, # Remove
        empty_center_low_stop, # Remove
        small_high_upright_rectangular_zero, # Remove
        rounded_high_stop_with_filled_centre # Remove
]

def recitation_symbols_filter(string, symbols=recitationSymbols):
    '''Removes the Special Recitation Symbols from `string`
        Args:
            param1(str): a string to be filtered
            param2([char]: a list of recitation symbols

    Issues:
        * Some small litters have diacritics when they are removed
          their diacritics remains.

        * pyarabic strip_tashkeel -> revise it.
    '''
    
    error.is_string(string, 'You must pass an string')

    for symbol in symbols:
        if symbol == alef_wasl_with_saad_above:
            string = string.replace(alef_wasl_with_saad_above, arabic.alef)
        # Do not remove hamza_above
        elif symbol == hamza_above:
            continue
        elif symbol in remove_no_tashkeel_after:
            string = string.replace(symbol, '')
        else:
            for pat in patterns_list:
                string = re.sub( pat , '', string)

    return string

'''
for x in recitationSymbols :
    print("> " + x + '\n')
'''
