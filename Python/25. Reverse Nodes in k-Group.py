# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head, k: int):
        dumm = curr = ListNode()
        stop = False

        while True:
            temp = temp2 = ListNode()
            temp2.next = head
            temp3 = head

            for _ in range(k):
                if curr.next != None:
                    curr = curr.next
                temp2 = temp2.next
                if temp2 == None:
                    stop = True
                    break
                head = head.next

            if stop:
                while curr.next:
                    curr = curr.next
                curr.next = temp3
                break

            temp2.next = None
            curr.next = self.reverse(temp.next)

        return dumm.next

    def reverse(self, listnode):
        previous_node = None
        current_node = listnode
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node
