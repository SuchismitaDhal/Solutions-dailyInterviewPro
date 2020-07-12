# TWITTER
"""
    SOLVED -- LEETCODE#867
    Given a matrix, transpose it. 
    Transposing a matrix means the rows are now the column and vice-versa.
"""


def transpose(mat):
    # Time: O(m*n)   Space: O(1)
    n = len(mat)
    m = len(mat[0])

    res = [[0 for i in range(n)] for j in range(m)]

    for i in range(n):
        for j in range(m):
            res[j][i] = mat[i][j]

    return res


mat = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(mat))
# [[1, 4],
#  [2, 5],
#  [3, 6]]
