# AMAZON
"""
    SOLVED -- LEETCODE#340
    [VALIDATED] https://leetcode.com/discuss/interview-question/332807/Uber-or-Phone-screen-or-Longest-substring-with-at-most-K-distinct-characters/304809
    You are given a string s, and an integer k. 
    Return the length of the longest substring in s that contains at most k distinct characters.

    For instance, given the string:
        aabcdefff and k = 3, 
    then the longest substring with 3 distinct characters would be defff. 
    The answer should be 5.
"""


def longest_substring_with_k_distinct_characters(s, k):
    hash = dict()
    sz = 0
    l = 0
    for r in range(len(s)):
        if sz > k:
            if hash[s[l]] == 1:
                del hash[s[l]]
                sz -= 1
            else:
                hash[s[l]] -= 1
            l += 1
        if s[r] in hash:
            hash[s[r]] += 1
        else:
            hash[s[r]] = 1
            sz += 1

    return r - l + 1


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
