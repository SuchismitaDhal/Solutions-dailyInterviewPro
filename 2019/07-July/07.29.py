# MICROSOFT
"""
    SOLVED -- LEETCODE#3
    Given a string, find the length of the longest substring without repeating characters.
    Can you find a solution in linear time?
"""


class Solution:
    def toi(self, c):
        return ord(c) - ord('a')

    def lengthOfLongestSubstring(self, s):
        # Time: O(n) each character is traversed at most twice
        # Space: O(1)
        v = [-1] * 26
        n = len(s)
        i = 0
        j = 0
        l = -1

        while j < n:
            k = self.toi(s[j])
            if v[k] == -1:  # expand window
                v[k] = j
                j += 1

            else:  # move window
                l = max(l, v[k])
                while i <= l and j < n:
                    # move left
                    k = self.toi(s[i])
                    if v[k] == i:
                        v[k] = -1
                    i += 1
                    # move right
                    k = self.toi(s[j])
                    if v[k] != -1:
                        l = max(l, v[k])
                    v[k] = j
                    j += 1

        return j - i


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
w = "dvdf"
print(Solution().lengthOfLongestSubstring(w))
