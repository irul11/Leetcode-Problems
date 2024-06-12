from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Use Dijkstra's Algorithm

        adj_list = [[] for _ in range(n)]

        for flight in flights:
            adj_list[flight[0]].append((flight[1], flight[2]))
        
        distance = [float("inf") for _ in range(n)]
        distance[src] = 0

        # queue for visited city
        que = deque()
        que.append((0, (0, src)))

        while len(que):
            top = que.popleft()            

            if top[0] > k:
                continue

            for city in adj_list[top[1][1]]:
                if city[1] + top[1][0] < distance[city[0]]:
                    distance[city[0]] = city[1] + top[1][0]
                    que.append((top[0] + 1, (distance[city[0]], city[0])))
        
        
        return distance[dst] if distance[dst] != float("inf") else -1
    