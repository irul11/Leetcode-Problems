class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dig = ""
        for t in s:
            dig += str(ord(t) - 96)
            
        for _ in range(k):
            temp = 0
            for u in dig:
                temp += int(u)
            dig = str(temp)
        
        return int(dig)
        