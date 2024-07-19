class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1[0] = list(map(int, event1[0].split(":")))
        event1[1] = list(map(int, event1[1].split(":")))
        event2[0] = list(map(int, event2[0].split(":")))
        event2[1] = list(map(int, event2[1].split(":")))
        start1 = event1[0][0]*60 + event1[0][1]
        end1 = event1[1][0]*60 + event1[1][1]
        start2 = event2[0][0]*60 + event2[0][1]
        end2 = event2[1][0]*60 + event2[1][1]
        if start2 <= start1 <= end2 or start2 <= end1 <= end2 or start1 <= start2 <= end1 or start1 <= end2 <= end1:
            return True
        
        return False
        