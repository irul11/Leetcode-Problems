class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left , right = 0 , len(nums)-1
        count = 0
        while left < right:
            if nums[left] + nums[right] > upper:
                right -= 1
            else:
                count += right - left
                left += 1
        left , right = 0 , len(nums)-1
        while left < right:
            if nums[left] + nums[right] < lower:
                count -= right - left
                left += 1  
            else:
                right -= 1
        return count
        