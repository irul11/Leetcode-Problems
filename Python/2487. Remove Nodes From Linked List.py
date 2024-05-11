# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        curr = head

        # Reverse the List 
        while curr:
            next_node = curr.next
            curr.next = reverse
            reverse = curr
            curr = next_node

        curr2 = reverse
        max_val = float("-inf")
        head = None
        
        # Create new list 
        while curr2:
            if curr2.val >= max_val:
                max_val = curr2.val

                # This same logic as reverse above
                next_node = curr2.next
                curr2.next = head
                head = curr2
                curr2 = next_node

            else:
                curr2 = curr2.next
                
        return head
