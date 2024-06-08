class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        
        maps = dict()
        maps[0] = -1
        sums = 0
        
        for i in range(n):
            sums += nums[i]
            if sums % k in maps:
                if i - maps[sums % k] >= 2:
                    return True
            else:
                maps[sums % k] = i
                
        return False
