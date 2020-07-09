# MICROSOFT
"""
    SOLVED -- LEETCODE#941
    Given an array of heights,
    determine whether the array forms a "mountain" pattern.
    A mountain pattern goes up and then down.
    Like
          /\
         /  \
        /    \
"""


class Solution(object):
    def validMountainArray(self, arr):
        # Time: O(n)     Space: O(1)
        n = len(arr)
        if n < 3:
            return False
        mxfound = False

        for i in range(1, n):
            if mxfound:
                if arr[i] >= arr[i - 1]:
                    return False
            else:
                if arr[i] <= arr[i - 1]:
                    return False
                elif i + 1 < n and arr[i] > arr[i + 1]:
                    mxfound = True

        return mxfound


print(Solution().validMountainArray([1, 2, 3, 2, 1]))
# True

print(Solution().validMountainArray([1, 2, 3]))
# False
