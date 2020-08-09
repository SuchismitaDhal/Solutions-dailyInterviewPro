# GOOGLE
"""
    SOLVED -- LEETCODE#973
    Given a list of points and a number k, 
    find the k closest points to the origin.
"""
import heapq


def dist(p):
    return p[0]*p[0] + p[1]*p[1]


def findClosestPointsOrigin(points, k):
    # Time: O(nlogk)     Space: O(k)
    pq = []
    for p in points:
        heapq.heappush(pq, (-dist(p), p))
        if len(pq) == k + 1:
            heapq.heappop(pq)
    return [p[1] for p in pq]


print(findClosestPointsOrigin([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
# [[-1, -1], [1, 1], [2, 2]]
