# LINKEDIN
"""
    SOLVED -- LEETCODE#70
    You are given a positive integer N which represents the number of steps 
    in a staircase. You can either climb 1 or 2 steps at a time. 
    Write a function that returns the number of unique ways to climb the stairs.
    Can you find a solution in O(n) time?
"""


def staircase(n):
    # Time: O(n)     Space: O(1)
    f = 1
    s = 2

    for i in range((n-1)//2):
        f = f + s
        s = f + s

    if n % 2 == 0:
        return s
    else:
        return f


print(staircase(4))
# 5
print(staircase(5))
# 8
