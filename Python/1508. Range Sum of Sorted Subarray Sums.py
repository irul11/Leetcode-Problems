class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(len(nums)):
            prefix = 0
            for j in range(i, len(nums)):
                prefix += nums[j]
                arr.append(prefix)
        arr.sort()

        return sum(arr[left-1:right]) % 1_000_000_007
        