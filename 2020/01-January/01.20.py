# APPLE
"""
    SOLVED -- TO BE TESTED
    Given a list of strings, find the list of characters that appear in all strings.
"""


def toBitstring(s):
    bv = 0
    for c in s:
        i = ord(c) - ord('a')
        mask = 1 << i
        bv |= mask
    return bv


def common_characters(strs):
    #Time: O(m*n)
    # m: length of longest string   n: total strings

    sol = []
    r = (1 << 26) - 1

    for s in strs:
        r &= toBitstring(s)

    for i in range(26):
        mask = 1 << i
        mask &= r
        if mask != 0:
            sol.append(chr(ord('a') + i))

    return sol


print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
# assumtion: even if a character appears twice in all the strings,
#            it appears only once in the solution
