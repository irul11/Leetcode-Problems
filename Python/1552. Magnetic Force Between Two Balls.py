class Solution:
    def maxDistance(self, p: List[int], m: int) -> int:
        p.sort()
        
        ans = 0
        
        left, right = 1, p[-1] - p[0]
        while left <= right:
            mid = (left + right) // 2
            balls = 1
            prevIndex = 0
            for i in range(1, len(p)):
                if p[i] - p[prevIndex] >= mid:
                    balls += 1
                    prevIndex = i
                    
            if balls >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
            
        return ans
        