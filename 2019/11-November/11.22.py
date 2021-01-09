# APPLE
"""
    SOLVED -- [SIMILAR] LEETCODE#1064
    A fixed point in a list is where the value is equal to its index. 
    So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list 
    since the index and value is the same. 
    Find a fixed point (there can be many, just return 1) in a sorted list 
    of distinct elements, or return None if it doesn't exist.
    Can you do this in sublinear time?
"""

def find_fixed_point(nums):
    # Time: O(log n)    Space: O(1)
    l = 0
    r = len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] == m:
            return m
        if nums[m] < m:
            l = m+1
        if nums[m] > m:
            r = m

    return None

print(find_fixed_point([-5, 1, 3, 4]))
# 1
