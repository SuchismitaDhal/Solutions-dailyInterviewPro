# MICROSOFT
"""
    SOLVED -- LEETCODE#300
    [OPTIMIZATION]
        https://leetcode.com/problems/longest-increasing-subsequence/discuss/152065/Python-explain-the-O(nlogn)-solution-step-by-step
        https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    You are given an array of integers. 
    Return the length of the longest increasing subsequence 
    (not necessarily contiguous) in the array.

    Example:
    [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    The following input should return 6 
    since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
"""


def findseq(nums):
    # Time: O(n*n)     Space: O(n)
    sol = 1
    maxlen = [1 for _ in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                maxlen[i] = max(maxlen[i], maxlen[j] + 1)
        sol = max(sol, maxlen[i])

    return sol


print(findseq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
