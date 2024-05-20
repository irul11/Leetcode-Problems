class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        result = 0
        for num in nums:
            result |= num
        return result << (len(nums) - 1)
