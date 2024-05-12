from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []
        for i in range(1, n-1):
            temp = []
            for j in range(1, n-1):         
                temp.append(max([
                    grid[i-1][j-1]  , grid[i-1][j]  , grid[i-1][j+1],
                    grid[i][j-1]    , grid[i][j]    , grid[i][j+1],
                    grid[i+1][j-1]  , grid[i+1][j]  , grid[i+1][j+1]
                ]))
            result.append(temp)
        return result
        
        