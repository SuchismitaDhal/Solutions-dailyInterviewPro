# FACEBOOK
"""
    NOT SOLVED 
    HINT : https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/
           https://github.com/jiemingxin/LeetCode/blob/master/tutorials/graph/CircularStringChains.java
           
    Two words can be 'chained' if the last character of the first word 
    is the same as the first character of the second word.
    Given a list of words, determine if there is a way to 'chain' 
    all the words in a circle.
    Example:
    Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
    Output: True
    Explanation:
    The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.
"""

from collections import defaultdict


def dfs(curr, visited, edges):
    visited.add(curr)
    pathlen = 1

    for to in edges:
        if to not in visited:
            pathlen = max(pathlen, 1 + dfs(to, visited, edges))

    return pathlen


def chainedWords(words):
    # Time: O(n^2)  Space: O(n)
    edges = defaultdict(list)

    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i][-1] == words[j][0]:
                edges[words[i]].append(words[j])
            if words[j][-1] == words[i][0]:
                edges[words[j]].append(words[i])
    
    maxpathlen = 0
    for word in words:
        maxpathlen = max(maxpathlen, dfs(word, set(), edges))

    return maxpathlen == len(words)


print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
print(chainedWords(['ab', 'bc', 'bd', 'da', 'cb']))
