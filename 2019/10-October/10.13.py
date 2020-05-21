# APPLE
"""
    SOLVED -- LEETCODE#136
    Given an array of integers, arr, 
    where all numbers occur twice except one number which occurs once, 
    find the number. 
    Your solution should ideally be O(n) time and use constant extra space.
    Example:
    Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
    Output: 7
"""


class Solution(object):
    def findSingle(self, nums):
        # Time: O(n)  Space: O(1)
        sol = 0
        for x in nums:
            sol = sol ^ x
        return sol


nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3
