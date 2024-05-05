class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        array = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                array += [
                    (i, board[i][j]),
                    (board[i][j], j),
                    (i//3, j//3, board[i][j])
                ]
        print (array)
        return len(array) == len(set(array))
    


if __name__ == "__main__":
    solution = Solution()
    # For testing
    # print(solution.isValidSudoku(
    #     board = 
    #         [["5","3",".",".","7",".",".",".","."],
    #         ["6",".",".","1","9","5",".",".","."],
    #         [".","9","8",".",".",".",".","6","."],
    #         ["8",".",".",".","6",".",".",".","3"],
    #         ["4",".",".","8",".","3",".",".","1"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".","6",".",".",".",".","2","8","."],
    #         [".",".",".","4","1","9",".",".","5"],
    #         [".",".",".",".","8",".",".","7","9"]]
    # ))