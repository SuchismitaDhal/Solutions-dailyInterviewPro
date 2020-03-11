# LINKEDIN
"""
    SOLVED -- LEETCODE#973
    Given a list of points as a tuple (x, y) and an integer k, find the k closest
    points to the origin (0, 0).
"""
import heapq


def closest_points(points, k):
    # Time: O(n + klogn)  Space: O(n)
    # Optimisation: https://www.youtube.com/watch?v=1rEUgAG7f_c
    #     Time:  O(n) since k closest points can be returned in any order
    #     Space: O(k)
    #     maintain a maxheap of size k
    #     create maxheap by negeting key

    pq = []
    sol = []
    for t in points:
        d = t[0]**2 + t[1]**2
        heapq.heappush(pq, (-d, t))
        if len(pq) > k:
            heapq.heappop(pq)

    for i in range(k):
        p = heapq.heappop(pq)[1]  # O(logn)
        sol.append(p)
    return sol


print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]
