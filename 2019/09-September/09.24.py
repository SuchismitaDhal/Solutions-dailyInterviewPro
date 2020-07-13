# FACEBOOK
"""
    SOLVED -- LEETCODE#228
    Given a sorted list of numbers, return a list of strings 
    that represent all of the consecutive numbers.
    Example:
    Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
    Output: ['0->2', '5->5', '7->11', '15->15']
    Assume that all numbers will be greater than or equal to 0, 
    and each element can repeat.
"""


def makepair(sp, ep):
    return str(sp) + '->' + str(ep)


def findRanges(nums):
    sol = []
    if len(nums) == 1:
        return [makepair(nums[0], nums[0])]

    sp = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] + 1:
            sol.append(makepair(sp, nums[i - 1]))
            sp = nums[i]

    sol.append(makepair(sp, nums[len(nums) - 1]))
    return sol


print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
