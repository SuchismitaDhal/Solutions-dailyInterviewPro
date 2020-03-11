# FACEBOOK
"""
    SOLVED -- LEETCODE#166
    Given a numerator and a denominator, 
    find what the equivalent decimal representation is as a string. 
    If the decimal representation has recurring digits, 
    then put those digits in brackets (ie 4/3 should be represented by 1.(3) to represent 1.333...). 
    Do not use any built in evaluator functions like python's eval. 
    You can also assume that the denominator will be nonzero.
"""


def frac_to_dec(numerator, denominator):
    # Space: O(denominator) for remainder dictionary
    n = numerator
    d = denominator
    res = ""

    if max(n, d) > 0 and min(n, d) < 0:
        res += "-"
    n = abs(n)
    d = abs(d)
    res += str(n // d)

    if n % d == 0:
        return res

    frac = ""
    rem = dict()
    i = 0
    while n:
        r = n % d
        if r == 0:
            break
        if r in rem:
            # recurring solution
            p = rem[r]
            return res + "." + frac[:p] + "(" + frac[p:] + ")"
        else:
            rem[r] = i
            i += 1
            n = r * 10
            frac += str(n//d)

    return res + "." + frac


print(frac_to_dec(-3, 2))
# -1.5

print(frac_to_dec(4, 3))
# 1.(3)

print(frac_to_dec(1, 6))
# 0.1(6)
