# MICROSOFT
"""
    Given a list of numbers, and a target number n, find all unique combinations
    of a, b, c, d, such that a + b + c + d = n.
    // referred : https://www.techiedelight.com/4-sum-problem/
"""


def fourSum(nums, target):
    # Time: O(n^2)   Space: O(n^2)
    n = len(nums)
    t = target
    nums.sort()

    sol = []
    pairsum = dict()

    for i in range(n - 1):
        for j in range(i + 1, n):
            f = 0
            sum = nums[i] + nums[j]
            if sum not in pairsum:
                pairsum[sum] = [(nums[i], nums[j])]
            else:
                for p in pairsum[sum]:
                    if nums[i] == p[0]:
                        f = 1
                        break
                if f == 0:
                    pairsum[sum].append((nums[i], nums[j]))

    # for sum in pairsum:
    #     samesum = pairsum[sum]
    #     for pair in samesum:
    #         req = t - sum
    #         if req in pairsum:
    #             for p in pairsum[req]:
    #                 if i > p[1]:
    #                     sol.append(sorted([i, j, p[0], p[1]]))
    print(pairsum)
    return sol


print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]
print("//////////////////////////////////")
print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]
print("//////////////////////////////////")
print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])
