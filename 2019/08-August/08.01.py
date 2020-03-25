# AIRBNB
"""
    SOLVED -- ./2020/03-March/03.17.py
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
    def getRange(self, arr, target):
        # Time: O(logn)     Space: O(1)
        # find first occurance
        l = 0
        r = len(arr) - 1
        while l < r:
            m = int((l + r) / 2)
            if arr[m] < x:
                l = m+1
            else:
                r = m
            # print(f"({l}, {r})")
        s = l

        # find the last occurance
        l = s
        r = len(arr) - 1
        while l < r:
            # print(f"({l}, {r})")
            m = int((l + r) / 2)
            if arr[m] == x:
                l = m+1
            else:
                r = m

        e = r-1

        return [s, e]


arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
