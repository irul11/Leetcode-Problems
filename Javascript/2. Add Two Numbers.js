/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let result = new ListNode()
    let curr = result
    let res = 0

    while (l1 || l2) {
        let temp = res
        if (l1) {
            temp += l1.val
            l1 = l1.next
        }
        if (l2) {
            temp += l2.val
            l2 = l2.next
        }
        res = temp > 9 ? 1 : 0

        curr.next = new ListNode(temp%10)
        curr = curr.next
    }
    if (res === 1) {
        curr.next = new ListNode(1)
    }
    return result.next
};