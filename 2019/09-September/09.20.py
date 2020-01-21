# AIRBNB
"""
    SOLVED
    Given a list of words, group the words that are anagrams of each other.
    (An anagram are words made up of the same letters).
    Example:
    Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
    Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
"""

import collections


def checkAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    ans = 0
    for i in range(len(s1)):
        ans = ans ^ ord(s1[i]) ^ ord(s2[i])

    if (ans == 0):
        return True
    else:
        return False


def groupAnagramWords(strs):
    # time : O(n^2.k)      n: no. of words    k: no. of letters
    # space : O(n)
    group = []
    ans = []
    n = len(strs)
    for i in range(n):
        if strs[i] != '':
            group.append(strs[i])
            for j in range(i + 1, n):
                if (checkAnagram(strs[i], strs[j])):
                    group.append(strs[j])
                    strs[j] = ''
            ans.append(group)
            group = []
    return ans


print groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg'])
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
