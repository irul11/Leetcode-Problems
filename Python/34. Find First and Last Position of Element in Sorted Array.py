class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False) if left != -1 else -1
        return [left, right]
    
    def binary_search(
            self, 
            nums: list[int], 
            target: int, 
            to_left: bool # This parameter for determine the most left or the most right index of target in nums
    ) -> list[int]:
        index = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                index = mid
                if to_left:
                    right = mid-1
                else:
                    left = mid+1
        return index



if __name__ == "__main__":
    solution = Solution()
    # For testing
    # print(solution.searchRange(
    #     nums = [5,7,7,8,8,10,11,12],
    #     target = 10
    # ))