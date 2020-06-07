# FACEBOOK
""" 
    SOLVED -- LEETCODE#78
    Given a list of unique numbers, 
    generate all possible subsets without duplicates. 
    This includes the empty set as well.
"""


def generateAllSubsets(nums):
    # Time: O(n*2^n)  Space: O(1) no *extra* space
    sol = [[]]
    for num in nums:
        idx = len(sol)
        for i in range(idx):
            new = sol[i] + [num]
            sol.append(new)

    return sol


print(generateAllSubsets([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
