class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        arr = [1] * len(nums)

        for i in range(len(nums)):
            arr[i] *= prod
            prod *= nums[i]
        print(arr)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            arr[i] *= prod
            prod *= nums[i]
        
        return arr
