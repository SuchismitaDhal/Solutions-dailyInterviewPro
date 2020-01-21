# AMAZON
"""
    SOLVED -- LEETCODE#128
    You are given an array of integers. 
    Return the length of the longest consecutive elements sequence in the array.
    For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence
     1, 2, 3, 4, and thus, you should return its length, 4.

     Can you do this in linear time?
"""


def longest_consecutive(nums):
    # time : O(n)     space : O(n)
    hmap = set(nums)
    if len(nums) == 0:
        return 0

    mxl = 1
    for x in nums:
        if (x - 1) not in hmap:
            c = 1
            k = x + 1
            while k in hmap:
                c += 1
                k += 1
            mxl = max(mxl, c)
    return mxl


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
