# UBER
"""
    SOLVED 
    [VERIFIED] -- https://www.geeksforgeeks.org/largest-connected-component-on-a-grid/
    Find the maximum number of connected colors in a grid.
    Can you solve this both recursively and iteratively?
"""


class Grid:
    def __init__(self, grid):
        self.grid = grid

    def dfs(self, i, j):
        val = self.grid[i][j]
        self.grid[i][j] = -1
        sol = 1
        sol += self.dfs(i + 1, j) if i + \
            1 < len(self.grid) and self.grid[i + 1][j] == val else 0
        sol += self.dfs(i - 1, j) if i - \
            1 >= 0 and self.grid[i - 1][j] == val else 0
        sol += self.dfs(i, j+1) if j + \
            1 < len(self.grid[0]) and self.grid[i][j+1] == val else 0
        sol += self.dfs(i, j-1) if j - \
            1 >= 0 and self.grid[i][j-1] == val else 0
        return sol

    def max_connected_colors(self):
        # Time: O(n^2)   Space: O(n^2) for dfs
        maxcount = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[0][0] != -1:
                    maxcount = max(maxcount, self.dfs(i, j))
        return maxcount


grid = [[1, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 1, 0, 0]]

print(Grid(grid).max_connected_colors())
# 7
