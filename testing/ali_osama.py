
from pyarabic.araby import strip_tashkeel, strip_tatweel
def separate_token_with_dicrites(token):
    """gets a token with taskeel, and returns a list contains the token characters with their tashkeel.
    Args:
        param1 (int): list contains the token characters with their tashkeel.
    Returns:
         [str]: a list contains the token characters with their tashkeel.
    """
    token_without_tatweel = strip_tatweel(token)
    print(token_without_tatweel)
    hroof_with_tashkeel = []
    for index,i in enumerate(token):
        if((token[index] in (alphabet or alefat or hamzat) )):
            k = index
            harf_with_taskeel =token[index]
            while((k+1) != len(token) and (token[k+1] in (tashkeel or harakat or shortharakat or tanwin ))):
                harf_with_taskeel =harf_with_taskeel+""+token[k+1]
                k = k + 1
            index = k
            hroof_with_tashkeel.append(harf_with_taskeel)
    return hroof_with_tashkeel
