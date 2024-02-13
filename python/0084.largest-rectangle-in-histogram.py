#  Category: algorithms
#  Level: Hard
#  Percent: 43.91087%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#
#
#  Example 1:
#
#  Input: heights = [2,1,5,6,2,3]
#  Output: 10
#  Explanation: The above is a histogram where width of each bar is 1.
#  The largest rectangle is shown in the red area, which has an area = 10 units.
#
#
#  Example 2:
#
#  Input: heights = [2,4]
#  Output: 4
#
#
#
#  Constraints:
#
#
#  	1 <= heights.length <= 10⁵
#  	0 <= heights[i] <= 10⁴
#

import unittest
from typing import List, Tuple


#  start_marker
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[Tuple[int, int]] = []
        max_area = 0
        for i, h in enumerate(heights):
            # print(f"i: {i}, h: {h}, stack: {stack}")
            start: int = i
            while stack and stack[-1][1] > h:
                # print(f"stack: {stack}")
                old_i, old_h = stack.pop()
                # print(f"old_i: {old_i}, old_h: {old_h}")
                area = (i - old_i) * old_h
                max_area = max(area, max_area)
                # print(f"area: {area}, max_area: {max_area}")
                start = old_i
            if not stack or stack[-1][1] < h:
                stack.append((start, h))
        # print(f"stack at end: {stack}")
        while stack:
            old_i, old_h = stack.pop()
            # print(f"old_i: {old_i}, old_h: {old_h}")
            area = (len(heights) - old_i) * old_h
            max_area = max(area, max_area)
            # print(f"area: {area}, max_area: {max_area}")
        return max_area
        #  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        heights = [2, 1, 5, 6, 2, 3]
        expected = 10
        result = Solution().largestRectangleArea(heights)
        self.assertEqual(result, expected)

    def test_case_2(self):
        heights = [2, 4]
        expected = 4
        result = Solution().largestRectangleArea(heights)
        self.assertEqual(result, expected)

    def test_case_3(self):
        heights = [2, 1, 2]
        expected = 3
        result = Solution().largestRectangleArea(heights)
        self.assertEqual(result, expected)

    def test_case_4(self):
        heights = [2, 1, 2, 1]
        expected = 4
        result = Solution().largestRectangleArea(heights)
        self.assertEqual(result, expected)

    def test_case_5(self):
        heights = [2, 1, 2, 1, 2]
        expected = 5
        result = Solution().largestRectangleArea(heights)
        self.assertEqual(result, expected)

    def test_case_6(self):
        heights = [2]
        expected = 2
        result = Solution().largestRectangleArea(heights)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
