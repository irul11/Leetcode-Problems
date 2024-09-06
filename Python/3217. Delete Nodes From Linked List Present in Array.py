# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        sets = set(nums)

        head = ListNode(0, head)
        cur = head

        while cur:
            if cur.next and cur.next.val in sets:
                cur.next = cur.next.next if cur.next.next else None
            else:
                cur = cur.next
        
        return head.next
        