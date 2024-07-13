class Solution:
    def survivedRobotsHealths(self, pos: List[int], hp: List[int], dirc: str) -> List[int]:
        left, right = [], []
        for i in sorted(range(len(pos)), key=lambda i: pos[i]):
            if dirc[i] == "R":
                right.append(i)
            else:
                while right and hp[i] > hp[right[-1]]:
                    right.pop()
                    hp[i] -= 1
                if not right:
                    left.append(i)
                elif hp[i] == hp[right[-1]]:
                    right.pop()
                else:
                    hp[right[-1]] -= 1
                    
        return [hp[i] for i in sorted(left+right)]
