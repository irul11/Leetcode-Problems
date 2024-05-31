class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        maps = defaultdict(int)
        n = len(nums)

        for i in range(n):
            maps[nums[i]] += 1
            if maps[nums[i]] > 1:
                del maps[nums[i]]
                
        return list(maps.keys())
