class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small, big = inf, inf

        for num in nums:
            if num <= small:
                small = num
            elif num <= big:
                big = num
            else:
                return True
            # print(small, big)
        
        return False
