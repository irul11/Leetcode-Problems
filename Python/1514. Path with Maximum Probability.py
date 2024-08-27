class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        p, g = [0.0] * n, defaultdict(list)

        for i, (a, b) in enumerate(edges):
            g[a].append((b, i))
            g[b].append((a, i))
        
        p[start_node] = 1.0
        heap = [(-p[start_node], start_node)]

        while heap:
            prob, curr = heapq.heappop(heap)
            if curr == end_node:
                return -prob
            for neighbor, i in g.get(curr, []):
                if -prob * succProb[i] > p[neighbor]:
                    p[neighbor] = -prob * succProb[i]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
        
        return 0.0
        