# FACEBOOK
"""
    SOLVED -- LEETCODE#136
    Given a list of numbers, 
    where every number shows up twice except for one number, 
    find that one number.
    Example:
    Input: [4, 3, 2, 4, 1, 3, 2]
    Output: 1
    Challenge: Find a way to do this using O(1) memory.
"""


def singleNumber(nums):
    # Time: O(n)     Space: O(1)
    sol = 0

    for n in nums:
        sol = sol ^ n

    return sol


print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1
