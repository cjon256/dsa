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

import (
	"reflect"
	"testing"
)

func listToLinkedList(nums []int) *ListNode {
	head := &ListNode{}
	cur := head
	for _, num := range nums {
		cur.Next = &ListNode{Val: num}
		cur = cur.Next
	}
	return head.Next
}

func Test_mergeKLists(t *testing.T) {
	type args struct {
		lists []*ListNode
	}
	tests := []struct {
		name string
		args args
		want *ListNode
	}{
		{
			name: "merge k sorted lists",
			args: args{
				lists: []*ListNode{
					listToLinkedList([]int{1, 4, 5}),
					listToLinkedList([]int{1, 3, 4}),
					listToLinkedList([]int{2, 6}),
				},
			},
			want: listToLinkedList([]int{1, 1, 2, 3, 4, 4, 5, 6}),
		},
		{
			name: "merge 1 sorted list",
			args: args{
				lists: []*ListNode{
					listToLinkedList([]int{1, 4, 5}),
				},
			},
			want: listToLinkedList([]int{1, 4, 5}),
		},
	}
	for _, tt := range tests {
		tt := tt
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()
			if got := mergeKLists(tt.args.lists); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("mergeKLists() = %v, want %v", got, tt.want)
			}
		})
	}
}
