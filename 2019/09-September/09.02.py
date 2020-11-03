# TWITTER
"""
    SOLVED -- LEETCODE#53
    You are given an array of integers.
    Find the maximum sum of all possible contiguous subarrays of the array.

    Example: [34, -50, 42, 14, -5, 86]
    Given this input array, the output should be 137.
    The contiguous subarray with the largest sum is [42, 14, -5, 86].
    Your solution should run in linear time.
"""


def max_subarray_sum(arr):
    # Space: O(n)   Time: O(1)
    if len(arr) == 1:
        return arr[0]
        
    n = len(arr)
    sol = arr[0]
    maxsumtillnow = sol
        
    for i in range(1, n):
        maxsumtillnow = max(maxsumtillnow + arr[i], arr[i])
        sol = max(maxsumtillnow, sol)
        
    return sol


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137

