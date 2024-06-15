class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        arr = [(capital[i], profits[i]) for i in range(n)]
        arr.sort()

        heaps = []
        heapq.heapify(heaps)

        i = 0
        for _ in range(k):
            while i < n and arr[i][0] <= w:
                heapq.heappush(heaps, -arr[i][1]) 
                i += 1
            if not heaps:
                break

            w -= heapq.heappop(heaps)

        return w
