# MICROSOFT
"""
    SOLVED -- LEETCODE#62
    You 2 integers n and m representing an n by m grid, 
    determine the number of ways you can get from the top-left to the 
    bottom-right of the matrix y going only right or down.
    Example:
    n = 2, m = 2
    This should return 2, since the only possible routes are:
    Right, down
    Down, right.
"""


def num_ways(n, m):
    # Time: O(n^2)      Space: O(n^2) can be optimised to O(n) by using a single array
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    dp[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            dp[i][j] += dp[i-1][j] + dp[i][j-1]

    return dp[m][n]


print(num_ways(2, 2))
# 2
