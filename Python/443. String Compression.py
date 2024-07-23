class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = []
        curr = chars[0]
        c = 1
        for i in range(1, len(chars)):
            if chars[i] != curr:
                ans += curr
                if c > 1:
                    ans += list(str(c))
                c = 1
                curr = chars[i]
            else:
                c += 1

        ans += curr
        if c > 1:
            ans += list(str(c))

        for j in range(len(ans)):
            chars[j] = ans[j]

        # print(ans)
        return len(ans)
