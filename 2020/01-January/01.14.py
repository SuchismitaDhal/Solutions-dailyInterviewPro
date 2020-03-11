# FACEBOOK
"""
    SOLVED 
    HINT : https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
    Given a list of meetings that will happen during a day, 
    find the minimum number of meeting rooms that can fit all meetings.
    Each meeting will be represented by a tuple of (start_time, end_time), 
    where both start_time and end_time will be represented by an integer to indicate the time. 
    start_time will be inclusive, and end_time will be exclusive, 
    meaning a meeting of (0, 10) and (10, 20) will only require 1 meeting room.
"""


def comp(p):
    if p[1] == 1:
        return p[0] + 0.5
    return p[0]


def meeting_rooms(meetings):
    # Time : O(nlogn)    Space: O(n)
    sol = 1
    inf = 1

    times = []
    for meeting in meetings:
        times.append((meeting[0], 1))
        times.append((meeting[1], -1))

    times = sorted(times, key=comp)
    h = 0
    sol = 0
    for t in times:
        h += t[1]
        sol = max(sol, h)

    return sol


print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
