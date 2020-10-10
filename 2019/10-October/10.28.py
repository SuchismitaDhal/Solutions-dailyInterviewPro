# TWITTER
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    Given an array of integers of size n, where all elements are between 1 and n inclusive, 
    find all of the elements of [1, n] that do not appear in the array. 
    Some numbers may appear more than once.
    Example:
    Input: [4,5,2,6,8,2,1,5]
    Output: [3,7]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Time: O(n)   Space: O(n)
        n = len(nums)
        sol = []
        hsh = [False for i in range(n)]

        for num in nums:
            hsh[num - 1] = True

        for i in range(n):
            if hsh[i] == False:
                sol.append(i + 1)

        return sol


nums = [4, 6, 2, 6, 7, 2, 1]
print(Solution().findDisappearedNumbers(nums))
# [3, 5]
