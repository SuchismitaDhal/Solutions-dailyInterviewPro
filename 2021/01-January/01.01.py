# GOOGLE
"""
    SOLVED -- LEETCODE#688
    A chess board is an 8x8 grid. Given a knight at any position (x, y) 
    and a number of moves k, we want to figure out after k random moves 
    by a knight, the probability that the knight will still be on the chessboard. 
    Once the knight leaves the board it cannot move again and will be considered off the board.
"""

move = [[-2, -1], [-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1]]
def is_knight_on_board(x, y, k, cache={}):
    # Time: O(k)    Space: O(1)
    currBoard = [[0 for _ in range(8)] for _ in range(8)]
    nextBoard = [[0 for _ in range(8)] for _ in range(8)]
    currBoard[x][y] = 1
    
    def isValidMove(x, y):
        return min(x, y) >= 0 and max(x, y) < 8 
    
    sol = 0
    curr = 1
    
    for _ in range(k):
        for i in range(8):
            for j in range(8):
                for dx, dy in move:
                    if isValidMove(i + dx, j + dy):
                        nextBoard[i + dx][j + dy] += currBoard[i][j] * 0.125
                currBoard[i][j] = 0
        nextBoard, currBoard = currBoard, nextBoard
        
    return sum(map(sum, currBoard))

print(is_knight_on_board(0, 0, 1))
# 0.25