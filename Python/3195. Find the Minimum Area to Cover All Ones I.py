class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = [inf, 0]
        col = [inf, 0]
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row[0] = min(row[0], i)
                    col[0] = min(col[0], j)
                    row[1] = max(row[1], i)
                    col[1] = max(col[1], j)
                    
        return (row[1]-row[0]+1) * (col[1]-col[0]+1)
        