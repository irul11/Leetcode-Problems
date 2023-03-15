class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        result = []
        curr = 0

        while curr <= len(nums) - 3:
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue

            left = curr + 1
            right = len(nums) - 1

            if nums[curr] + nums[right] > nums[right] or nums[curr] + nums[right] < nums[curr]:
                return result
            while left < right:
                three_sum = nums[curr] + nums[left] + nums[right]

                if three_sum < 0:
                    left += 1

                elif three_sum > 0:
                    right -= 1

                elif three_sum == 0:
                    result.append([nums[curr], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1

            curr += 1

        return result