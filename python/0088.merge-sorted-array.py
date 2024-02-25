#  Category: algorithms
#  Level: Easy
#  Percent: 49.075558%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
#  Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
#  The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
#
#  Example 1:
#
#  Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#  Output: [1,2,2,3,5,6]
#  Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
#  The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
#
#
#  Example 2:
#
#  Input: nums1 = [1], m = 1, nums2 = [], n = 0
#  Output: [1]
#  Explanation: The arrays we are merging are [1] and [].
#  The result of the merge is [1].
#
#
#  Example 3:
#
#  Input: nums1 = [0], m = 0, nums2 = [1], n = 1
#  Output: [1]
#  Explanation: The arrays we are merging are [] and [1].
#  The result of the merge is [1].
#  Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
#
#
#
#  Constraints:
#
#
#  	nums1.length == m + n
#  	nums2.length == n
#  	0 <= m, n <= 200
#  	1 <= m + n <= 200
#  	-10⁹ <= nums1[i], nums2[j] <= 10⁹
#
#
#
#  Follow up: Can you come up with an algorithm that runs in O(m + n) time?


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1 = nums1[:m]
        n2 = nums2
        res = nums1
        i1 = i2 = i_res = 0
        while i1 < m and i2 < n:
            if n1[i1] < n2[i2]:
                res[i_res] = n1[i1]
                i1 += 1
            else:
                res[i_res] = n2[i2]
                i2 += 1
            i_res += 1
        while i1 < m:
            res[i_res] = n1[i1]
            i1 += 1
            i_res += 1
        while i2 < n:
            res[i_res] = n2[i2]
            i2 += 1
            i_res += 1
        #  end_marker

    def merge_by_copy_and_sort(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:
        nums1[m:] = nums2
        nums1.sort()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        res = [1, 2, 2, 3, 5, 6]
        self.s.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, res)

    def test_case_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        res = [1]
        self.s.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, res)

    def test_case_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        res = [1]
        self.s.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, res)

    def test_case_4(self):
        nums1 = [0, 0]
        m = 0
        nums2 = [1, 2]
        n = 2
        res = [1, 2]
        self.s.merge_by_copy_and_sort(nums1, m, nums2, n)
        self.assertEqual(nums1, res)

    def test_case_5(self):
        nums1 = [1, 0, 0]
        m = 1
        nums2 = [2, 3]
        n = 2
        res = [1, 2, 3]
        self.s.merge_by_copy_and_sort(nums1, m, nums2, n)
        self.assertEqual(nums1, res)


if __name__ == "__main__":
    unittest.main()
