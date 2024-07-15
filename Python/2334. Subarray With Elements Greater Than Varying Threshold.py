class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n, stack = len(nums), [-1]
        nums.append(0)
        for i,num in enumerate(nums):
            while nums[stack[-1]] > num:
                bar = nums[stack.pop()]
                if bar*(i-stack[-1]-1) > threshold:
                    return i-stack[-1]-1
            
            if nums[stack[-1]] == num:
                stack[-1] = i
            else:
                stack.append(i)
            print(stack)
        return -1
