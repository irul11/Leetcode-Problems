class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = 0
        maps = defaultdict(int)
        compound = ""
        nums = [1]
        
        i = len(formula) - 1
        while i >= 0:
            x = 1
            while self.isInt(formula[i]):
                n += int(formula[i]) * x
                x *= 10
                i -= 1
            
            s = formula[i]

            if s == ")":
                temp = 1 if n == 0 else n
                nums.append(temp * nums[-1])
                n = 0
            elif s == "(":
                nums.pop()
            elif 97 <= ord(s) <= 122:
                compound = s + compound
            elif 65 <= ord(s) <= 90:
                compound = s + compound
                temp = 1 if n == 0 else n
                maps[compound] += temp * nums[-1]
                compound = ""
                n = 0
            i -= 1
            
        ans = ""
        for m in sorted(maps.items()):
            ans += m[0] 
            if m[1] > 1:
                ans += str(m[1])

        return ans


    def isInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
            