#  Category: algorithms
#  Level: Medium
#  Percent: 47.32611%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
#  You must write an algorithm that runs in O(n) time.
#
#
#  Example 1:
#
#  Input: nums = [100,4,200,1,3,2]
#  Output: 4
#  Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
#
#  Example 2:
#
#  Input: nums = [0,3,7,2,5,8,4,6,0,1]
#  Output: 9
#
#
#
#  Constraints:
#
#
#  	0 <= nums.length <= 10⁵
#  	-10⁹ <= nums[i] <= 10⁹
#
import unittest
from typing import Dict, List, NamedTuple

#  start_marker
from sortedcontainers import SortedSet


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = SortedSet(nums)
        max_interval = 0
        while num_set:
            start = end = num_set.pop(0)
            while end + 1 in num_set:
                end = num_set.pop(0)
            max_interval = max(max_interval, end - start + 1)
        return max_interval
        #  end_marker

    def longestConsecutive_ends(self, nums: List[int]) -> int:
        Ends = NamedTuple("Ends", (("s", int), ("e", int)))
        max_interval = 0
        interval_dict: Dict[int, Ends] = {}
        for n in nums:
            if n in interval_dict:
                continue
            start = end = n
            if n - 1 in interval_dict:
                before = interval_dict[n - 1]
                start = before.s
            if n + 1 in interval_dict:
                after = interval_dict[n + 1]
                end = after.e
            n_intvl = Ends(s=start, e=end)
            max_interval = max(max_interval, end - start + 1)
            interval_dict[n] = n_intvl
            if start != n:
                interval_dict[start] = n_intvl
            if end != n:
                interval_dict[end] = n_intvl
        return max_interval


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [100, 4, 200, 1, 3, 2]
        expected = 4
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        expected = 9
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_3(self):
        nums = [1, 2, 0, 1]
        expected = 3
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_4(self):
        nums = [1, 2, 0, 1, 2]
        expected = 3
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_5(self):
        nums = [1, 2, 0, 1, 2, 3]
        expected = 4
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_6(self):
        nums = [1, 2, 0, 1, 2, 3, 4]
        expected = 5
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_7(self):
        nums = []
        expected = 0
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_8(self):
        nums = [1]
        expected = 1
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_9(self):
        nums = [1, 2]
        expected = 2
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_10(self):
        nums = [1, 2, 3]
        expected = 3
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)

    def test_case_11(self):
        nums = [1, 6, 3, 4]
        expected = 2
        result = Solution().longestConsecutive(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
