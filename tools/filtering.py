'''Contains Uthmanic symbols and related functions.
    reference: en.wikipedia.org/wiki/Arabic_script_in_Unicode
'''

import arabic

hamza_above     = '\u0654'
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
    alef_wasl_with_saad_above, # Rplace with alef
    hamza_above, # ???????
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

def recitation_symbols_filter(string, symbols=recitationSymbols ):
    '''Removes the Special Recitation Symbols from `string`
        Args:
            param1(str): a string to be filtered
            param2([char]: a list of recitation symbols
    '''
    for symbol in symbols:
        if symbol == alef_wasl_with_saad_above:
            string = string.replace(alef_wasl_with_saad_above, arabic.alef)
        else:
            string = string.replace(symbol, '')

    return string

'''
for x in recitationSymbols :
    print("> " + x + '\n')
'''
