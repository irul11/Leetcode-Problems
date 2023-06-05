# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: 
            fast, slow = fast.next, slow.next
            print(head)
        slow.next = slow.next.next
        print(head)
        return head
    
    # Below is the way to make linked list form an array (if head is an array)
    # linked_list = ListNode(head[0])
    
    # node = linked_list
    # for i in range(1, len(head)):
    #     if i == n:
    #         continue
    #     current = ListNode(head[i])
    #     node.next = current
    #     node = node.next

