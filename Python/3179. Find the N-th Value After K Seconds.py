class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        arr = [1 for i in range(n)]

        while k > 0:
            for i in range(1,n):
                arr[i] = arr[i] + arr[i-1]
            k -= 1
            
        return arr[-1] % (10**9 + 7)
    