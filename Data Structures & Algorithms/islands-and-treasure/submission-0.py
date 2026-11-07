class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        # Locate all treasures
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        # Process waves
        while queue:
            row, col = queue.popleft()
            for neighbor_row, neighbor_col in [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1)
            ]:
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                    if grid[neighbor_row][neighbor_col] == 2147483647:
                        grid[neighbor_row][neighbor_col] = grid[row][col] + 1
                        queue.append((neighbor_row, neighbor_col))