class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        def heap_permutation(arr: list, size: int):
            # print(arr, size)
            if size == 1:
                result.append(arr.copy())
                # print(arr)
                return
            
            for i in range(size):
                heap_permutation(arr, size-1)

                if size % 2 == 0:
                    arr[i], arr[size-1] = arr[size-1], arr[i]
                else:
                    arr[0], arr[size-1] = arr[size-1], arr[0]
        
        heap_permutation(nums, len(nums))
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.permute(
        [1,2,3]
    ))