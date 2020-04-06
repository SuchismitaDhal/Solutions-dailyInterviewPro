# FACEBOOK
"""
    SOLVED -- LEETCODE#566
    Reshaping a matrix means to take the same elements in a matrix 
    but change the row and column length. 
    This means that the new matrix needs to have the same elements 
    filled in the same row order as the old matrix. 
    Given a matrix, a new row size x and a new column size y, 
    reshape the matrix. 
    If it is not possible to reshape, return None.
"""


def reshape_matrix(mat, x, y):
    # Time: O(n) n being the number of elements in the matrix
    # Space: O(1)
    n = len(mat)
    if n == 0 and x * y == 0:
        return mat
    m = len(mat[0])
    if m * n != x * y:
        return None

    sol = [[0 for i in range(x)] for j in range(y)]

    for i in range(n * m):
        sol[i // x][i % x] = mat[i // m][i % m]

    return sol


print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
