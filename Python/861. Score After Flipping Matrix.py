class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        toggle = [False] * m
        
        for j in range(0, n):
            max_col = m * (1 << n-1-j) 
            sum_col = 0 if j != 0 else max_col

            for i in range(m):
                if j == 0:
                    toggle[i] = True if grid[i][j] == 0 else False

                elif toggle[i]:
                    if grid[i][j] == 0:
                        sum_col += 1 * (1 << n-1-j)
                        
                else:
                    sum_col += grid[i][j] * (1 << n-1-j) 
                    
            if sum_col < max_col - sum_col:
                sum_col = max_col - sum_col
                
            result += sum_col

        return result
