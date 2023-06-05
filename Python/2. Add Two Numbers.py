# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # link1 = ListNode(l1.val + l2.val)
        link1 = ListNode(l1.val + l2.val, ListNode(0))
        if link1.val > 9:
            link1.val -= 10
            link1.next = ListNode(1)
        if l1.next is None and l2.next is None:
            return ListNode(l1.val + l2.val) if link1.next.val == 0 else link1

        while l1.next is not None or l2.next is not None:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next

            current = link1
            while current.next.next is not None:
                current = current.next
            jumlah = l1.val + l2.val + current.next.val
            if jumlah > 9:
                # if l1.next is None:
                #     current.next = ListNode(jumlah-10)
                # else:
                current.next = ListNode(jumlah - 10, ListNode(1))
            else:
                if l1.next is None and l2.next is None:
                    current.next = ListNode(jumlah)
                else:
                    current.next = ListNode(jumlah, ListNode(0))

            # print(current.next.val)

        return link1

