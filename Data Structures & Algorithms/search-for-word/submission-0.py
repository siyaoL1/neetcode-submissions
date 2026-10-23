class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        stack = []
        for row in range(rows):
            for col in range(cols):
                stack.append(((row,col), 0, {(row, col)}))
        
        def check_visited_and_add(stack, visited, row, col, new_index, new_visited):
            if (row, col) not in visited and (0 <= row < rows) and (0 <= col < cols):
                stack.append(((row, col), new_index, new_visited.copy()))
        print(board)
        while stack:
            (row, col), index, visited = stack.pop()
            if board[row][col] == word[index]:
                # print(row, col, word[index])
                new_index = index + 1
                if new_index == len(word):
                    return True
                visited.add((row, col))
                check_visited_and_add(stack, visited, row - 1, col, new_index, visited)
                check_visited_and_add(stack, visited, row + 1, col, new_index, visited)
                check_visited_and_add(stack, visited, row, col - 1, new_index, visited)
                check_visited_and_add(stack, visited, row, col + 1, new_index, visited)
        
        
        return False