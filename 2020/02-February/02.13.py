# GOOGLE
"""
    SOLVED 
    Given a list of positive numbers, 
    find the largest possible set such that 
    no elements are adjacent numbers of each other.
"""


def maxNonAdjacentSum(nums):
    # assuming more than 2 numbers
    # Time: O(n)  Space: O(1)
    sol = 0
    mtn = nums[0]
    for i in range(2, len(nums)):
        sol = max(sol, nums[i] + mtn)
        mtn = max(mtn, nums[i - 1])
    return sol


print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
