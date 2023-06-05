import math
class Solution(object):
    def checkStraightLine(self, coordinates):
        if len(coordinates) <= 2:
            return True
        dx1 = coordinates[1][0] - coordinates[0][0]
        dy1 = coordinates[1][1] - coordinates[0][1]
        m1 = math.atan(dx1/dy1) if dy1 != 0 else float("inf")
        for i in range (2, len(coordinates)):
            dx2 = coordinates[i][0] - coordinates[i-1][0]
            dy2 = coordinates[i][1] - coordinates[i-1][1]
            m2 = math.atan(dx2/dy2) if dy2 != 0 else float("inf")
            if m1 != m2:
                return False
        return True