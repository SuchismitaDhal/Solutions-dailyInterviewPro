# UBER
"""
    Given a number of integers, combine them so it would create the largest number.
    Example:
    Input:  [17, 7, 2, 45, 72]
    Output:  77245217
"""
import functools

def compare(x, y):
    if len(x) < len(y) and x == y[:len(x)]:
      return -1
    elif len(y) < len(x) and y == x[:len(y)]:
      return 1
    else: 
      if x == y:
        return 0
      return -1 if x > y else 1

def largestNum(nums):
    strs = list(map(str, nums))
    strs.sort(key = functools.cmp_to_key(compare))
    
    sol = 0
    for numstr in strs:
      l = len(numstr)
      sol = sol * (10 ** l) + int(numstr)

    return sol

print(largestNum([17, 7, 2, 45, 72]))
# 77245217
