# MICROSOFT
"""
    READ DISSCUSSIONS -- LEETCODE#18
    Given a list of numbers, and a target number n, find all unique combinations
    of a, b, c, d, such that a + b + c + d = n.
"""


def fourSum(nums, target):
    # Time: O(n^2)   Space: O(n^2)
    n = len(nums)
    t = target
    nums = sorted(nums)
    print(nums)

    sol = list()
    pairsum = dict()

    # building dictionary
    for i in range(n-1):
        for j in range(i+1, n):
            sum = nums[i] + nums[j]
            if sum not in pairsum:
                pairsum[sum] = [(nums[i], nums[j])]
            else:
                pairsum[sum].append((nums[i], nums[j]))

    # traversing all keys
    for s in pairsum:
        r = target - s
        if r in pairsum:
            for pairs in pairsum[s]:
                max = pairs[1]-1
                for pairr in pairsum[r]:
                    if pairr[0] > max:
                        sol.append([pairs[0], pairs[1], pairr[0], pairr[1]])
                        max = pairr[0]
    print(pairsum)
    return sol


print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])
