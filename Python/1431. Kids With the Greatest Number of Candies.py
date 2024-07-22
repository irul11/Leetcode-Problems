class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        ans = [False]*len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxx:
                ans[i] = True

        return ans
