#  Category: algorithms
#  Level: Medium
#  Percent: 54.731308%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given an integer array height of length n. There are n vertical
#  lines drawn such that the two endpoints of the ith line are (i, 0) and (i,
#  height[i]).
#
#  Find two lines that together with the x-axis form a container, such that the
#  container contains the most water.
#
#  Return the maximum amount of water a container can store.
#
#  Notice that you may not slant the container.
#
#
#  Example 1:
#
#  Input: height = [1,8,6,2,5,4,8,3,7]
#  Output: 49
#  Explanation: The above vertical lines are represented by array
#  [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
#  container can contain is 49.
#
#
#  Example 2:
#
#  Input: height = [1,1]
#  Output: 1
#
#
#
#  Constraints:
#
#
#  	n == height.length
#  	2 <= n <= 10⁵
#  	0 <= height[i] <= 10⁴

import unittest
from typing import List


#  start_marker
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            # print(f"{left=} {right=}")
            area = min(height[left], height[right]) * (right - left)
            # print(f"{area=} {max_area=}")
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        # end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input_data = [1, 1]
        expected = 1
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)

    def test_case_2(self):
        input_data = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)

    def test_case_3(self):
        input_data = [1, 2, 1]
        expected = 2
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)

    def test_case_4(self):
        input_data = [1, 2, 4, 3]
        expected = 4
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)

    def test_case_5(self):
        input_data = [1, 2, 1, 3]
        expected = 4
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)

    def test_case_6(self):
        input_data = [1, 2, 1, 3, 1]
        expected = 4
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)

    def test_case_7(self):
        input_data = [1, 3, 1, 3, 1]
        expected = 6
        result = Solution().maxArea(input_data)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
