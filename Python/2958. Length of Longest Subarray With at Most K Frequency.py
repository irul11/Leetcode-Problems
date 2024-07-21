from typing import List
from collections import defaultdict, deque

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(deque)
        result = 0
        left = 0

        for i in range(n):
            if len(count[nums[i]]) == k:
                length = i - left
                if length > result:
                    result = length
                temp = count[nums[i]].popleft()
                # if current popleft value < left, then do nothing
                # else left equal to current popleft value + 1
                left = temp + 1 if temp >= left else left 
            count[nums[i]].append(i)

        return result if n-left < result else n-left
        