# TWITTER
"""
    Given a list of numbers and a target number, 
    find all possible unique subsets of the list of numbers that sum up to the target number. 
    The numbers will all be positive numbers.
"""


def sum_combinations(nums, target):
    # Time: O(2^n)  Space: O(n^2)
    # assuming non-zero numbers
    sol = set()
    if target == 0:
        return [[]]
    for i in range(len(nums)):
        if nums[i] <= target:
            suff = sum_combinations(nums[i + 1:], target - nums[i])
            for s in suff:
                s.append(nums[i])
                sol.add(s)

    return sol


print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]
