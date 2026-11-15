class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        orientation = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        directions = ["right", "down", "left", "up"]
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        res = []
        row, col = 0, 0
        curr_orientation = 0

        while top <= bottom and left <= right:
            direction = directions[curr_orientation]

            dr, dc = orientation[curr_orientation]
            before = len(res)
            while top <= row <= bottom and left <= col <= right:
                res.append(matrix[row][col])
                row += dr
                col += dc


            row -= dr
            col -= dc
            if dr == 1:
                right -= 1
            elif dr == -1:
                left += 1

            if dc == 1:
                top += 1
            elif dc == -1:
                bottom -= 1

            curr_orientation = (curr_orientation + 1) % 4
            next_dr, next_dc = orientation[curr_orientation]
            row += next_dr
            col += next_dc

        return res