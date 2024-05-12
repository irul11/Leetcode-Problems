from typing import List
from math import inf

class Solution:
    result = float("inf")
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n, result = len(grid), len(grid[0]), -inf
        
        for i in range(m):
            for j in range(n):
                prev = min(grid[i-1][j] if i else inf, grid[i][j-1] if j else inf)
                result = max(result, grid[i][j] - prev)
                grid[i][j] = min(grid[i][j], prev)
                
        return result
        