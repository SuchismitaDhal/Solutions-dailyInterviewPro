# AMAZON
"""
    SOLVED -- LEETCODE#405
    Given a non-negative integer n, convert the integer to hexadecimal 
    and return the result as a string. 
    Hexadecimal is a base 16 representation of a number, 
    where the digits are 0123456789ABCDEF. 
    Do not use any builtin base conversion functions like hex.
"""


def to_hex(n):
    # Time: O(logn)    Space: O(1)
    rep = ['0', '1', '2', '3', '4', '5', '6', '7',
           '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    sol = ""

    if n == 0:
        return "0"

    # for negetive numbers
    if n < 0:
        n = n + (1 << 32)

    while n:
        r = n % 16
        sol += rep[r]
        n = n // 16

    return sol[::-1]


print(to_hex(123))
# 7B
