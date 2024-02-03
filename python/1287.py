#  Category: algorithms
#  Level: Easy
#  Percent: 61.097454%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an integer array sorted in non-decreasing order, there is exactly one
#  integer in the array that occurs more than 25% of the time, return that
#  integer.
#
#
#  Example 1:
#
#  Input: arr = [1,2,2,6,6,6,6,7,10]
#  Output: 6
#
#
#  Example 2:
#
#  Input: arr = [1,1]
#  Output: 1
#
#
#
#  Constraints:
#
#
#  	1 <= arr.length <= 10⁴
#  	0 <= arr[i] <= 10⁵
#


import unittest

#  start_marker
from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        try:
            return Counter(arr).most_common(1)[0][0]
        except IndexError:
            return -1


#  end_marker


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]), 6)

    def test2(self):
        self.assertEqual(Solution().findSpecialInteger([1, 1]), 1)

    def test3(self):
        self.assertEqual(Solution().findSpecialInteger([]), None)

    def test4(self):
        self.assertEqual(
            Solution().findSpecialInteger(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
            ),
            1,
        )


if __name__ == "__main__":
    unittest.main()
