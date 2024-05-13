class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        last_match = 0
        star_index = -1

        while i < len(s):
            print(s[i], p[j], star_index, last_match)
            if j < len(p) and (p[j] == "?" or p[j] == s[i]):
                i += 1
                j += 1
                
            elif j < len(p) and  p[j] == "*":
                last_match = i
                star_index = j
                j += 1
            
            elif star_index != -1:
                j = star_index + 1
                i = last_match + 1
                last_match += 1
            else:
                return False
            
        while j < len(p) and p[j] == "*":
            j += 1
            
        return j == len(p)
    