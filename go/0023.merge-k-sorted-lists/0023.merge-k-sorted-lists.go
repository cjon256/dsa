//  Category: algorithms
//  Level: Hard
//  Percent: 51.878803%

//  You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
//
//  Merge all the linked-lists into one sorted linked-list and return it.
//
//
//  Example 1:
//
//  Input: lists = [[1,4,5],[1,3,4],[2,6]]
//  Output: [1,1,2,3,4,4,5,6]
//  Explanation: The linked-lists are:
//  [
//    1->4->5,
//    1->3->4,
//    2->6
//  ]
//  merging them into one sorted list:
//  1->1->2->3->4->4->5->6
//
//
//  Example 2:
//
//  Input: lists = []
//  Output: []
//
//
//  Example 3:
//
//  Input: lists = [[]]
//  Output: []
//
//
//
//  Constraints:
//
//
//  	k == lists.length
//  	0 <= k <= 10⁴
//  	0 <= lists[i].length <= 500
//  	-10⁴ <= lists[i][j] <= 10⁴
//  	lists[i] is sorted in ascending order.
//  	The sum of lists[i].length will not exceed 10⁴.
//

package merge_k_sorted_lists_0023

type ListNode struct {
	Val  int
	Next *ListNode
}

// start_marker
func mergeKLists(lists []*ListNode) *ListNode {
	res := &ListNode{}
	cur := res
	for {
		min := -1
		for i, l := range lists {
			if l == nil {
				continue
			}
			if min == -1 || l.Val < lists[min].Val {
				min = i
			}
		}
		if min == -1 {
			break
		}
		cur.Next = lists[min]
		cur = cur.Next
		lists[min] = lists[min].Next
	}
	return res.Next
}

// end_marker
