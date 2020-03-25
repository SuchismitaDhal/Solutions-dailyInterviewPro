# AIRBNB
"""
    SOLVED -- LEETCODE#34
    Given a sorted array, A, with possibly duplicated elements, 
    find the indices of the first and last occurrences of a target element, x. 
    Return -1 if the target is not found.
    Example:
    Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
    Output: [6,8]

    Input: A = [100, 150, 150, 153], target = 150
    Output: [1,2]

    Input: A = [1,2,3,4,5,6,10], target = 9
    Output: [-1, -1]
"""


class Solution:
    def getLeft(self, arr, t, x, y):
        l = y - x + 1
        if l == 0:
            return - 1
        if arr[x] == t:
            return x
        if l == 1:
            return - 1
        if l == 2:
            if arr[y] == t:
                return y
            else:
                return -1

        m = x + (l // 2)

        if arr[m] == t:
            if arr[m - 1] != t:
                return m
            else:
                return self.getLeft(arr, t, x, m - 1)

        if arr[m] < t:
            return self.getLeft(arr, t, m, y)
        else:
            return self.getLeft(arr, t, x, m-1)

    def getRight(self, arr, t, x, y):
        l = y - x + 1
        if l == 0:
            return - 1
        if arr[y] == t:
            return y
        if l == 1:
            return - 1
        if l == 2:
            if arr[x] == t:
                return x
            else:
                return - 1

        m = x + (l // 2)

        if arr[m] == t:
            if arr[m + 1] != t:
                return m
            else:
                return self.getRight(arr, t, m + 1, y)

        if arr[m] < t:
            return self.getRight(arr, t, m + 1, y)
        else:
            return self.getRight(arr, t, x, m - 1)

    def getRange(self, arr, target):
        # Time: O(logn)  Space: O(logn) for recursion stack
        n = len(arr)
        return [self.getLeft(arr, target, 0, n-1), self.getRight(arr, target, 0, n-1)]


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
