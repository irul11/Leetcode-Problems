class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        k = k % sums

        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
            