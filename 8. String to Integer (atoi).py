class Solution:
    def myAtoi(self, s: str) -> int:
        import re
        pengkali = 1
        s = s.strip()
        if re.match(r'^-', s):
            s = s[1:]
            pengkali = -1
        elif re.match(r'^\+', s):
            s = s[1:]
        # print(s)
        digit = re.match(r'(^\d+)', s)
        if digit:
            if int(digit.group()) * pengkali > 2**31 -1:
                return 2**31-1
            elif int(digit.group()) * pengkali < -(2**31):
                return -(2**31)
            else:
                return int(digit.group()) * pengkali
        else:
            return 0
