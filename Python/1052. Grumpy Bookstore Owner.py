class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total, ans = 0, 0

        for i in range(n):
            if grumpy[i] == 0 or i < minutes:
                total += customers[i]
            ans = total

        for i in range(1, n - minutes + 1):
            if grumpy[i - 1] == 1:
                total -= customers[i-1]
            if grumpy[i + minutes - 1] == 1:
                total += customers[i + minutes - 1]
            ans = max(ans, total)
            
        return ans
