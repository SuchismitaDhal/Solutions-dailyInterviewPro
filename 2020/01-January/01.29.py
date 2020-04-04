# AMAZON
"""
    SOLVED -- LEETCODE#7
    Given an integer, reverse the digits. 
    Do not convert the integer into a string and reverse it.
"""


def reverse_integer(num):
    if num < 0:
        ngtv = True
        num = 0 - num
    else:
        ngtv = False

    rev = 0
    while num > 0:
        r = num % 10
        num = num // 10
        rev = rev * 10 + r

    if ngtv:
        return 0 - rev
    else:
        return rev


print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
