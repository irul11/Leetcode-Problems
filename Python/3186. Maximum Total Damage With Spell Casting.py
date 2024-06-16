class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        c = Counter(power)
        ans = 0
        arrc = sorted(c.keys())

        dp = [0 for _ in range(len(arrc)) ]
        dp[0] = arrc[0] * c[arrc[0]]

        for i in range(1, len(arrc)):
            curr = arrc[i] * c[arrc[i]]
            dp[i] = dp[i-1]

            prevIndex = i - 1
            while ( prevIndex >= 0 and 1 <= abs(arrc[prevIndex] - arrc[i]) <= 2):
                prevIndex -= 1
            
            if prevIndex >= 0:
                dp[i] = max(dp[i], dp[prevIndex] + curr)
            else:
                dp[i] = max(dp[i], curr)
        
        return dp[len(arrc) - 1]