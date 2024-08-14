class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans, n = 0, len(nums)
        l, r = 0, nums[-1] - nums[0]

        while l < r:
            counter = 0
            m = (l + r) // 2

            i = j = 0
            while i < n:
                while j < n and nums[j] <= nums[i] + m:
                    j += 1
                    
                counter += j - i - 1
                i += 1
            
            if counter < k:
                l = m + 1
            else:
                r = m
        
        return l