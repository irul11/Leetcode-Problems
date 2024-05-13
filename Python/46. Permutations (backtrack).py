class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def backtrack(n, nums):
            if n == len(nums):
                result.append(nums.copy())
                return 
            
            for i in range(n, len(nums)):
                nums[i], nums[n] = nums[n], nums[i]
                backtrack(n+1, nums)
                nums[n], nums[i] = nums[i], nums[n]
                    
            return 

        backtrack(0, nums)
        return result
