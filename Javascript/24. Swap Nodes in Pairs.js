/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
	let dumm = curr = new ListNode();
	if (head === null || head.next === null) return head;

	while (true) {
		const temp1 = new ListNode(head.val);
		const temp2 = new ListNode(head.next.val, temp1);

		curr.next = temp2;

		curr = curr.next.next;
		head = head.next.next;

		if (!head) {
			return dumm.next;
		} else if (!head.next) {
			curr.next = head;
			return dumm.next;
		}
	}
};