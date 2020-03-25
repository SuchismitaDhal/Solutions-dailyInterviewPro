# LINKEDIN
"""
    SOLVED -- LEETCODE#991
    You are only allowed to perform 2 operations, 
    multiply a number by 2, or subtract a number by 1. 
    Given a number x and a number y, 
    find the minimum number of operations needed to go from x to y.

"""


def min_operations(x, y):
    # Time: O(log(y/x))  Space: O(1)
    if x >= y:
        return x - y

    # if y is odd, only one way is to add 1 to it
    # if y is even,
    # for the situation:
    #     x - - - - - y
    # for y to reach x, we must(atleast once)
    # divide it by 2. Since ((y/2) + 1)[2 steps] is more
    # favorable than ((y+2)/2)[3 steps],
    t = 0
    while y > x:
        t += 1
        if y % 2:
            y += 1
        else:
            y //= 2
    t += x - y
    return t


print(min_operations(6, 20))
# (((6 - 1) * 2) * 2) = 20 : 3 operations needed only
# print 3
