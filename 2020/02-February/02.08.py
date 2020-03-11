# AIRBNB
"""
    SOLVED -- LEETCODE#169
    A majority element is an element that appears more than half the time. 
    Given a list with a majority element, find the majority element.
"""


def majority_element(nums):
    # Time: O(n)     Space: O(n)
    occ = dict()
    for num in nums:
        if num in occ:
            occ[num] += 1
        else:
            occ[num] = 1

    r = len(nums)//2
    for i in occ:
        if occ[i] > r:
            return i
    return None


print(majority_element([3, 5, 3, 3, 2, 4, 3]))
# 3
