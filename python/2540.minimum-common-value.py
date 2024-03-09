#  Category: algorithms
#  Level: Easy
#  Percent: 54.1%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring

#
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
#
#
#
# Example 1:
#
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# Explanation: The smallest element common to both arrays is 2, so we return 2.
#
# Example 2:
#
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
#
#
#
# Constraints:
#
#     1 <= nums1.length, nums2.length <= 105
#     1 <= nums1[i], nums2[j] <= 109
#     Both nums1 and nums2 are sorted in non-decreasing order.
#

import unittest
from typing import List


#  start_marker
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        curr1 = 0
        curr2 = 0
        while curr1 < len(nums1) and curr2 < len(nums2):
            if nums1[curr1] == nums2[curr2]:
                return nums1[curr1]
            elif nums1[curr1] < nums2[curr2]:
                curr1 += 1
            else:
                curr2 += 1
        return -1

        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums1 = [1, 2, 3]
        nums2 = [2, 4]
        expected_result = 2
        result = Solution().getCommon(nums1, nums2)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        nums1 = [1, 2, 3, 6]
        nums2 = [2, 3, 4, 5]
        expected_result = 2
        result = Solution().getCommon(nums1, nums2)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
