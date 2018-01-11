'''Contains Uthmanic symbols and related functions.
    reference: en.wikipedia.org/wiki/Arabic_script_in_Unicode
'''

'''
    TODO:
        [DONE] add all uthmanic  symbols by unicode, here 
        2 def uthmanic_filter(symbols=[uthmanic]):
            return 'uthmanic free text.'

'''

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


uthmanic = [ hamza_above,
             small_high_meem,
             small_low_meem,
             small_high_seen,
             small_low_seen,
             small_alef,
             small_waw,
             small_yeh,
             small_high_noon,
             mad_lazim_mark,
             tatweel,
             alef_wasl_with_saad_above,
             empty_centre_high_stop,
             small_high_rounded_zero,
             empty_center_low_stop,
             small_high_upright_rectangular_zero,
             rounded_high_stop_with_filled_centre ]


def uthmanic_filter(symbols=uthmanic):
    pass
