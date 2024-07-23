class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counter = 1
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter -= 1
            if counter < 0:
                if nums[j] == 0:
                    counter += 1
                j += 1
        return i - j
        