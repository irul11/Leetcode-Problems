class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, n-1

        while nums[left] < 0 and nums[right] > 0 and left < right:
            if nums[left]*-1 == nums[right]:
                return nums[right]
            elif nums[left]*-1 > nums[right]:
                left += 1
            else:
                right -= 1

        return -1
