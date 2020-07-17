# AMAZON
"""
    SOLVED -- LEETCODE#238
    You are given an array of integers. 
    Return an array of the same size where the element at each index 
    is the product of all the elements in the original array except for the element at that index.
    For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
    You cannot use division in this problem.
"""


def products(nums):
    # Time: O(n)     Space: O(1)
    n = len(nums)
    sol = [1] * n
    for i in range(1, n):
        sol[i] = nums[i - 1] * sol[i - 1]

    agg = 1
    for i in range(n - 1, -1, -1):
        sol[i] *= agg
        agg *= nums[i]

    return sol


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
