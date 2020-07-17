# TWITTER
"""
    SOLVED -- LEETCODE#15
    Given an array, nums, of n integers, 
    find all unique triplets (three numbers, a, b, & c) 
    in nums such that a + b + c = 0. 
    Note that there may not be any triplets that sum to zero 
    in nums, and that the triplets must not be duplicates.
    Example:
    Input: nums = [0, -1, 2, -3, 1]
    Output: [0, -1, 1], [2, -3, 1]
"""


class Solution(object):
    def threeSum(self, nums):
        # Time: O(n^2)
        # Space: O(n)
        hash = {}
        n = len(nums)
        nums.sort()
        sol = []

        # build hash
        last = nums[0]
        l = 1
        for i in range(1, n):
            if nums[i] == last:
                l += 1
            else:
                hash[last] = (i - l, l)
                last = nums[i]
                l = 1
        hash[last] = (n - l, l)

        # check for case x + x + x = 0
        if 0 in hash and hash[0][1] >= 3:
            sol.append([0, 0, 0])

        # check for case x + x + y = 0
        last = None
        for i in range(n):
            if nums[i] != last:
                if hash[nums[i]][1] >= 2:
                    if - 2 * nums[i] in hash:
                        sol.append([-2*nums[i], nums[i], nums[i]])
                last = nums[i]

        # check for case x + y + z = 0
        last = None
        for i in range(n):
            if nums[i] != last:
                prev = nums[i]
                for j in range(i + 1, n):
                    if nums[j] != prev:
                        req = -(nums[i] + nums[j])
                        if req > nums[j] and req in hash:
                            sol.append(nums[i], nums[j], req)
                        prev = nums[j]
                last = nums[i]
        return sol


# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]
