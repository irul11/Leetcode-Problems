class Solution:
    def threeSumClosest(self, nums, target) -> int:
        if len(nums) < 3:
            return []

        nums.sort()
        result = float('inf')
        curr = 0

        while curr <= len(nums) - 3:
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue

            left = curr + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[curr] + nums[left] + nums[right]

                if three_sum < target:
                    left += 1

                elif three_sum > target:
                    right -= 1

                else:
                    return three_sum

                if abs(three_sum - target) < abs(result - target):
                    result = three_sum

            curr += 1

        return result

