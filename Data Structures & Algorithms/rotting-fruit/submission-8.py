class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rounds = 0
        rows, cols = len(grid), len(grid[0])

        # Get the list of already rotted fruit index
        current = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    current.append((row, col))

        while current:
            next_round = []
            for row, col in current:
                # Rot and record the rotted neighbors for next round of process
                pairs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                for neighbor_row, neighbor_col in pairs:
                    in_boundary = (neighbor_row >= 0 and neighbor_col >= 0 
                        and neighbor_row < rows and neighbor_col < cols
                    )
                    if in_boundary and grid[neighbor_row][neighbor_col] == 1:
                        grid[neighbor_row][neighbor_col] = 2
                        next_round.append((neighbor_row, neighbor_col))
            if next_round:
                rounds += 1
            current = next_round

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return rounds
        