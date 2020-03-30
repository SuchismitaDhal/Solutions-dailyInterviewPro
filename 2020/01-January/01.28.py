# FACEBOOK
"""
    Reshaping a matrix means to take the same elements in a matrix 
    but change the row and column length. 
    This means that the new matrix needs to have the same elements 
    filled in the same row order as the old matrix. 
    Given a matrix, a new row size x and a new column size y, 
    reshape the matrix. 
    If it is not possible to reshape, return None.
"""


def reshape_matrix(mat, x, y):
    n = len(mat)
    if n == 0 and x * y == 0:
        return mat
    m = len(mat[0])
    if n * m != x * y:
        return None


print(reshape_matrix([[1, 2], [3, 4]], 1, 4))
# [[1], [2], [3], [4]]

print(reshape_matrix([[1, 2], [3, 4]], 2, 3))
# None
