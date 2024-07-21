class Solution:
    def validStrings(self, n: int) -> List[str]:
        def bt(pref, ans):
            if len(pref) == n:
                ans.append(pref)
                return
            
            if len(pref) > 0 and pref[-1] != "0":
                bt(pref + "0", ans)
            bt(pref + "1", ans)
        
        ans = []
        bt("0", ans)
        bt("1", ans)
        # print(ans)
        return ans
        