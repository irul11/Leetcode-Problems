class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = 1
        while n in nums_set:
            n += 1
        return n