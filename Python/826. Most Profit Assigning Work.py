class Solution:
    def maxProfitAssignment(self, d: List[int], p: List[int], w: List[int]) -> int:
        arr = [(d[i], p[i]) for i in range(len(d))]
        arr.sort()
        w.sort()

        ans = left = maxx = 0
        for i in range(len(w)):
            k = w[i]            
            while left < len(arr) and arr[left][0] <= k:
                maxx = max(maxx, arr[left][1])
                left += 1
                
            ans += maxx
            
        return ans
