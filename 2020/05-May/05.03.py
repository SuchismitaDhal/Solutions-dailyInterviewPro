# APPLE
"""
    SOLVED -- LEETCODE#75
    Given an array with n objects colored red, white or blue, 
    sort them in-place so that objects of the same color are adjacent, 
    with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    Note: You are not suppose to use the library’s sort function for this problem.
    Can you do this in a single pass?
    Example:
    Input: [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
"""


class Solution:
    def sortColors(self, nums):
        # Time: O(n)    Space: O(1)
        n = len(nums)
        l, r = 0, n - 1
        i = l
        while i <= r:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums[i] = nums[l]
                nums[l] = 0
                l += 1
                i = max(i, l)
            else:
                nums[i] = nums[r]
                nums[r] = 2
                r -= 1
        return nums


nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
