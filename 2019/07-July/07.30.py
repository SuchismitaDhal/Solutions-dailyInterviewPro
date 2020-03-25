# TWITTER
"""
    SOLVED -- LEETCODE#5
    A palindrome is a sequence of characters that reads the same backwards and forwards.
    Given a string, s, 
    find the longest palindromic substring in s.

    Example:
    Input: "banana"
    Output: "anana"

    Input: "million"
    Output: "illi"
"""
import math


class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s
        str = []
        l, r = 0, 0

        for i in range(n - 1):
            str.append(s[i])
            str.append('.')
        str.append(s[n - 1])

        for i in range(1, 2 * n - 2):
            k = 1
            while i - k >= 0 and i + k < 2 * n - 1:
                if str[i - k] == str[i + k]:
                    k += 1
                else:
                    k -= 1
                    break

            k -= 1
            if 2 * k + 1 > r - l + 1:
                r = i + k
                l = i - k

        l = math.ceil(l / 2)
        r = math.floor(r / 2)

        return s[l:r+1]


s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
s = "baaaab"
print(str(Solution().longestPalindrome(s)))
