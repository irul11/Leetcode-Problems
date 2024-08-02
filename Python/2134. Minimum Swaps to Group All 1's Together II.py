class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOne = sum(nums)
        currOne = sum(nums[-totalOne:])
        
        maxOne = currOne

        for i in range(len(nums)):
            currOne += nums[i] - nums[i - totalOne]
            maxOne = max(maxOne, currOne)
        
        return totalOne - maxOne
        