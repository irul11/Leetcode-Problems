# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        val = 0

        while fast:
            if fast.val == 0:
                slow = slow.next
                slow.val = val
                val = 0
            else:
                val += fast.val
        
            fast = fast.next
            
        slow.next = None

        return head.next
