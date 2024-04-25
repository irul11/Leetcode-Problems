class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = self.increase(nums)[:]
        print(nums)
    
    def increase(self, nums: list) -> list:   
        if len(nums) == 1:
            return nums
        
        right = len(nums) - 1
        left = right - 1
        swap_array = [nums[right]]

        while left >= 0:
            swap_array.append(nums[left])
            
            if nums[left] < nums[left+1]:
                if right == left + 1:
                    nums[left], nums[right] = nums[right], nums[left]
                    return nums
                else:
                    if nums[right] > nums[left]:
                        nums[left], nums[left+1], nums[right] = nums[right], nums[left], nums[left+1]
                        if right - (left + 1) >= 2:
                            nums[left+2:right] = self.increase(nums[left+2:right])
                        return nums
                    else:
                        arr_small = []
                        while nums[right] <= nums[left]:
                            arr_small.append(nums[right])
                            right -= 1
                        arr_big = self.increase(nums[:right+1])
                        return arr_big[:left+1] + arr_small + arr_big[left+1:]

            left -= 1
        return swap_array

if __name__ == "__main__":
    solution = Solution()
    # solution.nextPermutation([1,5,1]);
    solution.nextPermutation([2,2,7,5,4,3,2,2,1]);