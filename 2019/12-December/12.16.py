# FACEBOOK
"""
    SOLVED -- LEETCODE#189
    Given an array and an integer k, rotate the array by k spaces.
    Do this without generating a new array and without using extra space.
"""
import math


def rotate_list(nums, k):
    # Time: O(n)   Space: O(1)
    n = len(nums)
    t = math.gcd(n, k)
    k = k % n

    for j in range(t):
        i = j - k
        if i < 0:
            i = n+i
        temp = nums[j]
        while i != j:
            temp, nums[i] = nums[i], temp
            i = i-k
            if i < 0:
                i = n + i
        nums[j] = temp


a = [1, 2, 3, 4, 5]
rotate_list(a, 2)
print(a)
# [3, 4, 5, 1, 2]
