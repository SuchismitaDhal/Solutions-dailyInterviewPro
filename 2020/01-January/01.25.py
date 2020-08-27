# AIRBNB
"""
    SOLVED -- LEETCODE#119
    Pascal's Triangle is a triangle where all numbers are the sum of the 
    two numbers above it. Here's an example of the Pascal's Triangle of size 5.
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    Given an integer n, generate the n-th row of the Pascal's Triangle.
"""


def pascal_triangle_row(n):
    # Time: O(n)     Space: O(1)
    num = n-1
    den = 1
    sol = [1]
    for i in range(1, n):
        p = (sol[i - 1] * num) // den
        sol.append(p)
        num -= 1
        den += 1
    return sol


print(pascal_triangle_row(5))
# [1, 5, 10, 10, 5, 1]
