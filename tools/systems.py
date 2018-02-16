from arabic import *


# Exporting
'''
[['ب', 'ت', 'ث', 'ن'], 
 ['ح', 'خ', 'ج'],
 ['د', 'ذ'],
 ['ر', 'ز'],
 ['س', 'ش'],
 ['ص', 'ض'], 
 ['ط', 'ظ'], 
 ['ع', 'غ'], 
 ['ف', 'ق']]
'''
withoutDotSystem = [behLike]
withoutDotSystem.append(jeemLike)
withoutDotSystem.append(dalLike)
withoutDotSystem.append(rehLike)
withoutDotSystem.append(seenLike)
withoutDotSystem.append(sadLike)
withoutDotSystem.append(tahLike)
withoutDotSystem.append(ainLike)
withoutDotSystem.append(fehLike)

'''
[
['ء', 'ؤ', 'ئ', 'ٔ', 'ٕ', 'إ', 'أ']
]
'''
hamazatSystem = [hamzat]

default = sorted(alphabet)
'''
print(withoutDotSystem)
print(hamazatSystem)
'''
