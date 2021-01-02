# GOOGLE
"""
    A chess board is an 8x8 grid. Given a knight at any position (x, y) 
    and a number of moves k, we want to figure out after k random moves 
    by a knight, the probability that the knight will still be on the chessboard. 
    Once the knight leaves the board it cannot move again and will be considered off the board.
"""

def is_knight_on_board(x, y, k, cache={}):
  # Fill this in.

print (is_knight_on_board(0, 0, 1))
# 0.25