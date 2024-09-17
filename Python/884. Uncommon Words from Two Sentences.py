class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        maps = defaultdict(int)
        for s in (s1 + " " + s2).split():
            maps[s] += 1 

        ans = []
        for k in maps:
            if maps[k] == 1:
                ans.append(k)
        
        return ans
        