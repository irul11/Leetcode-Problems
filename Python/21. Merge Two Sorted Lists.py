# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list = ListNode()
        current = list
            
        while list1 and list2:
            if list1.val <= list2.val:
                current.val = list1.val
                current.next = list1.next
                list1 = list1.next
                if not list1:
                    current.next = list2
                    break
            else:
                current.val = list2.val
                current.next = list2.next
                list2 = list2.next
                if not list2:
                    current.next = list1
                    break
            current = current.next

        return list