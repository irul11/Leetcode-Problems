# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        dumm = ListNode()
        curr = dumm
        if head == None or head.next == None:
            return head

        while True:
            temp1 = ListNode(head.val)
            temp2 = ListNode(head.next.val, temp1)
            curr.next = temp2
            curr = curr.next.next
            head = head.next.next
            if head == None:
                return dumm.next

            elif head.next == None:
                curr.next = head
                return dumm.next
