class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we count the passes that we need to take for rot all of the fruit or there's no change from the last round then return -1
        rounds = 0
        updated = True
        rows, cols = len(grid), len(grid[0])

        
        def rot_surrounding(row, col) -> list:
            rotted = []
            pairs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for neighbor_row, neighbor_col in pairs:
                in_boundary = neighbor_row >= 0 and neighbor_col >= 0 and neighbor_row < rows and neighbor_col < cols
                if in_boundary and grid[neighbor_row][neighbor_col] == 1:
                    grid[neighbor_row][neighbor_col] = 2
                    rotted.append((neighbor_row, neighbor_col))
            
            return rotted

        # Get the list of already rotted fruit index
        current = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    current.append((row, col))

        
        while current:
            next_round = []
            for row, col in current:
                next_round.extend(rot_surrounding(row, col))
            if next_round:
                rounds += 1
            current = next_round

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return rounds
        