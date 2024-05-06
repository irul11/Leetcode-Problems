from collections import defaultdict, deque

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        empty_cell = deque()

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if (value) == '.':
                    empty_cell.append((r, c))
                else:
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[(r//3, c//3)].add(value)
        
        digits = [str(n) for n in range(1, 10)]
        def dfs():
            if not empty_cell:
                return True
            
            r, c = empty_cell[0]
            box = (r//3, c//3)
            
            for value in digits:
                if value not in rows[r] and value not in cols[c] and value not in boxes[box]:
                    board[r][c] = value
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box].add(value)
                    empty_cell.popleft()
                    
                    if dfs():
                        return True
                    
                    board[r][c] = '.'
                    rows[r].discard(value)
                    cols[c].discard(value)
                    boxes[box].discard(value)
                    empty_cell.appendleft((r, c))
                    
            return False

        if dfs():
            return board
    
    def print_board(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- " * 11)
            for j in range(len(board[0])):
                cell = board[i][j]
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(cell)
                    continue
                print(cell, end=" ")
            

# # Example usage:
# sudoku_grid = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]
# solver = Solution()
# solver.print_board(sudoku_grid)
# print("+ "*11)
# # solver.solveSudoku(sudoku_grid)
# solver.print_board(solver.solveSudoku(sudoku_grid))
