class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        x = [arr[0]]
        for i in range(1, len(arr)):
            x.append(x[-1] ^ arr[i])

        ans = []
        for q in queries:
            k, l = q
            if k <= 0:
                ans.append(x[l])
            else:
                ans.append(x[k-1] ^ x[l])

        return ans
            