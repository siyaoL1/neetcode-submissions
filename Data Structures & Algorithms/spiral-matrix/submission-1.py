class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        result = []
        row, col = 0, -1  # The first step lands on (0, 0).
        direction = 0

        while top <= bottom and left <= right:
            dr, dc = directions[direction]

            while top <= row + dr <= bottom and left <= col + dc <= right:
                row += dr
                col += dc
                result.append(matrix[row][col])

            if dc == 1:
                top += 1
            elif dr == 1:
                right -= 1
            elif dc == -1:
                bottom -= 1
            else:
                left += 1

            direction = (direction + 1) % 4

        return result