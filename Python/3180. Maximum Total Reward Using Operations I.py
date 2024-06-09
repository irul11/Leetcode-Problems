class Solution:
    def maxTotalReward(self, rv: List[int]) -> int:
        # This solution was obtained from next problem (so this is the optimal solution)
        nums = sorted(set(rv))
        x = 1

        for r in nums:
            valid = x & ((1 << r) - 1)
            # print(r, x, valid)
            x |= valid << r

        return x.bit_length() - 1
        