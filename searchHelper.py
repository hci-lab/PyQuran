"""searchHelper: contains helper functions for searching.
"""


def count_spaces_before_index(string, index):
    """counts spaces before a char in string.

    Args: 
        param1 (str): string
        param2 (int): char index inside string
    Returns:
         int: number of spaces before string[index]

    """
    count = 0
    for i in range(index):
        if string[i] == ' ':
            count += 1

    return count
