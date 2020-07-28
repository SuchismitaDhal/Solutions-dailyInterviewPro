# AMAZON
"""
    SOLVED -- LEETCODE#442
    Given an array of size n, 
    and all values in the array are in the range 1 to n, 
    find all the duplicates.
"""


class Solution(object):
    def findDuplicates(self, nums):
        # Time: O(n)     Space: O(1)
        for i in range(len(nums)):
            if nums[i] > 0:
                x = nums[i]
                nums[i] = 0
                while nums[x-1] > 0:
                    temp = nums[x - 1]
                    nums[x - 1] = -1
                    x = temp
                nums[x - 1] -= 1

        sol = []
        for i in range(len(nums)):
            if nums[i] < -1:
                sol.append(i + 1)
        return sol


print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
# [2, 3]
