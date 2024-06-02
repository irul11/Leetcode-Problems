class Solution:
    def clearStars(self, s: str) -> str:
        q = []
        heapq.heapify(q)
        arr = []
        for i in range(len(s)):
            if s[i] != "*":
                heapq.heappush(q, (ord(s[i]), -i))
            else:
                temp = heapq.heappop(q)
                arr[-temp[1]] = "-"
            arr.append(s[i])
                
        ans = ""
        for c in arr:
            if ord(c) >= ord("a"):
                ans += c
            
        return ans
