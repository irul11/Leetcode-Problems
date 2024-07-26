class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        lenArr = len(original)
        lenStr = len(source)
        maps = dict()

        j = 0
        for i in range(lenArr):
            if original[i] not in maps:
                maps[original[i]] = j
                j += 1

        for i in range(lenArr):
            if changed[i] not in maps:
                maps[changed[i]] = j
                j += 1
        print(maps)
        dp = [[inf] * j for _ in range(j)]
        for i in range(len(dp)):
            dp[i][i] = 0
        for i in range(lenArr):
            dp[maps[original[i]]][maps[changed[i]]] = min(cost[i], dp[maps[original[i]]][maps[changed[i]]])

        for k in range(j):
            for i in range(j):
                for l in range(j):
                    dp[i][l] = min(dp[i][l], dp[i][k] + dp[k][l])

        ans = 0
        for i in range(lenStr):
            ii, ij = maps.get(source[i]), maps.get(target[i])
            
            if ii is None or ij is None or dp[ii][ij] == inf:
                return -1
            ans += dp[maps[source[i]]][maps[target[i]]]
            
        return ans
