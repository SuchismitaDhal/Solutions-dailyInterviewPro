# AIRBNB
"""
    Given two strings, determine the edit distance between them. 
    The edit distance is defined as the minimum number of edits 
    (insertion, deletion, or substitution) needed to change one string to the other.
    For example, "biting" and "sitting" have an edit distance of 2 
    (substitute b for s, and insert a t).
"""


def distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)


print(distance('biting', 'sitting'))
# 2
