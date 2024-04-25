class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        left = right - 1
        swap_array = [nums[right]]

        while left >= 0:
            swap_array.append(nums[left])
            
            if nums[left] < nums[left+1]:
                while nums[right] <= nums[left]:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                break
            left -= 1

        right = len(nums) - 1
        left += 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]        
            left += 1
            right -= 1   

if __name__ == "__main__":
    solution = Solution()
    # For testing
    # solution.nextPermutation([3, 2, 1]);
    # solution.nextPermutation([2,2,7,5,4,3,2,2,1]);