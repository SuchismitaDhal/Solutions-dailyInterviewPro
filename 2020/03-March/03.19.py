# AMAZON
"""
    SOLVED -- LEETCODE#274
    The h-index is a metric that attempts to measure 
    the productivity and citation impact of the publication of a scholar. 
    The definition of the h-index is if a scholar has at least h of their papers cited h times.
    Given a list of publications of the number of citations a scholar has, 
    find their h-index.
    Example:
    Input: [3, 5, 0, 1, 3]
    Output: 3
    Explanation:
    There are 3 publications with 3 or more citations, hence the h-index is 3.
"""


def hIndex(publications):
    # Time: O(nlogn)     Space: O(1)
    n = len(publications)
    publications.sort()

    for i in range(n):
        if publications[i] >= n - i:
            return n - i
    return 0


print(hIndex([5, 3, 3, 1, 0]))
# 3
