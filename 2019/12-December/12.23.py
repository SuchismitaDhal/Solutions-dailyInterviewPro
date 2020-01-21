# TWITTER
"""
    SOLVED -- LEETCODE#438
    Given 2 strings s and t, find and return all indexes in string s where t is an anagram.
"""


def find_anagrams(s, t):
    # Time: O(n)     Space: O(m)
    n = len(s)
    m = len(t)
    sol = list()

    org = dict()
    curr = dict()
    # build dict and init req
    for c in t:
        if c not in org:
            org[c] = 1
        else:
            org[c] += 1

    r = 0
    # compute for first window
    for i in range(m):
        c = s[i]
        if c in org:
            if c not in curr:
                curr[c] = 1
            else:
                curr[c] += 1
            if curr[c] <= org[c]:
                r += 1

    # slide window
    for j in range(m, n):
        i = j - m
        if r == m:
            sol.append(i)

        p = s[i]
        if p in org:
            curr[p] -= 1
            if curr[p] < org[p]:
                r -= 1

        q = s[j]
        if q in org:
            if q not in curr:
                curr[q] = 1
            else:
                curr[q] += 1
            if curr[q] <= org[q]:
                r += 1

    if r == m:
        sol.append(n-m)
    return sol


print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
