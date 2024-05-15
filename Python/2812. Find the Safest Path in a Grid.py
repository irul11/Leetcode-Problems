from collections import deque
from math import inf
from typing import List
import heapq  

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        def bfs(grid, score, n):
            queue = deque()
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        score[i][j] = 0
                        queue.append((i, j))

            while queue:
                x, y = queue.popleft()
                s = score[x][y]

                for (row, col) in [(0,1), (0,-1), (1,0), (-1,0)]:
                    curr_x = x + row
                    curr_y = y + col

                    if 0 <= curr_x < n and 0 <= curr_y < n and score[curr_x][curr_y] > s + 1:
                        score[curr_x][curr_y] = s + 1
                        queue.append((curr_x, curr_y))
        
        n = len(grid)
        score = [[inf for _ in range(n)] for _ in range(n)]
        bfs(grid, score, n)
        # print(score)
        visited = [[False for _ in range(n)] for _ in range(n)]
        
        prior_queue = [(-score[0][0], 0, 0)]
        heapq.heapify(prior_queue)

        while prior_queue:
            safe, x, y = heapq.heappop(prior_queue)
            safe *= -1
            
            if x == n - 1 and y == n - 1: # Right bottom
                return safe
            
            visited[x][y] = True

            for (row, col) in [(0,1), (0,-1), (1,0), (-1,0)]:
                curr_x = x + row
                curr_y = y + col

                if 0 <= curr_x < n and 0 <= curr_y < n and not visited[curr_x][curr_y]:
                    s = min(safe, score[curr_x][curr_y])
                    heapq.heappush(prior_queue, (-s, curr_x, curr_y))
                    visited[curr_x][curr_y] = True
        
        return -1
