# MICROSOFT
"""
    Given a string, find the length of the longest substring without repeating characters.
    Can you find a solution in linear time?
"""

# learnt - list initialisation


class Solution:
    def toi(self, c):
        return ord(c) - ord('a')

    def lengthOfLongestSubstring(self, s):
        visited = [-1] * 26
        n = len(s)
        ans = 0
        current = 0

        for i in range(n):
            k = self.toi(s[i])

        return ans


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
