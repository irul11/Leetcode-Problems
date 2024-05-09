class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        sub_arr = []

        def backtracking(arr: list[int], target: int, sub_arr: list[int]):
            i = 0
            while i < len(arr):
                if arr[i] > target:
                    break
                if arr[i] == target:
                    result.append(sub_arr + [arr[i]])
                    break

                backtracking(arr[i+1:], target - arr[i], sub_arr + [arr[i]])

                # For prevent duplicate
                j = 1
                while i+j < len(arr) and arr[i+j] == arr[i]:
                    j += 1
                i += j
                
        backtracking(candidates, target, sub_arr)
        
        return result
