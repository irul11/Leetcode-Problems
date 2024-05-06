class Solution:
    def countAndSay(self, n: int) -> str:     
        if n == 1:
            return "1"
        return self.rle(self.countAndSay(n - 1))
    
    def rle(self, str: str) -> str:
        count, curr = 0, str[0]
        temp = ""
        for s in str:
            if curr == s:
                count += 1
            else:
                temp += f'{count}{curr}'
                count = 1
                curr = s
        temp += f'{count}{curr}'
        
        return temp
        

if __name__ == "__main__":
    solution = Solution()
    # For testing
    # print("result:", solution.countAndSay(5))