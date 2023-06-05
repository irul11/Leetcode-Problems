class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        current = 0

        while current < len(nums) - 3:
            print(current)
            if current > 0 and nums[current] == nums[current - 1]:
                current += 1
                continue
            left = current + 1

            while left < len(nums) - 2:
                if left > current + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                
                middle = left + 1
                right = len(nums) - 1

                while middle < right:
                    sum = nums[current] + nums[left] + nums[middle] + nums[right]
                    if sum > target:
                        right -= 1
                    elif sum < target:
                        middle += 1
                    else:
                        result.append([nums[current], nums[left], nums[middle], nums[right]])
                        
                        middle += 1
                        right -= 1

                        while middle < right and nums[middle] == nums[middle - 1]:
                            middle += 1
                        while right > middle and nums[right] == nums[right + 1]:
                            right -= 1
                left += 1
            current += 1

        return result