# LINKEDIN
"""
    SOLVED -- LEETCODE#7
    Write a function that reverses the digits a 32-bit signed integer, x. 
    Assume that the environment can only store integers within the 32-bit signed integer range, 
    [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.
    Example:
    Input: 123
    Output: 321
"""
import math


class Solution:
    def reverse(self, x):
        r = 0
        n = x < 0
        x = abs(x)
        while x:
            r = r * 10 + x % 10
            x = math.floor(x / 10)

        if n:
            r = -r

        if r <= ((2 ** 31) - 1) and r >= ((-2) ** 31):
            return r
        else:
            return 0


print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0
