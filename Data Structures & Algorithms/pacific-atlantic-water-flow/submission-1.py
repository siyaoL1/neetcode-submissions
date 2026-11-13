class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        def reachable_from(border_cells):
            visited = set(border_cells)
            stack = list(visited)

            while stack:
                row, col = stack.pop()

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[row][col]
                    ):
                        stack.append((nr, nc))
                        visited.add((nr, nc))
            return visited
        
        pacific_border = (
            [(0, col) for col in range(cols)]
            + [(row, 0) for row in range(rows)]
        )
        atlantic_border = (
            [(rows - 1, col) for col in range(cols)]
            + [(row, cols - 1) for row in range(rows)]
        )

        pacific = reachable_from(pacific_border)
        atlantic = reachable_from(atlantic_border)

        return [[row, col] for row, col in pacific & atlantic]