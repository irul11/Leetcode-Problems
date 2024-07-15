class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        arr = [0 for _ in range(len(edges))]
        ans = maxx = 0

        for i in range(len(edges)):
            arr[edges[i]] += i
            # print(maxx, arr[edges[i]], ans)
            if maxx < arr[edges[i]]:
                maxx = arr[edges[i]]
                ans = edges[i]
            elif maxx == arr[edges[i]]:
                ans = min(edges[i], ans)
                
        return ans
