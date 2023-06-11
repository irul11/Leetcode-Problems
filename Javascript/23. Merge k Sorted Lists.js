/**
 * Definition for singly-linked list.

 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if (lists.length === 0) {
        return null;
    } else if (lists.length === 1) {
        return lists[0];
    }
    const mid = Math.floor(lists.length / 2);

    const left = mergeKLists(lists.slice(0, mid));
    const right = mergeKLists(lists.slice(mid,));

    return merge(left, right)
};

var merge = function(left, right) {
    list = new ListNode();
    curr = list;
    
    while (left && right) {
        if (left.val < right.val) {
            curr.next = left;
            left = left.next;
        } else {
            curr.next = right;
            right = right.next; 
        }
        curr = curr.next;
    }
    if (!left) {
        curr.next = right;
    } else {
        curr.next = left;
    }
    return list.next;
}