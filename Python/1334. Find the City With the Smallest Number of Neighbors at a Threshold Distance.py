class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # USING FLOYD WARSHALL ALGORITHM
        
        dp = [[inf] * n for _ in range(n)]
        for e in edges:
            dp[e[0]][e[1]] = e[2]
            dp[e[1]][e[0]] = e[2]
        for i in range(n):
            dp[i][i] = 0
        
        for h in range(n):
            for i in range(n):
                for j in range(n):
                    if (dp[i][j] > dp[i][h] + dp[h][j] and
                        dp[i][h] != inf and dp[h][j] != inf):
                        dp[i][j] = dp[i][h] + dp[h][j]
        
        arr = []

        for i in range(n):
            arr.append([-1, i])
            for j in range(n):
                if dp[i][j] <= distanceThreshold:
                    arr[i][0] += 1
        arr.sort(key=lambda x: (x[0], -x[1]))
        
        return arr[0][1]

