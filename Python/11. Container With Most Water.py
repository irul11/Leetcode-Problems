class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] > height[right]:
                temp = height[right] * (right - left)
                right -= 1
            else:
                temp = height[left] * (right - left)
                left += 1
            # print(height[right])
            if temp > area:
                area = temp

        return area
