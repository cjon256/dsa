//  Category: algorithms
//  Level: Easy
//  Percent: 77.11521%

//  Given the head of a singly linked list, return the middle node of the linked list.
//
//  If there are two middle nodes, return the second middle node.
//
//
//  Example 1:
//
//  Input: head = [1,2,3,4,5]
//  Output: [3,4,5]
//  Explanation: The middle node of the list is node 3.
//
//
//  Example 2:
//
//  Input: head = [1,2,3,4,5,6]
//  Output: [4,5,6]
//  Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
//
//
//
//  Constraints:
//
//
//  	The number of nodes in the list is in the range [1, 100].
//  	1 <= Node.val <= 100
//

//  start_marker
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        return head;
    }
}
//  end_marker

pub struct Solution;
use cargo_leet::ListNode;
// https://stackoverflow.com/questions/56914752/how-to-convert-a-linked-list-of-optionboxlistnode-to-a-veci32
// thx Shepmaster
pub fn list_to_vec(mut value: &Option<Box<ListNode>>) -> Vec<i32> {
    let mut v = Vec::new();
    while let Some(n) = value {
        v.push(n.val);
        value = &n.next;
    }
    v
}

#[cfg(test)]
mod tests {
    use super::*;
    use cargo_leet::ListHead;

    use rstest::rstest;

    #[rstest]
    #[case(ListHead::from(vec![1,2,3,4,5]).into(), Some(vec![3,4,5]))]
    #[case(ListHead::from(vec![1,2,3,4,5,6]).into(), Some(vec![4,5,6]))]
    #[case(ListHead::from(vec![]).into(), None)]
    fn case(#[case] head: Option<Box<ListNode>>, #[case] expected: Option<Vec<i32>>) {
        let actual = Solution::middle_node(head);
        let vec_actual = list_to_vec(&actual);
        if actual.is_some() {
            assert_eq!(vec_actual, expected.unwrap());
        } else {
            assert!(actual.is_none() && expected.is_none());
        }
    }
}
