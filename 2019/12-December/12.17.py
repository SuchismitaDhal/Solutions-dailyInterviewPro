# AMAZON
"""
    SOLVED -- LEETCODE#65
    Given a string that may represent a number, determine if it is a number. 
    Here's some of examples of how the number may be presented:
    "123" # Integer
    "12.3" # Floating point
    "-123" # Negative numbers
    "-.3" # Negative floating point
    "1.5e5" # Scientific notation
    Here's some examples of what isn't a proper number:
    "12a" # No letters
    "1 2" # No space between numbers
    "1e1.2" # Exponent can only be an integer (positive or negative or 0)

    Scientific notation requires the first number to be less than 10, however 
    to simplify the solution assume the first number can be greater than 10. 
    Do not parse the string with int() or any other python functions.
"""


def parse_number(s):
   # Time: O(n)  Space: O(1)
    if len(s) == 0:
        return False

    n = len(s)
    i = 0
    while s[i] == ' ':
        i += 1
        if i == n:
            return False
    s = s[i:n]

    n = n-i
    while s[n-1] == ' ':
        n -= 1
    s = s[0:n]

    if s[0] == '+' or s[0] == '-':
        s = s[1:n]

    if len(s) == 0:
        return False
    return ispure(s) or isdec(s) or isexp(s)


def ispure(s: str) -> bool:
    if len(s) == 0:
        return True
    return s.isdigit()


def isdec(s: str) -> bool:
    i = 0
    for c in s:
        if c == '.':
            break
        i += 1

    if i == len(s):
        return False

    l = s[0:i]
    if i != len(s)-1:
        r = s[i+1: len(s)]
    else:
        r = ""
    if len(r) == 0 and len(l) == 0:
        return False
    return ispure(l) and ispure(r)


def isexp(s: str) -> bool:
    i = 0
    for c in s:
        if c == 'e':
            break
        i += 1

    if i == len(s):
        return False

    l = s[0:i]
    r = s[i+1:len(s)]

    if len(r) > 0:
        if r[0] == '+' or r[0] == '-':
            r = r[1:len(r)]
    if len(l) == 0 or len(r) == 0:
        return False
    return (ispure(l) or isdec(l)) and ispure(r)


print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False
