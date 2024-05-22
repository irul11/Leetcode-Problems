class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        arr = []
        self.solve(nums, 0, arr, result)
        return result
    
    def solve(self, nums: List[int], start: int, arr: List[int], result: List[List[int]]):
        print(start, arr, result)
        if start == len(nums):
            result.append(arr.copy())
            return

        self.solve(nums, start + 1, arr, result)
        arr.append(nums[start])
        self.solve(nums, start + 1, arr, result)
        arr.pop()
        