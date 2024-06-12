class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        streak = 1

        for i in range(1, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            if nums[i] - nums[i-1] == 1:
                streak += 1
            else:
                ans = max(ans, streak)
                streak = 1

        return max(ans, streak) if nums else 0
