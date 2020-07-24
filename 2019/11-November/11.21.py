# MICROSOFT
"""
    SOLVED -- LEETCODE#393
    A UTF-8 character encoding is a variable width character encoding 
    that can vary from 1 to 4 bytes depending on the character. 
    The structure of the encoding is as follows:

    1 byte:  0xxxxxxx
    2 bytes: 110xxxxx 10xxxxxx
    3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
    4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    For more information, you can read up on the Wikipedia Page.
    <https://www.wikiwand.com/en/UTF-8?#/Description>

    Given a list of integers where each integer represents 1 byte, 
    return whether or not the list of integers is a valid UTF-8 encoding.
"""
import math

BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]


def check_util(byte):
    return byte & BYTE_EQUAL[2] == BYTE_MASKS[1]


def utf8_validator(bytes):
    # Time: O(n)   Space: O(1)
    n = len(bytes)
    if bytes[0] & BYTE_MASKS[n] == BYTE_EQUAL[n]:
        for i in range(1, n):
            if not check_util(bytes[i]):
                return False
        return True
    else:
        return False


print(utf8_validator([0b00000000]))
# True
print(utf8_validator([0b00000000, 10000000]))
# False
print(utf8_validator([0b11000000, 10000000]))
# True
print(utf8_validator([197, 130, 1]))
