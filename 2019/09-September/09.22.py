# GOOGLE
"""
    SOLVED 
    You are given an array of tuples (start, end) representing time intervals for lectures.
    The intervals may be overlapping. Return the number of rooms that are required.
    For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""


def end(val):
    return val[1]


def intervalScheduling(pairs):
    # time : O(nlogn)
    # space : O(1)
    n = 0
    l = 0
    pairs.sort(key=end)
    for p in pairs:
        if p[0] >= l:
            l = p[1]
            n += 1
    return n


intervals = [(30, 75), (0, 50), (60, 150)]
print intervalScheduling(intervals)
