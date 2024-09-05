class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sums = sum(rolls)
        l = n + len(rolls)

        res = mean * l - sums

        if res > 6 * n or res < n:
            return []
            
        ans = [res // n] * n
        res %= n
        
        i = 0
        while res > 0:
            ans[i] += 1
            res -= 1
            i += 1

        return ans
        