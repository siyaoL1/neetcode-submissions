class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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