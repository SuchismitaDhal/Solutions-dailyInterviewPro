# FACEBOOK
"""
    SOLVED -- LEETCODE#74
    Given a matrix that is organized such that the numbers will 
    always be sorted left to right, 
    and the first number of each row will always be greater than the last element 
    of the last row (mat[i][0] > mat[i - 1][-1]), 
    search for a specific value in the matrix and return whether it exists.
"""


def bin_search_col(col, v):
    if len(col) == 1:
        return 0
    m = len(col) // 2
    if col[0] <= v and col[1] > v:
        return 0
    if col[m] <= v:
        return m + bin_search_col(col[m:], v)
    else:
        return bin_search_col(col[:m], v)


def bin_search_row(row, v):
    if len(row) == 0:
        return False
    if len(row) == 1:
        return True if row[0] == v else False

    m = len(row) // 2
    if row[m] <= v:
        return bin_search_row(row[m:], v)
    else:
        return bin_search_row(row[:m], v)


def searchMatrix(mat, value):
    # Time: O(2logn)    Space: O(n) for clarity, can be done in O(logn)
    r, c = len(mat), len(mat[0])

    if mat[0][0] > value:
        return False

    col0 = [mat[i][0] for i in range(r)]
    target_col = bin_search_col(col0, value)
    return bin_search_row(mat[target_col], value)


mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
