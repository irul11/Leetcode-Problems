class Solution:
    def fractionAddition(self, e: str) -> str:
        def gcd(a, b):
            if a < b:
                a, b = b, a
            if b == 0:
                return a
            return gcd(b, a % b)
        
        def lcm(a, b):
            if a < b:
                a, b = b, a
            
            return (a * b) // gcd(a, b)
        
        denom = []
        num = []
        temp = ""
        i = 0
        while i < len(e):
            if e[i] == "/":
                denom.append("")
                i += 1
                while i < len(e) and e[i] not in ["+", "-"]:
                    denom[-1] += e[i]
                    i += 1
                denom[-1] = int(denom[-1])

            elif e[i] in ["+", "-"] or (i == 0):
                num.append("")
                while i < len(e) and e[i] != "/":
                    num[-1] += e[i]
                    i += 1
                num[-1] = int(num[-1])
            else:
                i += 1
        
        lccmm = denom[0]
        for i in range(1, len(denom)):
            lccmm = lcm(lccmm, denom[i])
        
        sums = 0
        for i in range(len(num)):
            sums += num[i] * (lccmm // denom[i])

        if sums == 0:
            return "0/1"

        g = gcd(abs(sums), lccmm)
        ans = str(sums//g) + "/" + str(lccmm//g)
        
        return ans
