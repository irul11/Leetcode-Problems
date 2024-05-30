class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        maps = defaultdict(list)
        maps[0].append(-1)
        ans = 0
        xor_sum = 0

        for k in range(len(arr)):
            xor_sum ^= arr[k]
            # print(maps, xor_sum ^ 0)
            for i in maps[xor_sum^0]:
                ans += k - i - 1
            maps[xor_sum].append(k)
        
        return ans

