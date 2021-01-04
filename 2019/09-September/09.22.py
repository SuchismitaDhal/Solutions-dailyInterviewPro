# GOOGLE
"""
    SOLVED -- LEETCODE#253
    You are given an array of tuples (start, end) representing time intervals for lectures.
    The intervals may be overlapping. Return the number of rooms that are required.
    For example. [(30, 75), (0, 50), (60, 150)] should return 2.
"""

def intervalScheduling(pairs):
    # Time : O(nlogn)   Space : O(n)
    pings = []
    for s, e in pairs:
        pings.append((s, 1))
        pings.append((e, -1))

    pings.sort()
    sol = rooms = 0
    for t, act in pings:
        rooms += act
        sol = max(sol, rooms)

    return sol

intervals = [(30, 75), (0, 50), (60, 150)]
print(intervalScheduling(intervals))
