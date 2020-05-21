# TWITTER
"""
    SOLVED -- LEETCODE#34
    Given a sorted list with duplicates, and a target number n, 
    find the range in which the number exists (represented as a tuple (low, high), both inclusive. 
    If the number does not exist in the list, return (-1, -1)).
"""


def lower_limit(nums, t, s, e):
    if e-s < 0 or nums[s] > t:
        return -1
    if nums[s] == t:
        return s

    m = (e + s) // 2
    if nums[m] < t:
        return lower_limit(nums, t, m + 1, e)
    else:
        return lower_limit(nums, t, s+1, m)


def upper_limit(nums, t, s, e):
    if e - s < 0 or nums[e] < t:
        return - 1
    if nums[e] == t:
        return e

    m = (e + s) // 2
    if nums[m] == t:
        return upper_limit(nums, t, m, e-1)
    else:
        return upper_limit(nums, t, s, m-1)


def find_num(nums, target):
    # Time: O(logn)
    # Space: O(logn) can be modified to iteretive solution, which will be O(1)
    ll = lower_limit(nums, target, 0, len(nums) - 1)
    if ll == -1:
        return (-1, -1)
    ul = upper_limit(nums, target, ll, len(nums) - 1)
    return (ll, ul)


print(find_num([1, 1, 3, 5, 7], 1))
# (0, 1)

print(find_num([1, 2, 3, 4], 5))
# (-1, -1)
