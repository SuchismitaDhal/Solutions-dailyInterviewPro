# APPLE
"""
    Given a sorted array, convert it into a binary search tree.
    Can you do this both recursively and iteratively?
"""
import math


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}, ({self.left}, {self.right})"


class Solution(object):
    def utilrecursive(self, nums):
        if len(nums) == 0:
            return None
        m = len(nums)//2
        root = Node(nums[m])
        root.left = self.utilrecursive(nums[:m])
        root.right = self.utilrecursive(nums[m + 1:])
        return root

    def utiliterative(self, nums):
        if len(nums) == 0:
            return None
        stack = list()

    def sortedArrayToBST(self, nums):
        return self.utilrecursive(nums), self.utiliterative(nums)


n = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])[1]
print(n)
# 0, (-3, (-10, (None, None), None), 9, (5, (None, None), None))
