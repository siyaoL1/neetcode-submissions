class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        
        boarder_zeros = set()
        for row in [0, rows - 1]:
            for col in range(cols):
                if board[row][col] == "O":
                    boarder_zeros.add((row, col))
        for col in [0, cols - 1]:
            for row in range(rows):
                if board[row][col] == "O":
                    boarder_zeros.add((row, col))
        
        stack = list(boarder_zeros)
        visited = set(boarder_zeros)
        while stack:
            row, col = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows and 
                    0 <= new_col < cols and 
                    board[new_row][new_col] == "O" and 
                    (new_row, new_col) not in visited
                ):
                    stack.append((new_row, new_col)) 
                    visited.add((new_row, new_col))
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if board[row][col] == "O" and (row, col) not in visited:
                    board[row][col] = "X"

# ["O","X","X","O","X"]
# ["X","O","O","X","O"]
# ["X","O","X","O","X"]
# ["O","X","O","O","O"]
# ["X","X","O","X","O"]]