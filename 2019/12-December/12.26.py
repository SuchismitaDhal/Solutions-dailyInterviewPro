# UBER
"""
    SOLVED -- LEETCODE#48
    Given a square 2D matrix (n x n), rotate the matrix by 90 degrees clockwise.
"""


def rotate(mat):
    # Time: O(n^2)    Space: O(1)

    n = len(mat)
    m = n-1
    # Transposing with right diagonal
    for i in range(m):
        for j in range(m - i):
            mat[i][j], mat[m - j][m - i] = mat[m - j][m - i], mat[i][j]

    # Fliping vertically
    for i in range(n // 2):
        for j in range(n):
            mat[i][j], mat[m - i][j] = mat[m - i][j], mat[i][j]

    return mat


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
