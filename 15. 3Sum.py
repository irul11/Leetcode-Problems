class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        result = []
        while i < len(nums) - 2:
            left = nums[i]
            j = i + 1
            while j < len(nums) - 1:
                left += nums[j]
                k = j + 1
                while k < len(nums):
                    left += nums[k]
                    if left == 0:
                        result.append([nums[i], nums[j], nums[k]])
            i += 1
            print(result)