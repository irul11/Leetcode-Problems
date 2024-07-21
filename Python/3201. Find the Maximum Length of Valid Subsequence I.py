class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd = even = both = 0
        c = nums[0] % 2

        for num in nums:
            if num & 1:
                odd += 1
            else:
                even += 1 

            if num % 2 == c:
                both += 1
                c = 1 - c 
        
        return max(odd, even, both)
