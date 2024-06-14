class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        sets = set()
        sets.add(nums[0])

        for i in range(1, len(nums)):
            if nums[i] in sets:
                temp = nums[i-1] + 1
                ans += (temp - nums[i])
                nums[i] = temp
            sets.add(nums[i])
            
        return ans
        