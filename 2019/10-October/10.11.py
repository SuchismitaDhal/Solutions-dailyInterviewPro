# MICROSOFT
"""
    Given a list of numbers of size n, where n is greater than 3, 
    find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.
"""


def find_min_max(nums):
    # uses (1 + 2*(n-2)) comparisions in worst case
    # worst case being when the array is sorted in decreasing order
    if nums[0] < nums[1]:
        min = nums[0]
        max = nums[1]
    else:
        min = num[1]
        max = num[0]

    for i in range(2, len(nums)):
        if nums[i] >= max:
            max = nums[i]
        else:
            if nums[i] < min:
                min = nums[i]

    return (min, max)


print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)
