class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons = 0

        for a in arr:
            if a & 1:
                cons += 1
                if cons == 3:
                    return True
            else:
                cons = 0
        
        return False
