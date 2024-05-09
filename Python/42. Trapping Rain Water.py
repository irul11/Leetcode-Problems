class Solution:
    def trap(self, height: list[int]) -> int:
        left = []
        result = 0

        for i in range(len(height)):
            if len(left) > 0 and height[i] >= left[-1][1]:
                # right = [i, height[i]]
                temp = left.pop()[1]
                while len(left) > 0 and left[-1][1] <= height[i]:
                    l = left.pop()
                    result += ((l[1]-temp) * (i-l[0]-1))
                    temp = l[1]
                if len(left) > 0 and left[-1][1] >= height[i]:
                    result += ((height[i] - temp) * (i-left[-1][0]-1))
            left.append([i, height[i]])
            
        return result
