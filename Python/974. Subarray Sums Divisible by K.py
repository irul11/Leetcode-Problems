class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)

        maps = defaultdict(int)
        maps[0] += 1
        sums = 0

        for i in range(n):
            sums += nums[i]
            if sums % k in maps:
                ans += maps[sums%k]
            maps[sums%k] += 1
            # print(sums, maps, ans)
        
        return ans           
