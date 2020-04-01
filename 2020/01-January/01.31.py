# MICROSOFT
"""
    SOLVED -- LEETCODE#14
    Given a list of strings, find the longest common prefix between all strings.
"""


def common_prefix(str1, str2):
    n = min(len(str1), len(str2))
    for i in range(n):
        if str1[i] != str2[i]:
            return str1[:i]
    return str1[:n]


def longest_common_prefix(strs):
    # Time: O(nm)   Space: O(m)
    # n is the number of strings, m is length of longest string
    sol = strs[0]

    for i in range(1, len(strs)):
        if sol == "":
            return ""
        sol = common_prefix(sol, strs[i])

    return sol


print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''
