from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = [0] * n
        result = float("-inf")

        for i in range(n-1, -1, -1):
            dp[i] = energy[i]
            if i < n - k:
                dp[i] += dp[i+k]
            if result < dp[i]:
                result = dp[i]

        return result
        