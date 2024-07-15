class Solution:
    def minimumCost(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        h.sort()
        v.sort()

        sumh = sum(h)
        sumv = sum(v)
        ans = 0

        while h and v:
            if h[-1] > v[-1]:
                ans += h[-1] + sumv
                sumh -= h.pop()
            else:
                ans += v[-1] + sumh
                sumv -= v.pop()
        
        return ans + sumh + sumv
