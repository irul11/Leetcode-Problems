class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0

        for log in logs:
            if log != "../":
                if log != "./":
                    ans += 1
            elif ans == 0:
                continue
            else:
                ans -= 1
            # print(ans)

        return ans
