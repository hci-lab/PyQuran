from pyquran import get_tashkeel_binary

from pyarabic.araby import name
#str ='وآتقين'
str =' ٱلْأَحْيَاءُ'
#str = 'بِـَٔايَٰتِنَآ أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ هُمْ فِيهَا خَٰلِدُونَ'
pattern = get_tashkeel_binary(str)[0]
Tashkeel = get_tashkeel_binary(str)[1]
j=0
for i in pattern:
 print(i,name(Tashkeel[j]))
 j=j+1
print(pattern)
print(Tashkeel)


