# FACEBOOK
"""
    SOLVED -- LEETCODE#557
    Given a string, you need to reverse the order of characters in each word within a sentence
    while still preserving whitespace and initial word order.
    Example 1:
    Input: "The cat in the hat"
    Output: "ehT tac ni eht tah"
    Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, str):
        # Time: O(n)    Space: O(1)
        if len(str) < 2:
            return str

        ph = [c for c in str]
        f, s = -1, 0
        while f < len(ph):
            if s == len(ph) or ph[s] == ' ':
                i, j = f + 1, s - 1
                while i < j:
                    ph[i], ph[j] = ph[j], ph[i]
                    i, j = i + 1, j - 1
                f = s
            s += 1

        return ''.join(ph)


print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah
