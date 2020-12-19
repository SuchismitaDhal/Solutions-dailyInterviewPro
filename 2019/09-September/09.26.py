# AMAZON
"""
    SOLVED -- LEETCODE#349
    Given two arrays, write a function to compute their 
    intersection - the intersection means the numbers that are in both arrays.
    Example 1:
        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
    Example 2:
        Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
        Output: [9,4]

    Note:
    Each element in the result must be unique.
    The result can be in any order.
"""

class Solution:
    def intersection(self, nums1, nums2):
        # Time: O(n + m)    Space: O(n)
        hash = set(nums1)
        sol = []

        for n in nums2:
            if n in hash:
                sol.append(n)
                hash.remove(n)

        return sol

print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))
# [9, 4]