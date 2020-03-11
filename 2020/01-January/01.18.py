# MICROSOFT
"""
    SOLVED -- LEETCODE#43
    Given two strings which represent non-negative integers, 
    multiply the two numbers and return the product as a string as well. 
    You should assume that the numbers may be sufficiently large such that 
    the built-in integer type will not be able to store the input 
    (Python does have BigNum, but assume it does not exist).
"""


def add(str1, str2):
    # assuming both are reversed,
    # and returning reversed sum
    m = len(str1)
    n = len(str2)

    # str1 has the longer string
    if m < n:
        str1, str2 = str2, str1

    sol = ""
    k = ord('0')

    i = 0
    c = 0
    while i < max(m, n):
        s = int(ord(str1[i]) - k) + c
        if i < min(m, n):
            s += int(ord(str2[i]) - k)
        c = s // 10
        sol += str(s % 10)
        i += 1

    if c > 0:
        sol += str(c)
    return sol


def multiply(str1, str2):
    # Time: O(n*m)   Space: O(n+m)
    str1 = str1[::-1]
    sol = ""
    k = ord('0')

    for x in str2:
        c = 0
        prod = ""
        for y in str1:
            p = int(ord(y) - k) * int(ord(x) - k) + c
            c = p // 10
            prod += str(p % 10)
        if c > 0:
            prod += str(c)
        print("prod : ", prod[::-1])

        if sol == "":
            sol = prod
        else:
            sol = add("0" + sol, prod)
    return sol[::-1]


print(multiply("11", "13"))
# 143
print(multiply("123", "456"))
