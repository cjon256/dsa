#  Category: algorithms
#  Level: Medium
#  Percent: 59.402668%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#
#  There is only one repeated number in nums, return this repeated number.
#
#  You must solve the problem without modifying the array nums and uses only constant extra space.
#
#
#  Example 1:
#
#  Input: nums = [1,3,4,2,2]
#  Output: 2
#
#
#  Example 2:
#
#  Input: nums = [3,1,3,4,2]
#  Output: 3
#
#
#
#  Constraints:
#
#
#  	1 <= n <= 10⁵
#  	nums.length == n + 1
#  	1 <= nums[i] <= n
#  	All the integers in nums appear only once except for precisely one integer which appears two or more times.
#
#
#
#  Follow up:
#
#
#  	How can we prove that at least one duplicate number must exist in nums?
#  	Can you solve the problem in linear runtime complexity?
#


import unittest

# from leetopenlib.linked_list import ListNode, list_to_linked_list, linked_list_to_list
# from leetopenlib.tree import TreeNode, list_to_tree, tree_to_list
# from leetopenlib.tree import TreeNode, liststr_to_tree, tree_to_liststr, pretty_print_tree
# from leetopenlib.graph import Node, graph_to_adj_list, adj_list_to_graph
from typing import List


#  start_marker
class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
        #  end_marker

    def findDuplicate_set(self, nums: List[int]) -> int:
        unneeded_set = set()
        for num in nums:
            if num in unneeded_set:
                return num
            unneeded_set.add(num)
        return -1
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 3, 4, 2, 2]
        expected = 2
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_2(self):
        nums = [3, 1, 3, 4, 2]
        expected = 3
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_3(self):
        nums = [1, 1]
        expected = 1
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_4(self):
        nums = [1, 3, 1, 2]
        expected = 1
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_5(self):
        nums = [1, 4, 1, 3, 2]
        expected = 1
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_6(self):
        nums = [4, 4, 1, 3, 2]
        expected = 4
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_7(self):
        nums = [4, 1, 2, 3, 4]
        expected = 4
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)

    def test_case_8(self):
        nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
        expected = 9
        result = Solution().findDuplicate(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
