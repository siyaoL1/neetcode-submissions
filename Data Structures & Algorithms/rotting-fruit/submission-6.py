class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we count the passes that we need to take for rot all of the fruit or there's no change from the last round then return -1
        rounds = 0
        updated = True
        rows, cols = len(grid), len(grid[0])

        non_empty = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    non_empty = True
        
        if not non_empty:
            return 0
        
        def rot_surrounding(row, col) -> list:
            rotted = []
            pairs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for row, col in pairs:
                in_boundary = row >= 0 and col >= 0 and row < rows and col < cols
                if in_boundary and grid[row][col] == 1:
                    grid[row][col] = 2
                    rotted.append((row, col))
            
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
                    if grid[row][col] == 2:
                        next_round.extend(rot_surrounding(row, col))
            current = next_round
            rounds += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return rounds - 1
        