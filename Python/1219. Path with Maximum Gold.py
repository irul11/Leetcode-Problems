class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = 0
        
        def backtracks(i, j, sets, total):
            nonlocal result
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in sets:
                if result < total:
                    result = total
                return 

            sets.add((i, j))

            backtracks(i+1, j, sets, total + grid[i][j])
            backtracks(i-1, j, sets, total + grid[i][j])
            backtracks(i, j+1, sets, total + grid[i][j])
            backtracks(i, j-1, sets, total + grid[i][j])

            sets.remove((i, j))
            return

        sets = set()
        for i in range(m):
            for j in range(n):
                backtracks(i,j,sets,0)

        return result
        