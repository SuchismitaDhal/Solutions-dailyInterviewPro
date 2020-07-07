# LINKEDIN
"""
    SOLVED -- (simitar) LEETCODE#86
    Given a list of numbers and an integer k, 
    partition/sort the list such that the all numbers less than k occur before k, 
    and all numbers greater than k occur after the number k.
"""


def partition_list(nums, k):
    # Time: O(n)     Space: O(1)
    p = 0
    for i in range(len(nums)):
        if nums[i] < k:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1
    return nums


print(partition_list([2, 2, 2, 5, 2, 2, 2, 2, 5], 3))
# [2, 2, 2, 2, 2, 2, 2, 5, 5]
