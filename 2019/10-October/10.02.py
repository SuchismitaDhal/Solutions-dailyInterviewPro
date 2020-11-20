# TWITTER
"""
    SOLVED -- LEETCODE#581
    Given a list of integers, return the bounds of the minimum range that must be sorted
    so that the whole list would be sorted.
    Example:
    Input: [1, 7, 9, 5, 7, 8, 10]
    Output: (1, 5)
    Explanation:
    The numbers between index 1 and 5 are out of order and need to be sorted.
"""


def findRangebrute(nums):
  # Time: O(nlogn)   Space: O(n)
    snum = list(nums)
    # if not type-casted to list, snum acts as a reference
    snum.sort()

    print("nums : ", nums)
    print("snum : ", snum)

    for i in range(len(nums)):
        if nums[i] != snum[i]:
            break

    if (i == len(nums)):
        return len(nums), len(nums)
        # returning n,n if array is sorted

    for j in range(len(nums) - 1, i, -1):
        if nums[j] != snum[j]:
            break
    return (i, j)


def findRange(nums):
    # Time: O(n)    Space: O(1)
    for s in range(len(nums)-1):
        if nums[s] > nums[s+1]:
            break
    s += 1

    if (s == len(nums)):
        return len(nums), len(nums)
        # returning n,n if array is sorted

    for e in range(len(nums) - 1, s, -1):
        if nums[e] < nums[e-1]:
            break
    e -= 1

    max = nums[s]
    min = nums[s]
    for i in range(s, e):
        if nums[i] > max:
            max = nums[i]
        if nums[i] < min:
            min = nums[i]
    print(max, min)
    for i in range(s):
        if nums[i] > min:
            s = i
            break

    for i in range(len(nums) - 1, e+1, -1):
        if nums[i] < max:
            e = i
            break

    return (s, e)


print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)
