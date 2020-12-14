# MICROSOFT
"""
    SOLVED -- LEETCODE#56
    You are given an array of intervals - that is, an array of tuples (start, end). 
    The array may not be sorted, and could contain overlapping intervals. 
    Return another array where the overlapping intervals are merged.
    For example:
    [(1, 3), (5, 8), (4, 10), (20, 25)]
    This input should return [(1, 3), (4, 10), (20, 25)] 
    since (5, 8) and (4, 10) can be merged into (4, 10).
"""

def merge(intervals):
    # Time: O(nlogn)    Space: O(1)
    merged = []
    intervals.sort()

    currl, currr = intervals[0][0], intervals[0][1]
    for l, r in intervals[1:]:
        if l <= currr:
            currr = max(currr, r)
        else:
            merged.append((currl, currr))
            currl, currr = l, r
    merged.append((currl, currr))

    return merged
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]