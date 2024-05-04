class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return mid + 1 if target > nums[mid] else mid
    


if __name__ == "__main__":
    solution = Solution()
    # For testing
    print(solution.searchInsert(
        nums=[1,3,5,6],
        target = 0
    ))