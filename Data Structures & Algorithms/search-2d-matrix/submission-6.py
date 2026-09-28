class Solution:
    def searchMatrix2D(self, matrix: List[List[int]], target: int) -> bool:
        # binary search in two axis 
        yl, yr = 0, len(matrix) - 1

        # find the row that starts with largest number that's smaller than target
        y_candidate = -1
        while yl <= yr:
            yc = (yl + yr) // 2
            if matrix[yc][0] <= target:
                y_candidate = yc
                yl = yc + 1
            else:
                yr = yc - 1
           
        if y_candidate == -1:
            return False

        xl, xr = 0, len(matrix[0]) - 1
        x_candidate = -1
        while xl <= xr:
            xc = (xl + xr) // 2
            if matrix[y_candidate][xc] == target:
                return True
            elif matrix[y_candidate][xc] < target:
                xl = xc + 1
            else:
                xr = xc - 1
            
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 
        right = rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            row = mid // cols
            col = mid % cols
            value = matrix[row][col]
            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
