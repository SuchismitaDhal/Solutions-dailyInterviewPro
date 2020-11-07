# AIRBNB
"""
    SOLVED -- LEETCODE#49
    Given a list of words, group the words that are anagrams of each other.
    (An anagram are words made up of the same letters).
    Example:
    Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
    Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]
"""
import string
char = string.ascii_lowercase

def sortWord(word):
    freq = [0 for _ in range(26)]
    for c in word:
        freq[ord(c) - ord('a')] += 1

    asc = []
    for i in range(26):
        for _ in range(freq[i]):
            asc.append(char[i])
    return ''.join(asc)

def groupAnagramWords(strs):
    # Time: O(n)    Space: O(m + n)
    # n: number of strings      m: maximum length of string
    groups = dict()
    for i in range(len(strs)):
        key = sortWord(strs[i])
        if key in groups:
            groups[key].append(i)
        else:
            groups[key] = [i]

    sol = []
    for idxs in groups.values():
        group = []
        for i in idxs:
            group.append(strs[i])
        sol.append(group)
    return sol

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
