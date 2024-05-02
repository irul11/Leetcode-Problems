class Solution:
    def search(self, nums: list[int], target: int) -> int:
        result = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[right] >= nums[mid]:
                if nums[mid] < target <= nums[right] :
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return result
    
if __name__ == "__main__":
    solution = Solution()
    # For testing
    # print(solution.search(
    #     nums = [7,8,1,2,3,4,5],
    #     target = 8
    # ))