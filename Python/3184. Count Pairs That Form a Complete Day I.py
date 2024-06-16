class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        maps = defaultdict(int)
        
        for i in range(len(hours)):
            ans += maps[hours[i] % 24]
            
            maps[(24 - hours[i] % 24) % 24] += 1
            
        return ans
    