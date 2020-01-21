# TWITTER
"""
    SOLVED
    You are given an array of integers.
    Find the maximum sum of all possible contiguous subarrays of the array.

    Example: [34, -50, 42, 14, -5, 86]
    Given this input array, the output should be 137.
    The contiguous subarray with the largest sum is [42, 14, -5, 86].
    Your solution should run in linear time.
"""


def max_subarray_sum(arr):
    n = len(arr)
    mxsum = 0
    sum = 0
    r = 0

    # maxsum if starting at 0
    for i in range(n):
        sum += arr[i]
        if (sum > mxsum):
            mxsum = sum
            r = i

    sum = mxsum
    for i in range(r):
        sum -= arr[i]
        if (sum > mxsum):
            mxsum = sum

    return mxsum


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137

"""
    can also be solved with optimization of Kadane’s Algorithm
"""
