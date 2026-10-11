class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we count the passes that we need to take for rot all of the fruit or there's no change from the last round then return -1
        rounds = 0
        updated = True
        rows, cols = len(grid), len(grid[0])
        
        def rot_surrounding(row, col) -> list:
            rotted = []
            pairs = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for row, col in pairs:
                in_boundary = row >= 0 and col >= 0 and row < rows and col < cols
                if in_boundary and grid[row][col] == 1:
                    rotted.append((row, col))
            
            return rotted

        while updated:
            rotted = []
            updated = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 2:
                        rotted.extend(rot_surrounding(row, col))
            if rotted:
                updated = True
                for row, col in set(rotted):
                    grid[row][col] = 2
            rounds += 1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        
        return rounds - 1
        