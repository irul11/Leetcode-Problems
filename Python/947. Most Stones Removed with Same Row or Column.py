class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maps = defaultdict(int)
        islands = 0

        def find(x: int):
            if x != maps[x]:
                maps[x] = find(maps[x])
            return maps[x]

        def union(x: int, y: int):
            maps.setdefault(x, x)
            maps.setdefault(y, y)
            maps[find(x)] = find(y)
        
        for i, j in stones:
            union(i, ~j)
        
        return len(stones) - len({find(x) for x in maps})
        
    