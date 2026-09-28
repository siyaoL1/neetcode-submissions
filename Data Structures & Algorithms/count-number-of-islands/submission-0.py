class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # first thought is to have a visited map of all the grid
        # whenever we hit a land we will scan and mark all the connected land as visited
        # then continuing scanning accross the grid till finish
        def clear_land(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                return
            grid[row][col] = '0'
            clear_land(row - 1, col)
            clear_land(row + 1, col)
            clear_land(row, col - 1)
            clear_land(row, col + 1)


        # but second thought realized that we can just clear the land by marking them to be 0
        land_count = 0
        # scanning accross the grid:
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    land_count += 1
                    clear_land(row, col)
        
        return land_count

        