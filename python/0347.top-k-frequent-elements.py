#  Category: algorithms
#  Level: Medium
#  Percent: 62.719578%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#
#  Example 1:
#  Input: nums = [1,1,1,2,2,3], k = 2
#  Output: [1,2]
#  Example 2:
#  Input: nums = [1], k = 1
#  Output: [1]
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁵
#  	-10⁴ <= nums[i] <= 10⁴
#  	k is in the range [1, the number of unique elements in the array].
#  	It is guaranteed that the answer is unique.
#
#
#
#  Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in Counter(nums).most_common(k)]
        #  end_marker


import unittest
from collections import Counter
from typing import List


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected)

    def test_2(self):
        nums = [1]
        k = 1
        expected = [1]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected)


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
