# TWITTER
"""
    A palindrome is a sequence of characters that reads the same backwards and forwards.
    Given a string, s, 
    find the longest palindromic substring in s.

    Example:
    Input: "banana"
    Output: "anana"

    Input: "million"
    Output: "illi"
"""


class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        l = [1] * n

        for i in range(1, n):
            m = i - l[i - 1] - 1
            if m > 0 and s[i] == s[m]:
                l[i] = l[i - 1] + 2
            else:
                if i >= 2 and s[i] == s[i - 2]:
                    l[i] = 3
                else:
                    if s[i] == s[i - 1]:
                        l[i] = 2
        print(l)

        p = 0
        for i in range(1, n):
            if l[i] > l[p]:
                p = i

        return s[p - l[p] + 1: p + 1]


s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
s = "baaaab"
print(str(Solution().longestPalindrome(s)))
