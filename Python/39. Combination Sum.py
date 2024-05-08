class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        temp = []
        def bactracking(arr, target, temp):
            for i in range(len(arr)):
                div = target // arr[i]

                if div == 0 or len(arr) == 0:
                    continue

                for j in range (1, div + 1):
                    if arr[i] * j == target:
                        result.append(temp + [arr[i]]*j)
                        continue
                    
                    bactracking(arr[:i], target - arr[i]*j, temp + [arr[i]]*j)
        bactracking(candidates, target, temp)
        return result

if __name__ == "__main__":
    solution = Solution()
    # For testing
    print("result:", solution.combinationSum([2,3,5], 11))