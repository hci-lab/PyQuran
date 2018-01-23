from pyarabic.araby import strip_tashkeel, strip_tatweel

def separate_token_with_dicrites(token):
    """gets a token(string) with tashkeel, and returns a list of strings,
    each string represents a character with its tashkeel.
    Args:
        token (str): string represents a word or aya or sura
    Returns:
        [str]: a list contains all arabic alphabets with their tashkeel as strings.
    """
    token_without_tatweel = araby.strip_tatweel(token)
    hroof_with_tashkeel = []
    another_characters = [" ","\n"]
    all_characters = list(arabic.alphabet) + list(arabic.alefat) + list(arabic.hamzat) + another_characters
    all_harakat = list(arabic.tashkeel)+ list(arabic.harakat)+list(arabic.shortharakat)+list(arabic.tanwin)
    for index,i in enumerate(token):
        if(token[index] in all_characters):
            k = index
            harf_with_taskeel = token[index]
            while((k+1) != len(token) and token[k+1] in all_harakat):
                harf_with_taskeel =harf_with_taskeel+""+token[k+1]
                k = k + 1
            index = k
            hroof_with_tashkeel.append(harf_with_taskeel)
    return hroof_with_tashkeel
