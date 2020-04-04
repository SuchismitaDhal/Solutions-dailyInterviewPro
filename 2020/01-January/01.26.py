# GOOGLE
"""
    SOLVED -- LEETCODE#16
    Given a list of numbers and a target number n, 
    find 3 numbers in the list that sums closest to the target number n. 
    There may be multiple ways of creating the sum closest to the target number, 
    you can return any combination in any order.
"""


def closest_3sum(nums, target):
    # Assuming size of nums to be greater than 3
    # Time: O(n*n)  Space: O(n*n)
    t = 0 - target
    sums = dict()

    sums[nums[0] + nums[1]] = [nums[0], nums[1]]
    m = [nums[0] + nums[1] + nums[2] + t, nums[2]]

    for i in range(2, len(nums)):
        for x in sums:
            if abs(x + nums[i] + t) < abs(m[0]):
                m[0] = x + nums[i] + t
                m[1] = nums[i]

        for j in range(0, i):
            if nums[j] + nums[i] not in sums:
                sums[nums[i] + nums[j]] = [nums[i], nums[j]]

    # print(sums)

    sol = []
    sol.append(m[1])
    s = m[0] - t - m[1]
    sol.append(sums[s][0])
    sol.append(sums[s][1])

    return sol


print(closest_3sum([2, 1, -5, 4], -1))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]
