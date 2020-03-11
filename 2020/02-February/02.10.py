# GOOGLE
"""
    SOLVED 
    Given an integer, find the number of 1 bits it has.
"""


def one_bits(num):
    # Time: O(1)     Space: O(1)
    r = 0
    while num:
        r += num % 2
        num = num // 2
    return r


print(one_bits(23))
# 4
# 23 = 0b1011
