import heapq
from typing import List

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio = [(wage[i]/quality[i], quality[i]) for i in range(len(quality))]
        ratio.sort()
        heaps = []
        heapq.heapify(heaps)
        
        quality_sum, max_ratio = 0, 0.0
        
        for i in range(k):
            quality_sum += ratio[i][1]
            heapq.heappush(heaps, -1*ratio[i][1])
            max_ratio = ratio[i][0]
            
        result = max_ratio * quality_sum

        for i in range(k, len(ratio)):
            quality_sum += ratio[i][1] - (heapq.heappop(heaps) * -1)
            heapq.heappush(heaps, -1*ratio[i][1])
            max_ratio = ratio[i][0]

            if i + 1 >= k:
                result = min(result, max_ratio * quality_sum)

        return result