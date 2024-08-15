class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ret = [0, 0]

        for bill in bills:
            if bill == 5:
                ret[0] += 1
            elif bill == 10:
                if ret[0] == 0:
                    return False
                ret[1] += 1
                ret[0] -= 1
            else:
                if ret[1] > 0 and ret[0] > 0:
                    ret[1] -= 1
                    ret[0] -= 1
                elif ret[1] == 0 and ret[0] >= 3:
                    ret[0] -= 3
                else:
                    return False

        return True
