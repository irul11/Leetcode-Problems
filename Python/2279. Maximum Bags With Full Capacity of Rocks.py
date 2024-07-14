class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ar: int) -> int:
        gaps = []
        ans = 0

        for i in range(len(capacity)):
            gaps.append(capacity[i] - rocks[i])
        
        gaps.sort()

        for gap in gaps:
            if gap <= ar:
                ans += 1
                ar -= gap
            else:
                break

        return ans
        