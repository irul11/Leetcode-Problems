/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
	let dumm = new ListNode();
	let curr = dumm;
	let stop = false;

	while (true) {
		let temp = new ListNode();
		let temp2 = temp;
		temp2.next = head;
		let temp3 = head;

		for (let i = 0; i < k; i++) {
			if (curr.next !== null) {
				curr = curr.next;
			}
			temp2 = temp2.next;
			if (temp2 === null) {
				stop = true;
				break;
			}
			head = head.next;
		}

		if (stop) {
			while (curr.next) {
				curr = curr.next;
			}
			curr.next = temp3;
			break;
		}

		temp2.next = null;
		curr.next = reverse(temp.next);
	}
	return dumm.next;
};

var reverse = function(head) {
	let prevNode = null;
	let currentNode = head;
	while (currentNode) {
		const nextNode = currentNode.next;
		currentNode.next = prevNode;
		prevNode = currentNode;
		currentNode = nextNode;
	}
	return prevNode;
}