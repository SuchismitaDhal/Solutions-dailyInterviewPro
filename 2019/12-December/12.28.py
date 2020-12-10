# GOOGLE
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    Given a positive integer, find the square root of the integer 
    without using any built in square root or power functions (math.sqrt or the ** operator). 
    Give accuracy up to 3 decimal points.
"""


def sqrt(x):
    # Time: O(n)     Space:O(n)
    # n: number of digits in x
    sol = 0

    s = [0, 0, 0]
    temp = x
    while temp:
        s.append(temp % 100)
        temp //= 100

    m = 0
    r = 0

    for n in s[::-1]:
        r = r * 100 + n
        x = 0
        while x < 10:
            if (m * 10 + x) * x > r:
                break
            else:
                x += 1
        x = x - 1
        sol = sol * 10 + x
        r = r - ((m * 10 + x) * x)
        m = m * 10 + 2 * x

    return sol/1000


print(sqrt(5))
# 2.236
