class Solution:
    def reverseParentheses(self, s: str) -> str:
        brackets = []
        maps = defaultdict(str)

        for i in range(len(s)):
            if s[i] == "(":
                brackets.append(i)
                
            elif s[i] == ")":
                if not len(brackets) & 1:
                    maps[len(brackets)-1] = maps[len(brackets)] + maps[len(brackets)-1]
                else:
                    maps[len(brackets)-1] += maps[len(brackets)]
                del maps[len(brackets)]
                brackets.pop()
            else:
                if (len(brackets) & 1):
                    maps[len(brackets)] = s[i] + maps[len(brackets)]
                else:
                    maps[len(brackets)] += s[i]
            # print(maps)
        
        return maps[0]
