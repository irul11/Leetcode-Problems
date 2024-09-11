class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bos = start ^ goal
        ans = 0
        while bos > 0:
            ans += bos & 1
            bos >>= 1

        return ans
        