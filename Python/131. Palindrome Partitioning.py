class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        valids = []
        n = len(s)
        
        def dfs(s: str, left: int, valids: List[str], result: List[List[str]]):
            if left == n:
                result.append(valids)
                return
            
            for i in range(left, n):
                if isPalindrome(s[left:i+1]):
                    dfs(s, i+1, valids + [s[left:i+1]], result)

        def isPalindrome(s: str):
            return s == s[::-1]

        dfs(s, 0, valids, result)
        return result
