# MICROSOFT
"""
    SOLVED -- LEETCODE 63
    A maze is a matrix where each cell can either be a 0 or 1. 
    A 0 represents that the cell is empty, and a 1 represents a wall that cannot be walked through.
    You can also only travel either right or down.
    Given a nxm matrix, find the number of ways someone can go from the top left corner to the 
    bottom right corner. You can assume the two corners will always be 0.

    Example:
    Input: [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    # 0 1 0
    # 0 0 1
    # 0 0 0
    Output: 2
    The two paths that can only be taken in the above example are: down -> right -> down -> right, 
    and down -> down -> right -> right.
"""


def paths_through_maze(maze):
    # time: O(n^2)    space: O(n^2)
    # dynamic programming with memoisation
    r = len(maze)
    c = len(maze[0])
    f = 0

    if r == 1 and c == 1:
        return 1
    dp = [[0 for i in range(c)] for j in range(r)]

    for i in range(c - 2, -1, -1):
        f = f or maze[r-1][i]
        if f == 0:
            dp[r - 1][i] = 1
        else:
            dp[r - 1][i] = 0

    f = 0
    for i in range(r - 2, -1, -1):
        f = f or maze[i][c - 1]
        if f == 0:
            dp[i][c - 1] = 1
        else:
            dp[i][c - 1] = 0

    for i in range(r - 2, -1, -1):
        for j in range(c - 2, -1, -1):
            if maze[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

    return dp[0][0]


print(paths_through_maze([[0, 1, 0],
                          [0, 0, 1],
                          [0, 0, 0]]))
# 2
