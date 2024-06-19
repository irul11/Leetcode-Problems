class Solution:
    def minDays(self, bd: List[int], m: int, k: int) -> int:
        ans = -1
        if m * k > len(bd):
            return ans
        
        def ispossible(mid):
            adj = 0
            tot = 0
            for b in bd:
                if mid >= b:
                    adj += 1
                    if adj == k:
                        tot += 1
                        adj = 0
                    if tot == m:
                        return True
                else:
                    adj = 0
                    
            return False
        
        left, right = 1, max(bd)

        while left < right:
            mid = (left + right) // 2
            
            if ispossible(mid):
                right = mid
            else:
                left = mid + 1

        return left
        