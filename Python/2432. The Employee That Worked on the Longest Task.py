class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans = logs[0][0]
        longest = logs[0][1]

        for i in range(1, len(logs)):
            if logs[i][1] - logs[i-1][1] > longest:
                longest = logs[i][1] - logs[i-1][1]
                ans = logs[i][0]
            elif logs[i][1] - logs[i-1][1] == longest:
                ans = min(logs[i][0], ans)
        
        return ans
