class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        ans = sums

        for i in range(k, len(nums)):
            sums += nums[i] - nums[i-k]
            ans = max(ans, sums)

        return ans / k
