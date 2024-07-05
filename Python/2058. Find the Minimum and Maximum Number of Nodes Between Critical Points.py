# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left = mid = -1
        right = 1

        prev = head
        curr = prev.next
        mind = inf

        while curr and curr.next:
            if curr.val < prev.val and curr.val < curr.next.val or curr.val > prev.val and curr.val > curr.next.val:
                if left == -1:
                    left = right
                    mid = left
                else:
                    mind = min(right - mid, mind)
                    mid = right
            prev = curr
            curr = curr.next
            right += 1
        
        if mid == left:
            return [-1, -1]
            
        return [mind, mid-left]
