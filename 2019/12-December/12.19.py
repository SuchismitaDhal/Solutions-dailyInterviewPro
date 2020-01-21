# MICROSOFT
"""
    SOLVED -- LEETCODE#977
    Given a list of sorted numbers (can be both negative or positive),
    return the list of numbers squared in sorted order.
    Solve this problem in O(n) time.
"""


def square_numbers(nums):
    # Time: O(n)    Space: O(1)

    # find first positive number
    p = 0
    n = len(nums)
    for x in nums:
        if x >= 0:
            break
        p += 1

    # traverse in both direction
    i = p - 1
    j = p
    sol = list()

    while i >= 0 or j < n:
        if j == n:
            sol.append(nums[i] * nums[i])
            i -= 1
        else:
            if i == -1:
                sol.append(nums[j] * nums[j])
                j += 1
            else:
                if nums[j] < abs(nums[i]):
                    sol.append(nums[j] * nums[j])
                    j += 1
                else:
                    sol.append(nums[i] * nums[i])
                    i -= 1

    return sol


print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
