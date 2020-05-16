# LINKEDIN
"""
    SOLVED -- LEETCODE#200
    Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), 
    count the number of islands present in the grid. The definition of an island is as follows:
    1.) Must be surrounded by water blocks.
    2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
    Assume all edges outside of the grid are water.
    Example:
        Input: 
        10001
        11000
        10110
        00000
        Output: 3
"""
from collections import deque


class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def bfs(self, grid, i, j):
        move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        Q = deque()
        Q.append((i, j))
        while len(Q) > 0:
            curr = Q.popleft()
            for s in move:
                nxt = (curr[0] + s[0], curr[1] + s[1])
                if self.inRange(grid, nxt[0], nxt[1]) and grid[nxt[0]][nxt[1]] == 1:
                    Q.append((nxt[0], nxt[1]))
                grid[curr[0]][curr[1]] = 0

    def numIslands(self, grid):
        # Time: O(n*n)   Space: O(n*n)
        sol = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sol += 1
                    self.bfs(grid, i, j)

        return sol


grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3
