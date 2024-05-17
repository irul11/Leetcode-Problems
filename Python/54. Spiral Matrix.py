class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        
        x = [0, m-1]
        y = [0, n-1]
        move = [0,1]

        i = j = 0
        while len(result) < m * n:
            if j > y[1] and move[1] == 1:
                j -= 1
                i += 1
                x[0] += 1
                move = [1, 0]
            elif i > x[1] and move[0] == 1:
                i -= 1
                j -= 1
                y[1] -= 1
                move = [0, -1]
            elif j < y[0] and move[1] == -1:
                j += 1
                i -= 1
                x[1] -= 1
                move = [-1, 0]
            elif i < x[0] and move[0] == -1:
                i += 1
                j += 1
                y[0] += 1
                move = [0,1]
            else:
                result.append(matrix[i][j])
                i += move[0]
                j += move[1]
                
        return result
