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
      # Fill this in.
      # idea: reverse the original string and find the longest common contigous subsequence


s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
