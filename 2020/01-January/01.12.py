# GOOGLE
"""
    SOLVED -- LEETCODE#503 similar
    Given a list of numbers, 
    for each element find the next element that is larger than the current element. 
    Return the answer as a list of indices. 
    If there are no elements larger than the current element, then use -1 instead.
"""


def next(i, nums, sol):
    n = i+1
    while 1:
        if nums[i] < nums[n]:
            sol[i] = n
            return
        if sol[n] == None:
            next(n, nums, sol)

        if sol[n] == -1:
            sol[i] = -1
            return
        n = sol[n]
    return


def larger_number(nums):
    # Time: O(n)     Space: O(n)
    n = len(nums)
    sol = [None] * n

    sol[n-1] = -1
    for i in range(n):
        if sol[i] == None:
            next(i, nums, sol)
    return sol


print(larger_number([3, 2, 5, 6, 9, 8]))
# print [2, 2, 3, 4, -1, -1]
