#  Category: algorithms
#  Level: Medium
#  Percent: 65.998375%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
#
#
#  Example 1:
#  Input: temperatures = [73,74,75,71,69,72,76,73]
#  Output: [1,1,4,2,1,1,0,0]
#  Example 2:
#  Input: temperatures = [30,40,50,60]
#  Output: [1,1,1,0]
#  Example 3:
#  Input: temperatures = [30,60,90]
#  Output: [1,1,0]
#
#
#  Constraints:
#
#
#  	1 <= temperatures.length <= 10⁵
#  	30 <= temperatures[i] <= 100
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List, Tuple


#  start_marker
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # gotta try a monotonic stack backwards kinda approach
        stack: List[Tuple[int, int]] = []
        res = [0] * len(temperatures)
        for i, curr in enumerate(temperatures):
            while stack and stack[-1][0] < curr:
                _, old_i = stack.pop()
                res[old_i] = i - old_i
            stack.append((curr, i))
        return res
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
        expected = [1, 1, 4, 2, 1, 1, 0, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_case_2(self):
        temperatures = [30, 40, 50, 60]
        expected = [1, 1, 1, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_case_3(self):
        temperatures = [30, 60, 90]
        expected = [1, 1, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    def test_case_4(self):
        temperatures = [30, 60, 90, 30, 60, 90]
        expected = [1, 1, 0, 1, 1, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    # example where all temperatures are the same
    def test_case_5(self):
        temperatures = [30, 30, 30, 30, 30, 30]
        expected = [0, 0, 0, 0, 0, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    # example where all temperatures are lower than previous
    def test_case_6(self):
        temperatures = [30, 20, 10, 0, -10, -20]
        expected = [0, 0, 0, 0, 0, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)

    # example where all temperatures are higher than previous
    def test_case_7(self):
        temperatures = [30, 40, 50, 60, 70, 80]
        expected = [1, 1, 1, 1, 1, 0]
        result = Solution().dailyTemperatures(temperatures)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
