# GOOGLE
"""
    SOLVED -- LEETCODE#75
    Given a list of numbers with only 3 unique numbers (1, 2, 3), 
    sort the list in O(n) time.
    Example 1:
    Input: [3, 3, 2, 1, 3, 2, 1]
    Output: [1, 1, 2, 2, 3, 3, 3]
    Challenge: Try sorting the list using constant space.
"""


def sortNums(nums):
    # Time: O(n)     Space: O(1)
    sol = []
    bckt = [0, 0, 0]

    for n in nums:
        bckt[n - 1] += 1

    for i in range(3):
        for j in range(bckt[i]):
            sol.append(i + 1)

    return sol


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
