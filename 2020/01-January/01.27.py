# FACEBOOK
"""
    SOLVED -- LEETCODE#67
    Given two binary numbers represented as strings, 
    return the sum of the two binary numbers as a new binary 
    represented as a string. 
    Do this without converting the whole binary string into an integer.
"""


def toint(c):
    return 1 if c == '1' else 0


def tochar(i):
    return '1' if i == 1 else '0'


def sum_binary(bin1, bin2):
    # Time: O(n)     Space: O(1)
    if len(bin1) > len(bin2):
        bin1 = bin1[::-1]
        bin2 = bin2[::-1]
    else:
        bn = bin1
        bin1 = bin2[::-1]
        bin2 = bn[::-1]

    sol = ""
    c = 0

    for i in range(len(bin1)):
        a = toint(bin1[i])
        b = toint(bin2[i]) if i < len(bin2) else 0

        s = a ^ b ^ c
        c = a & b & (~c) | c & (a | b)
        sol += tochar(s)

    if c == 1:
        sol += '1'

    return sol[::-1]


print(sum_binary("11101", "1011"))
# 101000
