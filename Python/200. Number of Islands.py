class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        sets = set()

        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1" and (x, y) not in sets:
                sets.add((x, y))
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x, y-1)
            return
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == "1" and (x, y) not in sets:
                    result += 1
                    dfs(x,y)
        
        return result
        