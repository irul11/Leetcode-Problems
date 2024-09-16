class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []

        for t in timePoints:
            curr = t.split(":")
            arr.append((int(curr[0]), int(curr[1])))
        
        arr.sort()
        arr.append((arr[0][0]+24, arr[0][1]))
        ans = 24 * 60 + 1
        for i in range(1, len(arr)):
            minutes = 0
            if arr[i][1] < arr[i-1][1]:
                minutes += arr[i][1] + 60 - arr[i-1][1]
                minutes += (arr[i][0] - 1 - arr[i-1][0]) * 60
            else:
                minutes += (arr[i][0] - arr[i-1][0]) * 60 + (arr[i][1] - arr[i-1][1])
                
            ans = min(ans, minutes)
            
        return ans
        