from tools import getTashkeelPattern
from tools import strip_mark_Al_mad
from pyarabic.araby import name
str ='وآتقين'
str =' ٱلْأَحْيَآءُ'
str = 'بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ هُمْ فِيهَا خَٰلِدُونَ'
pattern = getTashkeelPattern(str)[0]
Tashkeel = getTashkeelPattern(str)[1]
j=0
for i in pattern:
 print(i,name(Tashkeel[j]))
 j=j+1
print(pattern)
print(Tashkeel)


