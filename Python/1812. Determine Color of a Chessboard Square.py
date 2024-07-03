class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        s, n = coordinates[0], int(coordinates[1])

        if s in ['a', 'c', 'e', 'g']:
            if n % 2 == 0:
                return True
            return False
        else:
            if n % 2 == 0:
                return False
            return True
