class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    count = 0
                    stack = [(row, col)]
                    while stack:
                        curr_row, curr_col = stack.pop()
                        in_boundary = curr_row >= 0 and curr_row < rows and curr_col >= 0 and curr_col < cols
                        if in_boundary and grid[curr_row][curr_col] and (curr_row, curr_col) not in visited:
                            count += 1
                            stack.append((curr_row - 1, curr_col))
                            stack.append((curr_row + 1, curr_col))
                            stack.append((curr_row, curr_col - 1))
                            stack.append((curr_row, curr_col + 1))
                            visited.add((curr_row, curr_col))
                    result = max(result, count)
        return result
                    