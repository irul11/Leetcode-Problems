class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sets = set(allowed)

        ans = 0
        
        for word in words:
            ans += 1
            for w in word:
                if w not in sets:
                    ans -= 1
                    break
        
        return ans
        