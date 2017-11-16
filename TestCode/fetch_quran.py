from xml.etree import ElementTree

xml_file_name = 'quran-simple-clean.xml'

# Parsing xml
quran_tree = ElementTree.parse(xml_file_name)

def fetch_aya(sura_number, aya_number):

    sura_number -= 1
    aya_number -= 1

    # Getting `suras` list
    suras_list = quran_tree.findall('sura')

    # Get `ayas` list
    ayas_list = suras_list[sura_number].findall('aya')

    # Elements of a tag are stored in a dictionary
    return ayas_list[aya_number].attrib['text']


def main():
    # testing
    print(fetch_aya(12, 4))
    print(fetch_aya(114, 2))
    print(fetch_aya(17, 78))
    print(fetch_aya(25, 9))
    print(fetch_aya(33, 73))
    print(fetch_aya(33, 1))
    print(fetch_aya(34, 1))
    print(fetch_aya(34, 54))
    print(fetch_aya(1, 1))
    print(fetch_aya(2, 1))
    print(fetch_aya(22, 77))


if __name__ == '__main__':
    main()
