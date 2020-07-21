# FACEBOOK
"""
    SOLVED -- LEETCODE#283
    Given an array nums, write a function to move all 0's to the end of it while 
    maintaining the relative order of the non-zero elements.
    Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


class Solution:
    def moveZeros(self, nums):
        p = 0
        while nums[p]:
            p += 1
            if p == len(nums):
                break
        for i in range(p + 1, len(nums)):
            if nums[i]:
                nums[i], nums[p] = nums[p], nums[i]
                i += 1
                p += 1
        return


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
