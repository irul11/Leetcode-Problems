class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        ans = nb

        while nb >= ne:
            ans += nb // ne
            res = nb % ne
            nb //= ne
            nb += res

        return ans
        