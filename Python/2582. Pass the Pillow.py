class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ans = 1
        add = 1
        for i in range(time):
            ans += add
            if ans == n or ans == 1:
                add *= - 1
        return ans