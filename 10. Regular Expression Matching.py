class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # import re
        if re.match(r'^{}$'.format(p), s):
            return True
        else:
            return False
