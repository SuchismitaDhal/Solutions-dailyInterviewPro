# AMAZON
"""
    SOLVED
    Given a 2d n x m matrix where each cell has a certain amount of change on the floor, 
    your goal is to start from the top left corner mat[0][0] and end in the bottom right 
    corner mat[n - 1][m - 1] with the most amount of change. You can only move either left 
    or down.
"""


def max_change(mat):
    # Time: O(nm)    Space: O(nm)
    n = len(mat)
    m = len(mat[0])
    cost = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            cost[i][j] = mat[i][j] + max(cost[i + 1][j], cost[j][i + 1])

    return cost[0][0]


mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13
