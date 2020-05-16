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


def dfs(curr, G, visited, n):
    till = visited[curr]
    sol = False

    if till > n:
        return False

    for rel in G[curr]:
        if visited[rel] == 1 and till == n:
            return True
        visited[rel] = max(visited[rel], till + 1)
        sol = sol or dfs(rel, G, visited, n)

    return sol


def chainedWords(words):
    visited = defaultdict(int)
    G = defaultdict(list)

    n = 0
    for word in words:
        if word[0] != word[-1]:
            n += 1
            G[word[0]].append(word[-1])
    visited[words[0][0]] = 1
    print(G)

    sol = dfs(word[0][0], G, visited, n)
    print(visited)
    return sol


#print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
print(chainedWords(['ab', 'bc', 'bd', 'da', 'cb']))
