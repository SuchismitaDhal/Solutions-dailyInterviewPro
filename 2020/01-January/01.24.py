# UBER
"""
    SOLVED -- LEETCODE#821
    Given a string s and a character c, find the distance for all 
    characters in the string to the character c in the string s. 
    You can assume that the character c will appear at least once in the string.
"""
import math


def shortest_dist(s, c):
    # Time: O(n)     //no element is visited more than twice
    #Space: O(1)
    n = len(s)
    dist = [n for i in range(n)]

    locc = -1
    for i in range(n):
        if s[i] == c:
            occ = i
            dist[i] = 0
            if locc == -1:
                for j in range(occ):
                    dist[j] = i - j
                locc = occ
            else:
                st = math.ceil((occ + locc) / 2)
                for j in range(st, occ):
                    dist[j] = i - j
                locc = occ
        else:
            if locc != -1:
                dist[i] = dist[i-1] + 1

    return dist


print(shortest_dist('helloworld', 'l'))
# [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]
