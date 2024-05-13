class Solution:
    def jump(self, nums: list[int]) -> int:
        result = 0
        left = right = 0

        while right < len(nums)-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])
                print(farthest)
            left = right + 1
            right = farthest
            # print(left, right)
            result += 1

        return result
