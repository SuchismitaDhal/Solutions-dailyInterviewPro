# AMAZON
"""
    SOLVED -- NO SIMILAR PROBLEM FOUND
    You are given a 2D array of characters, and a target string.
    Return whether or not the word target word exists in the matrix.
    Unlike a standard word search, the word must be either going left-to-right,
    or top-to-bottom in the matrix.
    Example:
    [['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
    Given this matrix, and the target word FOAM, you should return true,
    as it can be found going up-to-down in the first column.
"""


def word_search(matrix, word):
    # Time: O(mn^2)     Space: O(1)

    def searchH(i, j):
        if j + len(word) > len(matrix[0]):
            return False
        for x in range(len(word)):
            if word[x] != matrix[i][j + x]:
                return False
        return True

    def searchV(i, j):
        if i + len(word) > len(matrix):
            return False
        for x in range(len(word)):
            if word[x] != matrix[i + x][j]:
                return False
        return True

    m = len(word)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if searchV(i, j) or searchH(i, j):
                return True
    return False


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(word_search(matrix, 'FOAM'))
# True
