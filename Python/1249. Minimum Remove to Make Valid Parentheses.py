class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = []
        result = ""

        for i in range(len(s)):
            if s[i] == "(":
                arr.append(len(result))
                result += s[i]
            elif s[i] == ")":
                if arr:
                    arr.pop()
                    result += s[i]
            else:
                result += s[i]
                
        while arr:        
            i = arr.pop()
            result = result[:i] + result[i+1:]
            
        return result
        