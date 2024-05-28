class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)        
        left = 0
        total = 0
        ans = 0
        
        for right in range(n):
            total += abs(ord(s[right]) - ord(t[right]))
            
            while total > maxCost:
                total -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
            