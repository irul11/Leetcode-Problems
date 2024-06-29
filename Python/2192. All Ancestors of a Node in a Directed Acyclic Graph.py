class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = [set() for _ in range(n)]
        incoming = [0]*(n)

        for start, end in edges:
            graph[start].append(end)
            ancestors[end].add(start)
            incoming[end]+=1
        
        q = deque()
        for node in range(n):
            if not incoming[node]:
                q.append(node)

        while q:
            node = q.popleft()
            for adjacent_node in graph[node]:
                ancestors[adjacent_node].update(ancestors[node])
                incoming[adjacent_node] -=1
                if not incoming[adjacent_node]:
                    q.append(adjacent_node)
                    
        result = []
        for node in range(n):
            result.append(sorted(ancestors[node]))
        return result
