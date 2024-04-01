class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1  # Count of unique elements
        slow = 0  # Pointer to track the last unique element

        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                k += 1

        del nums[slow + 1 :]  # Remove the remaining duplicates from the list

        return k
