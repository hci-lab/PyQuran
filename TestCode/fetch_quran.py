from xml.etree import ElementTree

xml_file_name = 'quran-simple-clean.xml'

# Parsing xml
quran_tree = ElementTree.parse(xml_file_name)

def get_sura(sura_number):
    """
        Input:
            * parameter 1: the ordered number of sura in The Mushaf.
        Output:
            * returns: list of its ayat [strings]
        NOTES:
            Do not forget that the index of the reunred list
            starts at zero.
    """

    sura_number -= 1
    sura = []
    suras_list = quran_tree.findall('sura')
    ayat = suras_list[sura_number]
    for aya in ayat:
        sura.append(aya.attrib['text'])
     
    return sura


def fetch_aya(sura_number, aya_number):
    """
        Input:
            * parameter 1: the ordered number of sura in The Mushaf.
            * parameter 2: the ordered number of aya.
        Output:
            * returns: aya (string)
    """

    aya_number -= 1
    sura = get_sura(sura_number)

    return sura[aya_number]


def main():
    # testing
#   print(fetch_aya(12, 4))
#   print(fetch_aya(114, 2))
#   print(fetch_aya(17, 78))
#   print(fetch_aya(25, 9))
#   print(fetch_aya(33, 73))
#   print(fetch_aya(33, 1))
#   print(fetch_aya(34, 1))
#   print(fetch_aya(34, 54))
#   print(fetch_aya(1, 1))
#   print(fetch_aya(2, 1))
#   print(fetch_aya(22, 77))
#   print(get_sura(1))
#   print(get_sura(114))
#   print(get_sura(113))
#   print(get_sura(112))
#   print(get_sura(1)[5-1])
#   print(get_sura(2)[100-1])

if __name__ == '__main__':
    main()
