# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        result = ListNode()
        curr2 = result

        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr = curr.next
                # If the next duplicate is null or not equal to current.val, current will jump to next node
                if not curr.next or curr.next and curr.val != curr.next.val:
                    curr = curr.next
                continue
                
            curr2.next = ListNode(curr.val)
            curr2 = curr2.next
            curr = curr.next

        return result.next
    