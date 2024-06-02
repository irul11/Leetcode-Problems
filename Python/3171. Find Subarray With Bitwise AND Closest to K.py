class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [set() for _ in range(n+1)] # increase by one for the initial standard of element 0
        ans = inf

        for i in range(n):                
            dp[i].add(nums[i])
            ans = min(ans, abs(k - nums[i]))
            if ans == 0:
                return 0

            for j in dp[i-1]:
                curr = j & nums[i]
                dp[i].add(curr)
                ans = min(ans, abs(k - curr))
                if ans == 0:
                    return 0

        return ans
        