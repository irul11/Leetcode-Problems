class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort()
        
        ans = meetings[0][0] - 1
        for i in range(n-1):
            if meetings[i+1][0] <= meetings[i][1]:
                meetings[i+1][1] = max(meetings[i][1], meetings[i+1][1])
            else:
                ans += meetings[i+1][0] - meetings[i][1] - 1
                
        ans += days - meetings[-1][1]
        return ans