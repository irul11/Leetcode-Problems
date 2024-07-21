class Solution:
    color = []
    visited = []
    def dfs(self, v, graph):
        self.color[v] = 1
        for u in graph[v]:
            if self.color[u] == 0:
                if self.dfs(u, graph):
                    return True
            elif self.color[u] == 1:
                return True
        self.color[v] = 2
        return False

    def find_cycle(self, graph, n):
        self.color = [0] * n

        for v in range(n):
            if self.color[v] == 0 and self.dfs(v, graph):
                return True
        
        return False

    def dfs2(self, v, graph, ans) :
        self.visited[v] = True
        for u in graph[v]:
            if not self.visited[u]:
                self.dfs2(u, graph, ans)
        ans.append(v)
    

    def topological_sort(self, graph, n , ans):
        self.visited = [False] * n
        ans.clear()
        for i in range(n):
            if not self.visited[i]:
                self.dfs2(i, graph, ans)
        ans.reverse()


    def buildMatrix(self, k: int, rc: List[List[int]], cc: List[List[int]]) -> List[List[int]]:
        graph1 = [[] for _ in range(k)]
        graph2 = [[] for _ in range(k)]
        
        for r in rc:
            graph1[r[0]-1].append(r[1]-1)
        
        for c in cc:
            graph2[c[0]-1].append(c[1]-1)
        
        if self.find_cycle(graph1, k) or self.find_cycle(graph2, k):
            return []

        ans1, ans2 = [], []

        self.topological_sort(graph1, k, ans1)
        self.topological_sort(graph2, k, ans2)

        ans = [[0] * k for _ in range(k)]
        maps = dict()
        
        for i in range(k):
            maps[ans2[i]] = i
        
        # print(maps)
        
        for i in range(k):
            ans[i][maps[ans1[i]]] = ans1[i] + 1
        
        return ans
