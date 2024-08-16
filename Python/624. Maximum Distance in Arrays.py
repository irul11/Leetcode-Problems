class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays = [[arrays[i], i] for i in range(len(arrays))]
        arr1 = sorted(arrays, key=lambda x: x[0][0])
        arr2 = sorted(arrays, key=lambda x: x[0][-1])

        ans = 0
        if arr1[0][1] == arr2[-1][1]:
            ans = max(
                abs(arr1[0][0][0] - arr2[-2][0][-1]),
                abs(arr1[1][0][0] - arr2[-1][0][-1]),
            )
        else:
            ans = abs(arr1[0][0][0] - arr2[-1][0][-1])
            
        return ans
        