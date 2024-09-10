# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if a < b:
                a, b = b, a

            mod = a % b
            a, b = b, mod
            if b == 0:
                return a
            return gcd(a, b)

        curr = head
        while curr:
            if curr.next:
                x = gcd(curr.val, curr.next.val)
                temp = curr.next
                curr.next = ListNode(x, temp)
                curr = curr.next.next
            else:
                curr = curr.next

        return head
