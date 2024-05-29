class Solution:
    def numSteps(self, s: str) -> int:
        bins = int(s, 2)
        ans = 0

        while bins > 1:
            ans += 1
            if bins & 1:
                bins += 1
            else:
                bins >>= 1

        return ans
        