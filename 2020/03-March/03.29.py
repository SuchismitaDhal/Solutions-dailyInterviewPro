# AIRBNB
"""
    SOLVED -- LEETCODE#50
    The power function calculates x raised to the nth power. 
    If implemented in O(n) it would simply be a for loop over n and multiply x n times. 
    Instead implement this power function in O(log n) time. 
    You can assume that n will be a non-negative integer.
"""


def pow(x, n):
    # Time: O(log n)     Space:O(log n)
    if n == 0:
        return 1
    if n == 1:
        return x

    if n % 2 == 0:
        r = pow(x, n / 2)
        return r * r
    else:
        return x * pow(x, n - 1)


print(pow(5, 3))
# 125
