class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        result = inf
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(result-target) > abs(total-target):
                    result = total
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return target
                # print(result)
        return result
        