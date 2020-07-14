# GOOGLE
"""
    SOLVED -- LEETCODE#295
    You are given a stream of numbers. 
    Compute the median for each new element.
    Eg. Given [2, 1, 4, 7, 2, 0, 5], 
    the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
"""
import heapq


def checkInvarient(curr, left, right):
    if abs(len(left) - len(right)) <= 1:
        return curr
    if len(left) > len(right):
        heapq.heappush(right, curr)
        return - heapq.heappop(left)

    else:
        heapq.heappush(left, -curr)
        return heapq.heappop(right)


def running_median(stream):
    # Time(for each new element): O(logn)
    # Space: O(n)
    left = []  # maxheap
    right = []  # minheap
    curr = stream[0]
    print(stream[0])

    for i in range(1, len(stream)):
        if stream[i] > curr:
            heapq.heappush(right, stream[i])
        else:
            heapq.heappush(left, -stream[i])
        curr = checkInvarient(curr, left, right)
        if (i+1) % 2 == 1:
            print(curr)
        else:
            if len(left) > len(right):
                print((-left[0] + curr) / 2)
            else:
                print((right[0] + curr)/2)


running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2
