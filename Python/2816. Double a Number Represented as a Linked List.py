# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if head.val > 4:
            head = ListNode(1, head)
            curr = head.next

        while curr.next:
            additional = 0
            if curr.next.val > 4:
                additional = 1
            curr.val = (curr.val*2 + additional) % 10
            curr = curr.next
        curr.val =  (curr.val * 2) % 10
        return head