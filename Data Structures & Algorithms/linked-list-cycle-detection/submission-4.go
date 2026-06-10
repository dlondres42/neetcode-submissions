/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
    curr := head
	fast := head.Next

	for curr != nil && fast != nil{
		if curr == fast {
			return true
		}
		curr = curr.Next
		if fast.Next != nil{
			fast = fast.Next.Next
		} else {
			return false
		}
	}

	return false
}
