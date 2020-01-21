# GOOGLE
"""
    LEETCODE#348
    Design a Tic-Tac-Toe game played between two players on an n x n grid. 
    A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid. 
    A player who succeeds in placing n of their marks in a horizontal, diagonal, 
    or vertical row wins the game. Once a winning condition is reached, 
    the game ends and no more moves are allowed. 
    Below is an example game which ends in a winning condition:

    Given n = 3, assume that player 1 is "X" and player 2 is "O" 
    board = TicTacToe(3);

    board.move(0, 0, 1); -> Returns 0 (no one wins)
    |X| | |
    | | | |    // Player 1 makes a move at (0, 0).
    | | | |

    board.move(0, 2, 2); -> Returns 0 (no one wins)
    |X| |O|
    | | | |    // Player 2 makes a move at (0, 2).
    | | | |

    board.move(2, 2, 1); -> Returns 0 (no one wins)
    |X| |O|
    | | | |    // Player 1 makes a move at (2, 2).
    | | |X|

    board.move(1, 1, 2); -> Returns 0 (no one wins)
    |X| |O|
    | |O| |    // Player 2 makes a move at (1, 1).
    | | |X|

    board.move(2, 0, 1); -> Returns 0 (no one wins)
    |X| |O|
    | |O| |    // Player 1 makes a move at (2, 0).
    |X| |X|

    board.move(1, 0, 2); -> Returns 0 (no one wins)
    |X| |O|
    |O|O| |    // Player 2 makes a move at (1, 0).
    |X| |X|

    board.move(2, 1, 1); -> Returns 1 (player 1 wins)
    |X| |O|
    |O|O| |    // Player 1 makes a move at (2, 1).
    |X|X|X|
"""


# naive version; Space: O(n^2)    Time: O(n)

class TicTacToe0(object):
    def __init__(self, n):
        # this commented initalisation is a bad way https://snakify.org/en/lessons/two_dimensional_lists_arrays/#section_2
        # self.mat = [[0] * (n + 1)] * (n + 1)
        self.mat = [[0 for i in range(n+1)] for j in range(n+1)]
        self.n = n

    def move(self, row, col, player):
        self.mat[row][col] = player
        score = self.rowcheck(row) + self.colcheck(col)
        if row == col or abs(row + col) == self.n + 1:
            score += self.diagcheck(row, col)
        return score

    def rowcheck(self, row):
        ans = self.mat[row][1]
        for i in range(2, self.n+1):
            if self.mat[row][i] != ans:
                return 0
        return ans

    def colcheck(self, col):
        ans = self.mat[1][col]
        for i in range(2, self.n+1):
            if self.mat[i][col] != ans:
                return 0
        return ans

    def diagcheck(self, row, col):
        # left diagonal
        if row == col:
            ans = self.mat[1][1]
            for i in range(2, self.n + 1):
                if self.mat[i][i] != ans:
                    return 0
            return ans

        # right diagonal
        else:
            ans = self.mat[1][self.n]
            for i in range(1, self.n):
                if self.mat[1 + i][self.n - i] != ans:
                    return 0
            return ans

# more optimised version; Space:O(n)    Time: O(1)


class TicTacToe(object):
    def __init__(self, n):
        self.rowSum = [0] * (n+1)
        self.colSum = [0] * (n+1)
        self.rdgSum = 0
        self.ldgSum = 0
        self.n = n

    def move(self, row, col, player):
        if player == 1:
            p = -1
        else:
            p = 1
        self.rowSum[row] += p
        self.colSum[col] += p

        # cell lies in left diagonal
        if row == col:
            self.ldgSum += p
        # cell lies in right diagonal
        if row + col == self.n + 1:
            self.rdgSum += p

        if max(self.rowSum[row], self.colSum[col], self.ldgSum, self.rdgSum) == self.n:
            return 2
        if min(self.rowSum[row], self.colSum[col], self.ldgSum, self.rdgSum) == -self.n:
            return 1
        return 0


board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
