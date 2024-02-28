#  Category: algorithms
#  Level: Medium
#  Percent: 46.870743%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#
#  Example 1:
#
#  Input: nums = [0,1]
#  Output: 2
#  Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#
#
#  Example 2:
#
#  Input: nums = [0,1,0]
#  Output: 2
#  Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
#
#  Constraints:
#
#
#  	1 <= nums.length <= 10⁵
#  	nums[i] is either 0 or 1.
#

import unittest
from collections import defaultdict
from typing import List


#  start_marker
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        posneg: defaultdict[int, List[int]] = defaultdict(lambda: [])

        def add_to_posneg(key: int, val: int) -> None:
            arr = posneg[key]
            if len(arr) < 2:
                arr.append(val)
            else:
                arr[1] = val

        add_to_posneg(0, 0)
        total = 0
        for i, n in enumerate(nums):
            if n == 0:
                total -= 1
            else:
                total += 1
            add_to_posneg(total, i + 1)
        res = 0
        for _, v in posneg.items():
            dist = v[-1] - v[0]
            res = max(res, dist)
        return res
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [0, 1]
        res = 2
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_2(self):
        nums = [0, 1, 0]
        res = 2
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_3(self):
        nums = [0, 1, 0, 1]
        res = 4
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_4(self):
        nums = [0, 0, 1, 0, 0, 0, 1, 1]
        res = 6
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_5(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 0]
        res = 0
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_6(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1]
        res = 0
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_7(self):
        nums = [0, 1, 1, 1, 1, 1, 1, 1]
        res = 2
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_8(self):
        nums = [0, 0, 0, 0, 0, 0, 0, 1]
        res = 2
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_9(self):
        nums = [0, 0, 0, 0, 0, 0, 1, 1]
        res = 4
        self.assertEqual(Solution().findMaxLength(nums), res)

    def test_case_10(self):
        nums = [0, 0, 0, 0, 0, 1, 1, 1]
        res = 6
        self.assertEqual(Solution().findMaxLength(nums), res)


if __name__ == "__main__":
    unittest.main()
