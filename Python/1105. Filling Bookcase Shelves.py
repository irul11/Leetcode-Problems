class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        ans = 0

        dp = [0] * (len(books) + 1)

        for i in range(1, len(books)+1):
            width, height = books[i-1]
            dp[i] = dp[i-1] + height
            
            j = i - 1
            while j > 0 and width + books[j-1][0] <= shelfWidth:
                height = max(height, books[j-1][1])
                width += books[j-1][0]
                dp[i] = min(dp[i], dp[j-1] + height)
                print(i, j-1, dp[i])
                j -= 1
        # print(dp)
        return dp[-1]
