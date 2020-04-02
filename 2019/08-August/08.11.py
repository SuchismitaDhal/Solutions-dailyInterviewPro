# UBER
"""
    SOLVED
    Given a list of numbers, find if there exists a pythagorean triplet in that list. 
    A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2
    Example:
    Input: [3, 5, 12, 5, 13]
    Output: True
    Here, 5^2 + 12^2 = 13^2.
"""


def findPythagoreanTriplets(nums):
    # Time: O(n*n)   Space: O(n)
    # statergy: square; 3sum
    Set = set()
    for i in range(len(nums)):
        nums[i] *= nums[i]
        Set.add(nums[i])

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum = nums[i] + nums[j]
            if sum in Set:
                return True

    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True
