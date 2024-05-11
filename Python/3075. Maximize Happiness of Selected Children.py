from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        j = 0
        result = 0
        for i in range(k):
            if happiness[i] - j < 0:
                break
            result += (happiness[i] - j)
            j += 1

        return result