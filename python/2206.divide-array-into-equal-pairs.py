#  Category: algorithms
#  Level: Easy
#  Percent: 73.371414%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an integer array nums consisting of 2 * n integers.
#
#  You need to divide nums into n pairs such that:
#
#
#  	Each element belongs to exactly one pair.
#  	The elements present in a pair are equal.
#
#
#  Return true if nums can be divided into n pairs, otherwise return false.
#
#
#  Example 1:
#
#  Input: nums = [3,2,3,2,2,2]
#  Output: true
#  Explanation:
#  There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
#  If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.
#
#
#  Example 2:
#
#  Input: nums = [1,2,3,4]
#  Output: false
#  Explanation:
#  There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy every condition.
#
#
#
#  Constraints:
#
#
#  	nums.length == 2 * n
#  	1 <= n <= 500
#  	1 <= nums[i] <= 500
#

import unittest
from collections import Counter
from typing import List


#  start_marker
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for k in c:
            if c[k] % 2 == 1:
                return False
        return True
        #  end_marker


class TestSolution(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().divideArray([3, 2, 3, 2, 2, 2]), True)

    def test2(self):
        self.assertEqual(Solution().divideArray([1, 2, 3, 4]), False)


if __name__ == "__main__":
    unittest.main()
