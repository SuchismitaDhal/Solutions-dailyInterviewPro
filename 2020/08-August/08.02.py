# AMAZON
"""
    SOLVED -- LEETCODE#340
    You are given a string s, and an integer k. 
    Return the length of the longest substring in s that contains at most k distinct characters.

    For instance, given the string:
        aabcdefff and k = 3, 
    then the longest substring with 3 distinct characters would be defff. 
    The answer should be 5.
"""


def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0
        
    hash = dict()
    sz = 0
    l = r = 0
    sol = 0
    while r < len(s):
        if sz > k:
            if hash[s[l]] == 1:
                del hash[s[l]]
                sz -= 1
            else:
                hash[s[l]] -= 1
            l += 1
        else:
            sol = max(sol, r - l)
            if s[r] in hash:
                hash[s[r]] += 1
            else:
                hash[s[r]] = 1
                sz += 1
            r += 1
    
    if sz <= k: sol = max(sol, r - l)                    
    return sol

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
