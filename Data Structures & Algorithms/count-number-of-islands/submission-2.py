from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def clearIsland(row, col):
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == "1":
                    stack.append((row - 1, col))
                    stack.append((row + 1, col))
                    stack.append((row, col - 1))
                    stack.append((row, col + 1))
                    grid[row][col] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    clearIsland(row, col)
        return count
       