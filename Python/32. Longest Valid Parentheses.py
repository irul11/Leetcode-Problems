class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result: int = 0
        array = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                array.append(i)
            else:
                array.pop()
                if not array:
                    array.append(i)
                else:
                    result = max(result, i - array[-1])
        return result

if __name__ == "__main__":
    solution = Solution()
    # For testing
    # long = solution.longestValidParentheses("))))())()()(()")
    # print(long)