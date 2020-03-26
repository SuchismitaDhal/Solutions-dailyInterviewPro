# MICROSOFT
"""
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
    flag = False
    n = len(lst)

    if lst[0] > lst[1]:
        if flag == True:
            return False
        else:
            lst[0] = lst[1]
            flag = True

    for i in range(1, n-1):
        if lst[i] < lst[i - 1]:
            if flag == True:
                return False
            else:
                if lst[i - 1] > lst[i + 1]:
                    return False
                else:
                    flag = True

    if lst[n-2] > lst[n-1]:
        if flag == True:
            return False
        else:
            flag = True

    return True


print(check([13, 4, 7]))
# True
print(check([5, 1, 3, 2, 5]))
# False
