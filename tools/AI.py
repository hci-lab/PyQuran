"""Contains encoding tools to apply Machine Learning and Deep Learning algorithms
on Quran and Arabic text generally."""

import arabic


def get_alphabet_tashkeel_combination(tashkeel=arabic.shortharakat):
    ''' Creating Letters with (fatha, damma, kasra, sukun) combinations
    Args:
        tashkeel: Opiotnal, [char], a list of diacritics.

    Example:
    ```python
    for i in get_alphabet_tashkeel_combination():
        print(i)
    for i  in arabic.alphabet:
        print(i)
    print(len(arabic.alphabet))
    print(arabic.alphabet)
    ```
    '''
    arabic_alphabet_tashkeel = []
    for haraka in arabic.shortharakat:
        for letter in arabic.alphabet:
                arabic_alphabet_tashkeel.append(letter + haraka)

    '''
        * Adding alphabets without tashkeel in front of 
          the letters/tashkeel combination
        * [] => alphabet without taskell then alphabet with fatha, ...
    '''
    alphabet = [] + arabic.alphabet
    alphabet += ' '
    arabic_alphabet_tashkeel = [''] + alphabet + arabic_alphabet_tashkeel
        
    return arabic_alphabet_tashkeel


def one_hot(string, padding_length=0):
    '''
        * Optimized for memory use.
        * encodes each letter in string with ont-hot vector
        * returns a list of one-hot vectors a list of (1*182) vectors
        * letter -> 1*182 vector
    '''
    cleanedString = factor_shadda_tanwin(string)
    charCleanedString = separate_token_with_dicrites(cleanedString)

    # Initializing a Matrix
    encodedString = np.zeros( (padding_length, len(lettersTashkeelCombination)) )

    letter = 0
    for char in charCleanedString:
        one_index = lettersTashkeelCombination.index(char)
        # * add 1 for the current letter in one_index
        encodedString[letter][one_index] = 1
        letter +=1

    return encodedString
