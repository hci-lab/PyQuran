"""standard error module
"""

def is_int(number, message):
    if type(number) is not int:
        raise ValueError(message)

def is_bool(boolean, message):
    if type(boolean) is not bool:
        raise ValueError(message)

