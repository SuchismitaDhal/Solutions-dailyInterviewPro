# MICROSOFT
"""
    SOLVED -- LEETCODE#665
    You are given an array of integers in an arbitrary order. 
    Return whether or not it is possible to make the array non-decreasing 
    by modifying at most 1 element to any value.
    We define an array is non-decreasing if array[i] <= array[i + 1] holds 
    for every i (1 <= i < n).
    Example:
    [13, 4, 7] should return true, 
    since we can modify 13 to any value 4 or less, to make it non-decreasing.

    [13, 4, 1] however, should return false, 
    since there is no way to modify just one element to make the array non-decreasing.
    Can you find a solution in O(n) time?
"""


def check(lst):
    # Time: O(n)     Space: O(1)
    d = 0
    f = 0
    n = len(lst)

    for i in range(n-1):
        if lst[i] > lst[i + 1]:
            d += 1
            if d == 1:
                f = i

    if d == 0:
        return True
    if d > 1:
        return False

    # d = 1
    s = f + 1
    if f == 0 or s == n - 1:
        return True

    return lst[f-1] <= lst[f+1] or lst[s-1] <= lst[s+1]


print(check([13, 4, 7]))
# True
print(check([5, 1, 3, 2, 5]))
# False
